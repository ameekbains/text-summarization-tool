import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]

    # Calculate word frequency
    word_freq = nltk.FreqDist(filtered_words)

    # Calculate sentence scores based on word frequency
    sent_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split()) < 30:  # Only consider sentences with fewer than 30 words
                    if sentence not in sent_scores:
                        sent_scores[sentence] = word_freq[word]
                    else:
                        sent_scores[sentence] += word_freq[word]

    # Select the top N sentences with highest scores
    summary_sentences = nlargest(num_sentences, sent_scores, key=sent_scores.get)

    # Join the sentences to create the summary
    summary = ' '.join(summary_sentences)
    return summary

# Example usage
text = """
Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language. It aims to enable computers to understand, interpret, and generate human language in a useful way. NLP techniques are used in various applications, such as language translation, sentiment analysis, and text summarization.
NLTK (Natural Language Toolkit) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources, such as WordNet. NLTK also includes a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.
"""

summary = summarize_text(text)
print(summary)
