import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag

def extract_sentences(text):
    """Extract sentences from the given text."""
    sentences = sent_tokenize(text)
    return sentences

def split_sentence_at_conjunctions(sentence):
    """Split a sentence into clauses based on conjunctions."""
    # Split by conjunctions: 'and', 'or', 'but', etc.
    clauses = re.split(r'\s+(?:and|or|but|so|nor|for|yet)\s+', sentence, flags=re.IGNORECASE)
    return [clause.strip() for clause in clauses if clause.strip()]

def is_meaningful_clause(clause):
    """Check if a clause contains a subject and predicate."""
    tokens = word_tokenize(clause)
    tagged_tokens = pos_tag(tokens)
    has_verb = any(tag.startswith('VB') for word, tag in tagged_tokens)
    has_subject = any(tag in ('NN', 'PRP') for word, tag in tagged_tokens)
    return has_verb and has_subject

def extract_clauses(text):
    """Extract and return meaningful clauses from the text."""
    sentences = extract_sentences(text)
    all_clauses = []
    for sentence in sentences:
        # Split the sentence into clauses
        clauses = split_sentence_at_conjunctions(sentence)
        # Filter out meaningful clauses
        meaningful_clauses = [clause for clause in clauses if is_meaningful_clause(clause)]
        all_clauses.extend(meaningful_clauses)
    
    return all_clauses

# Example usage
if __name__ == "__main__":
    text = "I ate mango and it tasted good. She went to the store but forgot to buy milk. He was tired so he went to bed early."
    
    clauses = extract_clauses(text)
    if not clauses:
        print("No meaningful clauses identified.")
    
    for idx, clause in enumerate(clauses):
        print(f"Clause {idx + 1}: {clause}")
