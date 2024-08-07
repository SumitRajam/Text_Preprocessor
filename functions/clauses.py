import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag


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

def extract_clauses(text):
    """Process text to extract main and subordinate clauses and return as formatted string."""
    main_clauses, subordinate_clauses, adverbial_clauses = analyze_clauses(text)
    
    result = []
    
    for clause in main_clauses:
        result.append(f"{clause} -> Main Clause")
    
    for clause in subordinate_clauses:
        result.append(f"{clause} -> Subordinate Clause")
    
    for clause in adverbial_clauses:
        result.append(f"{clause} -> Adverbial_clauses")
    
    return "\n".join(result)

# Example usage
if __name__ == "__main__":
    texts = ["Although it was raining, the game was not canceled.", "She went to the store, and he stayed home.", "Apple announced a new iPhone model with advanced camera features.", "The United States government is investigating the recent cyberattack.", "Due to heavy rainfall, several flights have been delayed at Mumbai airport."]
    
    results = []
    for text in texts:
        result = extract_clauses(text)
        results.append(result)
    
    # Print results for testing purposes
    for res in results:
        print(res)
