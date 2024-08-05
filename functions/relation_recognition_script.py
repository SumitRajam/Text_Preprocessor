import sys
import re
import nltk
from nltk import pos_tag, word_tokenize, ne_chunk
from nltk.tree import Tree

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_named_entities(text):
  """Extract named entities from text."""
  tokens = word_tokenize(text)
  pos_tags = pos_tag(tokens)
  tree = ne_chunk(pos_tags)
  entities = []

  for subtree in tree:
    if isinstance(subtree, Tree) and subtree.label() in ['PERSON', 'GPE', 'ORG']:
      entity = ' '.join(word for word, tag in subtree.leaves())
      entities.append((entity, subtree.label()))

  return entities

def extract_relations(text, entities):
  """Extract relations based on patterns."""
  relations = []
  used_pairs = set()  # To avoid duplicate relations

  # Define patterns for relation extraction
  patterns = {
    'ORG': re.compile(r'\b(in|based\s+in)\b', re.IGNORECASE),
    'PERSON': re.compile(r'\b(related\s+to|associated\s+with)\b', re.IGNORECASE)
  }

  tokens = word_tokenize(text)
  for i, token in enumerate(tokens):
    for entity, label in entities:
      if token in entity:
        # Check surrounding tokens for relation patterns
        context = ' '.join(tokens[max(i-5, 0):min(i+6, len(tokens))])
        for pattern_label, pattern in patterns.items():
          if pattern.search(context):
            # Only consider relations between different entities
            for other_entity, other_label in entities:
              if other_entity != entity:
                pair = tuple(sorted([entity, other_entity]))
                if pair not in used_pairs:
                  used_pairs.add(pair)
                  relations.append((entity, pattern.pattern, other_entity))

  return relations

def format_relations(relations):
  """Format relations into a human-readable string."""
  formatted_relations = []
  for relation in relations:
    formatted_relations.append(f"Relation between '{relation[0]}' and '{relation[2]}' via '{relation[1]}'")
  return '\n'.join(formatted_relations)

def main():
  if len(sys.argv) != 2:
    print("Usage: python relation_recognition_script.py <text>")
    sys.exit(1)

  text = sys.argv[1]
  entities = extract_named_entities(text)
  relations = extract_relations(text, entities)
  formatted_output = format_relations(relations)

  if formatted_output:
    print(formatted_output)
  else:
    print("No relations found.")

if __name__ == "__main__":
  main()
