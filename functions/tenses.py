import nltk
from nltk.tokenize import sent_tokenize
from nltk import pos_tag, word_tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def determine_tense(sentence):
    """Determine the tense of the given sentence."""
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)

    # Extract tense-related tags and words
    tense_info = {'present': False, 'past': False, 'future': False,
                  'continuous': False, 'perfect': False, 'conditional': False}

    # Check for conditionals
    if 'if' in tokens and any(word in tokens for word in ['had', 'were', 'would', 'should']):
        tense_info['conditional'] = True

    # Check for tense
    for word, tag in pos_tags:
        if tag.startswith('V'):
            # Check for future tense first
            if any(future_word in tokens for future_word in ['will', 'shall']):
                tense_info['future'] = True
                continue  # Skip further checks for this verb

            if 'ing' in word:
                tense_info['continuous'] = True
            elif tag.startswith('VBD') or tag.startswith('VBN'):
                tense_info['past'] = True
            elif tag.startswith('VB'):
                tense_info['present'] = True
            # Check for present perfect simple
            if word == 'has' and any(pos.startswith('VBN') for _, pos in pos_tags[1:]):
                tense_info['present'] = True
                tense_info['perfect'] = True

    # Determine overall tense
    if tense_info['conditional']:
        return "Conditional Perfect Tense" if tense_info['perfect'] else "Conditional Tense"
    elif tense_info['future']:
        if tense_info['continuous']:
            return "Future Continuous Tense"
        elif tense_info['perfect']:
            return "Future Perfect Tense"
        else:
            return "Future Tense"
    elif tense_info['past']:
        if tense_info['continuous']:
            return "Past Continuous Tense"
        elif tense_info['perfect']:
            return "Past Perfect Tense"
        else:
            return "Past Tense"
    elif tense_info['present']:
        if tense_info['continuous']:
            return "Present Continuous Tense"
        elif tense_info['perfect']:
            return "Present Perfect Tense"
        else:
            return "Present Tense"
    else:
        return "Unknown Tense"


def process_text(text):
    """Process the input text and return the tense of each sentence."""
    sentences = sent_tokenize(text)
    results = []
    for sentence in sentences:
        tense = determine_tense(sentence)
        results.append(f"{sentence} -> {tense}")
    return '\n'.join(results)
