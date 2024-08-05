import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define tag-to-full-form mapping
tag_map = {
    'DET': 'Determiner',
    'NN': 'Noun (common noun)',
    'NNP': 'Noun (proper noun)',
    'VB': 'Verb (base form)',
    'VBD': 'Verb (past tense)',
    'VBG': 'Verb (gerund/present participle)',
    'VBN': 'Verb (past participle)',
    'VBP': 'Verb (non-3rd person singular present)',
    'VBZ': 'Verb (3rd person singular present)',
    'ADJ': 'Adjective',
    'ADV': 'Adverb',
    'NUM': 'Numeral',
    'P': 'Preposition',
    'CNJ': 'Conjunction',
    'PRO': 'Pronoun',
    'VG': 'Verb (gerund)',
    'VD': 'Verb (past participle)',
    'NP': 'Noun Phrase',
    'PP': 'Prepositional Phrase',
    'JJ': 'Adjective',
    'PRP' : 'Personal Pronoun',
    'RB': 'Adverb',
    'IN': 'Preposition',
    'WDT': 'Wh-determiner',
    'NNS': 'Noun, plural',
    'CC': 'Coordinating conjunction',
    'DT': 'Determiner',
    'TO': 'Infinitive marker',
    'PRP$': 'Possessive pronoun',
    'JJ': 'Adjective',
    'PRP': 'Personal pronoun',
    'NN': 'Noun',
    'NP': 'Proper Noun',
    'NUM': 'Number',
    'PRO': 'Pronoun',
    'P': 'Preposition',
    'UH': 'Interjection',
    'V': 'Verb',
    'VD': 'Past Tense',
    'VG': 'Present Participle',
    'VN': 'Past Participle',
    'WH': 'WH Determiner'
}

def tag_text(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    # Convert tags to full forms and filter out punctuation
    tagged_full = [(word, tag_map.get(tag, tag)) for word, tag in tagged if word.isalpha()]
    return tagged_full

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        tagged_output = tag_text(input_text)
        # Print the tagged output in a format suitable for the Tkinter GUI
        for word, tag in tagged_output:
            print(f"{word}: {tag}")
    else:
        print("No input text provided.")
