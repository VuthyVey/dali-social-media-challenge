import json
data = json.loads(open('./data/dali_social_media.json').read())

# Helper Functions

def search_by_name(name):
    for member in data:
        if member['name'] == name:
            return member
    return None

from collections import Counter
import re
from nltk.util import ngrams  # nltk is a natural language toolkit for Python

def tokenize(text):
    # Remove punctuation and split into words
    if text:
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    return ""

# Common English stopwords, extend this list as needed
stopwords = set(["a", "am", "is", "in", "it", "the", "to", "and", "but", "we", "you", "over", "so", "not", "on", "with", "for", "as", "of", "at", "by", "this", "that", "from", "be", "are", "have", "has", "had", "was", "were", "or", "an", "if", "they", "their", "what", "which", "who", "whom", "these", "those", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])

# Generate bigrams and count their frequencies, excluding stopwords
def get_bigrams(quotes):
    bigrams = []
    for quote in quotes:
        words = [word for word in tokenize(quote) if word not in stopwords]
        bigrams.extend(ngrams(words, 2))

    bigram_counts = Counter(bigrams)
    return bigram_counts

def get_common_words(list_of_text):
    words = tokenize(list_of_text)
    for text in list_of_text:
        words.extend([word for word in tokenize(text) if word not in stopwords])

    word_counts = Counter(words)
    return word_counts.most_common(20)

