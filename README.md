# Text Summarization Tool using NLTK

This is a simple text summarization tool built using NLTK (Natural Language Toolkit) in Python. The tool takes a text input and generates a summary by selecting the most important sentences based on word frequency.

## Installation

1. Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. Install NLTK using pip:

    ```
    pip install nltk
    ```

3. Download NLTK resources (if not already downloaded):

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

## Usage

1. Import the `summarize_text` function from `summarizer.py` in your Python script.

    ```python
    from summarizer import summarize_text
    ```

2. Call the `summarize_text` function with the text you want to summarize and optionally specify the number of sentences in the summary.

    ```python
    text = "Your input text goes here..."
    summary = summarize_text(text, num_sentences=3)
    print(summary)
    ```

Make sure to replace "Your input text goes here..." with the actual text you want to summarize in the example section. Additionally, ensure that you have a file named `summarizer.py` containing the summarization function in the same directory as your README.md file.

## Example

```python
text = """
Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language. It aims to enable computers to understand, interpret, and generate human language in a useful way. NLP techniques are used in various applications, such as language translation, sentiment analysis, and text summarization.
NLTK (Natural Language Toolkit) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources, such as WordNet. NLTK also includes a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.
"""

summary = summarize_text(text)
print(summary)
Output:
NLP techniques are used in various applications, such as language translation, sentiment analysis, and text summarization. NLTK (Natural Language Toolkit) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources, such as WordNet.
