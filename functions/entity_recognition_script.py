import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag

# Download required NLTK data
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Define full forms for NER tags
NER_TAGS = {
    'PERSON': 'Person (e.g., names of people)',
    'GPE': 'Geopolitical Entity (e.g., countries, cities, states)',
    'ORGANIZATION': 'Organization (e.g., companies, institutions)',
    'LOCATION': 'Location (e.g., non-GPE locations, mountain ranges, bodies of water)',
    'DATE': 'Date (e.g., specific dates or time periods)',
    'TIME': 'Time (e.g., times of the day)',
    'MONEY': 'Money (e.g., amounts of money)',
    'PERCENT': 'Percent (e.g., percentages)',
    'FACILITY': 'Facility (e.g., buildings, airports)'
}

def recognize_entities(text):
    try:
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        entities = ne_chunk(tagged)
        recognized = []
        for subtree in entities:
            if hasattr(subtree, 'label'):
                entity_text = ' '.join(c[0] for c in subtree)
                entity_label = subtree.label()
                full_form = NER_TAGS.get(entity_label, 'Unknown label')
                recognized.append(f"{entity_text}: {full_form}")
        return '\n'.join(recognized) if recognized else "No entities recognized."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        print(recognize_entities(input_text))
    else:
        print("No input text provided.")
