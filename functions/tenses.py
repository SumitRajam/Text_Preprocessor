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

    # Initialize tense info
    tense_info = {'present': False, 'past': False, 'future': False,
                  'continuous': False, 'perfect': False, 'conditional': False}

    # Check for conditionals
    if 'if' in tokens and any(word in tokens for word in ['had', 'were', 'would', 'should']):
        tense_info['conditional'] = True

    # Extract main verb and its tag
    main_verb = None
    for word, tag in pos_tags:
        if tag.startswith('V'):
            main_verb = (word, tag)
            break

    if main_verb:
        verb, tag = main_verb
        # Check for future tense
        if 'will' in tokens or 'shall' in tokens:
            tense_info['future'] = True
            if 'ing' in verb:
                tense_info['continuous'] = True
            if 'been' in tokens:
                tense_info['perfect'] = True
        # Check for present perfect
        elif verb in ['has', 'have'] and any(pos.startswith('VBN') for _, pos in pos_tags[1:]):
            tense_info['present'] = True
            tense_info['perfect'] = True
        # Check for past perfect
        elif verb == 'had' and any(pos.startswith('VBN') for _, pos in pos_tags[1:]):
            tense_info['past'] = True
            tense_info['perfect'] = True
        # Check for future perfect
        elif 'will' in tokens and 'have' in tokens and any(pos.startswith('VBN') for _, pos in pos_tags[1:]):
            tense_info['future'] = True
            tense_info['perfect'] = True
        # Check for other tenses
        elif tag.startswith('VBD'):
            tense_info['past'] = True
        elif tag.startswith('VBG'):
            tense_info['continuous'] = True
        elif tag.startswith('VB'):
            tense_info['present'] = True

    # Determine overall tense
    if tense_info['conditional']:
        return "Conditional Perfect Tense" if tense_info['perfect'] else "Conditional Tense"
    elif tense_info['future']:
        if tense_info['continuous']:
            return "Future Continuous Tense" if not tense_info['perfect'] else "Future Perfect Continuous Tense"
        elif tense_info['perfect']:
            return "Future Perfect Tense"
        else:
            return "Future Tense"
    elif tense_info['past']:
        if tense_info['continuous']:
            return "Past Continuous Tense" if not tense_info['perfect'] else "Past Perfect Continuous Tense"
        elif tense_info['perfect']:
            return "Past Perfect Tense"
        else:
            return "Past Tense"
    elif tense_info['present']:
        if tense_info['continuous']:
            return "Present Continuous Tense" if not tense_info['perfect'] else "Present Perfect Continuous Tense"
        elif tense_info['perfect']:
            return "Present Perfect Tense"
        else:
            return "Present Tense"
    else:
        return "Unknown Tense"

def process_text1(text):
    """Process the input text and return the tense of each sentence."""
    sentences = sent_tokenize(text)
    results = []
    for sentence in sentences:
        tense = determine_tense(sentence)
        results.append(f"{sentence} -> {tense}")
    return '\n'.join(results)

# Example usage:
text = "I ate mango."
print(process_text1(text))  # Output should be "I ate mango -> Past Tense"
