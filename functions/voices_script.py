from nltk.tokenize import word_tokenize
from nltk import pos_tag


def check_voices(text):
    """Identify the voice of verbs in the text (active/passive)."""
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    voices = {'active': [], 'passive': []}
    
    # Iterate through the tokens and their tags
    for i in range(len(tokens)):
        word = tokens[i]
        tag = tagged[i][1]

        if tag.startswith('VB'):
            # Check if the next token is "by"
            if i + 1 < len(tokens) and tokens[i + 1].lower() == 'by':
                voices['passive'].append(word)
                # Skip the "by" and the word following it (which might be the agent in passive voice)
                i += 2
            else:
                voices['active'].append(word)
    
    if len(voices['passive']) != 0:
        return f"Passive voice -> {', '.join(voices['passive'])} by"
    elif len(voices['active']) != 0:
        return f"Active voice verbs: {', '.join(voices['active'])}"
    else:
        return "No verbs found"

# Example usage
# text = "The cake was eaten by the children."
# print(check_voices(text))
