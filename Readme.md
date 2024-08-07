# Text Preprocessing Project

Welcome to the Text Preprocessing Project! This project is designed to help you preprocess text data using various techniques like tokenization, lemmatization, stemming, and more. It includes a simple Tkinter GUI that allows users to input text and apply different preprocessing functions to it.

## Project Structure

- **Functions/**: This directory includes Python scripts for various text preprocessing functions:
  - `voices_script.py`: For handling different voice processing tasks.
  - `clauses.py`: For clause-based text processing.
  - `tenses.py`: For identifying and modifying tenses in text.
  - `pos_tagging.py`: For part-of-speech tagging.
  - `lemmatize_script.py`: For lemmatization.
  - `stem_script.py`: For stemming.
  - `tokenize_script.py`: For tokenization.
- **nltk_data/**: Contains necessary NLTK data used for various text processing tasks:
  - **corpora/**: Includes corpora like stopwords and WordNet.
  - **taggers/**: Contains the averaged perceptron tagger.
  - **tokenizers/**: Includes the Punkt tokenizer.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **Readme.md**: This file.
- **requirements.txt**: Lists the Python packages required to run the project.
- **run.py**: The main script to run the Tkinter GUI.

## Features

- **Tokenization**: Breaks down text into words or sentences.
- **Lemmatization**: Converts words to their base or dictionary form.
- **Stemming**: Reduces words to their root form.
- **POS Tagging**: Tags parts of speech for each word in the text.
- **Tense Handling**: Identifies and modifies tenses in the text.
- **Clause Processing**: Analyzes and processes clauses within the text.
- **Voice Processing**: Handles different voice-related text transformations.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SumitRajam/Text_Preprocessor.git
   cd Text_Preprocessor
    ```
2. **Install Dependencies**\
   Create a virtual environment and install the required packages
   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage
1. **Run tkinter GUI**\
    Start the application by running:
    ```bash
    python run.py
    ```
    The Tkinter GUI will open, allowing you to input text and apply various preprocessing functions.

2. **Using the GUI**
- **Input Text:** Enter the text you want to preprocess.
- **Select a Function:** Choose a preprocessing function from the available buttons.
- **View Output:** Click the selected button to apply the function and view the results.

## Contributing
We welcome contributions to enhance this project! If you'd like to contribute, please follow these steps:
1. **Fork the Repository:** Click the "Fork" button on the top-right corner of this page.
2. **Create a Branch:** Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature/your-feature-name
    ```
3. **Make Changes:** Implement your changes and commit them.
   ```bash
   git add .
   git commit -m "Add your commit message"
    ```
4. **Push Changes:** Push your changes to your forked repository.
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Create a Pull Request:** Go to the original repository and create a pull request from your forked repository.



# Happy preprocessing! ⚙️💬🧠🖥️