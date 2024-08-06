import sys
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string


def stem_text(text):
    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()
    # Initialize stop words
    stop_words = set(stopwords.words('english'))
    # Tokenize the input text
    tokens = word_tokenize(text)
    
    # Remove punctuation and filter out stopwords
    tokens = [token for token in tokens if token.isalpha() or token in string.punctuation]
    
    # Apply stemming and format output
    results = [f"{token} --> {stemmer.stem(token)}" for token in tokens if token.isalpha()]
    formatted_output = '\n'.join(results)
    
    return formatted_output

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])  # Join arguments to handle multi-word input
        print(stem_text(input_text))
    else:
        print("No input text provided.")
