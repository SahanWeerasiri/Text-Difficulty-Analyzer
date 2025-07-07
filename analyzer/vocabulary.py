import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import math

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def analyze_vocabulary(text: str) -> float:
    words = [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]
    
    if not words:
        return 0.0

    word_counts = Counter(words)
    unique_word_count = len(word_counts)
    total_word_count = len(words)

    vocabulary_richness = unique_word_count / total_word_count

    average_word_length = sum(len(word) for word in words) / total_word_count

    vocabulary_score = vocabulary_richness * math.log(average_word_length + 1)

    return vocabulary_score