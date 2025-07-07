import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import math

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def analyze_vocabulary(text: str) -> float:
    words = [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]
    
    if not words:
        return 0.0

    unique_word_count = len(set(words))
    total_word_count = len(words)

    vocabulary_richness = unique_word_count / total_word_count

    average_word_length = sum(map(len, words)) / total_word_count

    vocabulary_score = vocabulary_richness * math.log1p(average_word_length)

    return vocabulary_score