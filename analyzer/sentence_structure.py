import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

stop_words = set(stopwords.words('english'))


def analyze_sentence_structure(sentences: list[str]) -> float:
    """Analyzes the sentence structure of a list of sentences.

    Args:
        sentences (list[str]): A list of sentences to analyze.

    Returns:
        float: A score representing the complexity of the sentence structure.
               A higher score indicates more complex structures.
    """
    if not sentences:
        return 0.1

    total_sentences = len(sentences)
    total_words = 0
    long_sentence_count = 0
    long_sentence_threshold = 15

    for sentence in sentences:
        words = word_tokenize(sentence)
        num_words = len(words)
        total_words += num_words
        if num_words > long_sentence_threshold:
            long_sentence_count += 1

    average_sentence_length = total_words / total_sentences
    long_sentence_ratio = long_sentence_count / total_sentences

    structure_score = average_sentence_length * long_sentence_ratio

    return max(structure_score, 0.1)