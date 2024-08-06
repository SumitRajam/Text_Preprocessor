import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def determine_tense(sentence):
    """Determine the tense of the given sentence."""
    tokens = word_tokenize(sentence)
    print(tokens)
    pos_tags = pos_tag(tokens)

    # Initialize tense info
    tense_info = {
        'present': False, 'past': False, 'future': False,
        'continuous': False, 'perfect': False, 'conditional': False
    }

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
        for string in tokens:
            if "ing" in string:
                tense_info['continuous'] = True
                print("foo")
                
        if 'will' in tokens or 'Will' in tokens or 'Shall' in tokens or 'shall' in tokens:
            tense_info['future'] = True
            if 'been' in tokens or 'have' in tokens:
                tense_info['perfect'] = True
            elif 'ing' in tokens:
                tense_info['continuous'] = True
        # Check for present perfect
        elif verb in ['has', 'have'] and any(pos.startswith('VBN') for _, pos in pos_tags[1:]):
            tense_info['present'] = True
            tense_info['perfect'] = True
        # Check for past perfect
        elif verb == 'had' and any(pos.startswith('VBN') for _, pos in pos_tags[1:]):
            tense_info['past'] = True
            tense_info['perfect'] = True
        # Check for other tenses
        elif tag.startswith('VBG'):
            tense_info['continuous'] = True
        elif tag.startswith('VBD'):
            tense_info['past'] = True
        elif tag.startswith('VB'):
            tense_info['present'] = True

    # Determine overall tense
    if tense_info['conditional']:
        return "Conditional Perfect Tense" if tense_info['perfect'] else "Conditional Tense"
    elif tense_info['future']:
        if tense_info['continuous'] and tense_info['perfect']:
            return "Future Perfect Continuous Tense"
        elif tense_info['continuous']:
            return "Future Continuous Tense"
        elif tense_info['perfect']:
            return "Future Perfect Tense"
        else:
            return "Future Tense"
    elif tense_info['past']:
        if tense_info['continuous'] and tense_info['perfect']:
            return "Past Perfect Continuous Tense"
        elif tense_info['continuous']:
            return "Past Continuous Tense"
        elif tense_info['perfect']:
            return "Past Perfect Tense"
        else:
            return "Simple Past Tense"
    elif tense_info['present']:
        if tense_info['continuous'] and tense_info['perfect']:
            return "Present Perfect Continuous Tense"
        elif tense_info['continuous']:
            return "Present Continuous Tense"
        elif tense_info['perfect']:
            return "Present Perfect Tense"
        else:
            return "Simple Present Tense"
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

# Futur tense test:
# text = "She will complete her assignment tomorrow."
# print(process_text1(text))
# text1 = "Will you be attending the conference tomorrow?"
# print(process_text1(text1))
# text2 = "By the end of this year, they will have finished the construction."
# print(process_text1(text2)) 
# text3 = "By next year, I will have been studying here for five years."
# print(process_text1(text3)) 

# Present tense test cases
# text4 = "She completes her assignment every day."
# print(process_text1(text4))  # Simple Present Tense

# text5 = "She is completing her assignment right now."
# print(process_text1(text5))  # Present Continuous Tense

# text6 = "Before i asked her, she have completed her assignment."
# print(process_text1(text6))  # Present Perfect Tense

# text7 = "She have been working here for three years."
# print(process_text1(text7))  # Present Perfect Continuous Tense

# # Past tense test cases
# text8 = "She completed her assignment yesterday."
# print(process_text1(text8))  # Simple Past Tense

# text9 = "She was completing her assignment when the power went out."
# print(process_text1(text9))  # Past Continuous Tense

# text10 = "By the time you arrived, she had completed her assignment."
# print(process_text1(text10))  # Past Perfect Tense

# text11 = "By last year, she had been working here for five years."
# print(process_text1(text11))  # Past Perfect Continuous Tense 