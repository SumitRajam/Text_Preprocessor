import sys
from nltk.tokenize import word_tokenize


def tokenize_text(text):
    # Tokenize the input text
    tokens = word_tokenize(text)
    # Format tokens for output
    return ' '.join(f"'{token}'" for token in tokens)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])  # Join arguments to handle multi-word input
        print(tokenize_text(input_text))
    else:
        print("No input text provided.")
