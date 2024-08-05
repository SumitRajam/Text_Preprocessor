import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def identify_clauses(sentence):
    # Parse the sentence
    doc = nlp(sentence)
    
    # Initialize lists to store clauses
    main_clause = []
    subordinate_clauses = []
    current_clause = []
    subordinate_start = False
    
    for token in doc:
        # Detect the start of subordinate clauses
        if token.dep_ == 'mark':
            if current_clause:
                subordinate_clauses.append(' '.join(current_clause))
                current_clause = []
            subordinate_start = True

        if subordinate_start or token.dep_ in ('ROOT', 'acl', 'advcl'):
            if token.dep_ == 'ROOT':
                if current_clause:
                    subordinate_clauses.append(' '.join(current_clause))
                    current_clause = []
                main_clause.append(token.text)
            else:
                current_clause.append(token.text)
        else:
            if current_clause:
                current_clause.append(token.text)

    if current_clause:
        if not subordinate_start:
            main_clause.append(' '.join(current_clause))
        else:
            subordinate_clauses.append(' '.join(current_clause))

    return ' '.join(main_clause).strip(), [clause.strip() for clause in subordinate_clauses]

# Example sentence
sentence = "All the cars stop when the red light goes on"
main_clause, subordinate_clauses = identify_clauses(sentence)

print("Main Clause:", main_clause)
print("Subordinate Clauses:", subordinate_clauses)
