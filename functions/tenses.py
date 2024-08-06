import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_sentences(text):
    """Extract sentences from the given text."""
    return sent_tokenize(text)

def split_sentence_at_tags(sentence):
    """Split a sentence into clauses based on WH-words, prepositions, conjunctions, and punctuation."""
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    
    pattern = r'\s+(who|whom|whose|which|that|where|when|why|if|although|because|since|unless|while|during|for|in|on|at|by|with|and|but|or|nor|so|yet)\s+|(?<!\w)([.,])|(\s+--\s+)'
    
    sentence_str = ' '.join(tokens)
    clauses = re.split(pattern, sentence_str, flags=re.IGNORECASE)
    clauses = [clause.strip() for clause in clauses if clause and clause.strip()]
    
    return clauses

def is_subordinate_clause(clause):
    """Check if a clause is a subordinate or adverbial clause."""
    subordinating_conjunctions = {'although', 'because', 'since', 'if', 'unless', 'while', 'when', 'where', 'why', 'that', 'whom', 'whose', 'which'}
    adverbial_conjunctions = {'after', 'by the time', 'before', 'due to','when', 'while', 'until', 'as', 'since', 'because', 'although', 'if', 'unless', 'where', 'whether'}
    
    tokens = word_tokenize(clause)
    tagged_tokens = pos_tag(tokens)
    
    return any(word.lower() in adverbial_conjunctions for word, tag in tagged_tokens)

def is_meaningful_clause(clause):
    """Check if a clause contains a subject and predicate."""
    tokens = word_tokenize(clause)
    tagged_tokens = pos_tag(tokens)
    
    has_verb = any(tag.startswith('VB') for word, tag in tagged_tokens)
    has_subject = any(tag in ('NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$') for word, tag in tagged_tokens)
    
    return has_verb and has_subject

def analyze_clauses(text):
    """Analyze and return main, subordinate, and adverbial clauses, and determine the tense of main clauses."""
    sentences = extract_sentences(text)
    main_clauses = []
    subordinate_clauses = []
    adverbial_clauses = []
    
    for sentence in sentences:
        clauses = split_sentence_at_tags(sentence)
        for clause in clauses:
            if 'by the time' in clause.lower() or 'due to' in clause.lower():
                adverbial_clauses.append(clause)
                continue
            if is_subordinate_clause(clause):
                if any(word.lower() in {'when', 'where', 'why', 'how', 'to what extent'} for word, tag in pos_tag(word_tokenize(clause))):
                    adverbial_clauses.append(clause)
                else:
                    subordinate_clauses.append(clause)
            elif is_meaningful_clause(clause):
                main_clauses.append(clause)
    
    return main_clauses, subordinate_clauses, adverbial_clauses

def determine_tense(sentence):
    """Determine the tense of the given sentence."""
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)

    tense_info = {'present': False, 'past': False, 'future': False,
                  'continuous': False, 'perfect': False, 'conditional': False}

    if 'if' in tokens and any(word in tokens for word in ['had', 'were', 'would', 'should']):
        tense_info['conditional'] = True

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
                # print("foo")
                
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
    """Process text to extract main clauses and their tenses."""
    main_clauses, _, _ = analyze_clauses(text)
    result = []
    for clause in main_clauses:
        tense = determine_tense(clause)
        result.append(f"{clause} -> {tense}")
    return "\n".join(result)
