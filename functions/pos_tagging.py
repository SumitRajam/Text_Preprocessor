from nltk.tokenize import word_tokenize
from nltk import pos_tag


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
    'UH': 'Interjection',
    'V': 'Verb',
    'WH': 'WH Determiner'
}

def tag_text(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    # Convert tags to full forms and filter out punctuation
    tagged_full = [(word, tag_map.get(tag, tag)) for word, tag in tagged if word.isalpha()]
    
    # Format as 'word -> POS tag'
    formatted_output = '\n'.join(f"{word} -> {tag}" for word, tag in tagged_full)
    return formatted_output
