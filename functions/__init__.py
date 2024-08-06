import nltk

# Specify a custom download directory
nltk.data.path.append('./nltk_data')

# Define a function to download NLTK data if not already present
def download_nltk_data():
    # nltk.download('wordnet', download_dir='./nltk_data')
    # nltk.download('averaged_perceptron_tagger', download_dir='./nltk_data')
    # nltk.download('stopwords', download_dir='./nltk_data')
    # nltk.download('punkt', download_dir='./nltk_data')
    nltk_resources = {
        'tokenizers/punkt': 'punkt',
        'corpora/wordnet': 'wordnet',
        'taggers/averaged_perceptron_tagger': 'averaged_perceptron_tagger',
        'corpora/stopwords': 'stopwords'
    }
    for resource, name in nltk_resources.items():
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(name, download_dir='./nltk_data')


# Call the function to ensure NLTK data is downloaded
download_nltk_data()

# Import the functions from the various modules
from .stem_script import stem_text
from .tokenize_script import tokenize_text
from .lemmatize_script import lemmatize_text
from .pos_tagging import tag_text
from .tenses import process_text1
from .clauses import extract_clauses
from .voices_script import check_voices