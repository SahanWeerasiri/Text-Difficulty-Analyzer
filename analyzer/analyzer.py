import nltk
from nltk.tokenize import sent_tokenize
import math

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

from analyzer import sentence_structure, vocabulary, readability

def analyze_text_difficulty(text: str) -> float:
    """Analyzes the difficulty of a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        float: A difficulty score (higher is more difficult).
    """
    try:
        sentences = sent_tokenize(text)

        if not sentences:
            return 0.0

        structure_score = sentence_structure.analyze_sentence_structure(sentences)
        vocab_score = vocabulary.analyze_vocabulary(text)
        readability_score = readability.calculate_readability(text)

        if any(score <= 0 for score in [structure_score, vocab_score, readability_score]):
            return 0.0

        geometric_mean = math.pow(structure_score * vocab_score * readability_score, 1/3)

        return geometric_mean
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise