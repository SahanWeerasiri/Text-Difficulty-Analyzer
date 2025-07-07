```python
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from analyzer import sentence_structure, vocabulary, readability
import math

# Download necessary NLTK data
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

def analyze_text_difficulty(text: str) -> float:
    """Analyzes the difficulty of a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        float: A difficulty score (higher is more difficult).
    """
    try:
        sentences = sent_tokenize(text)

        # Handle edge case of empty string.
        if not sentences:
            return 0.0

        sentence_structure_score = sentence_structure.analyze_sentence_structure(sentences)
        vocabulary_score = vocabulary.analyze_vocabulary(text)
        readability_score = readability.calculate_readability(text)

        # Combine scores (you can adjust weights as needed)
        # Using a geometric mean to penalize low scores across any one factor.

        geometric_mean = math.pow(sentence_structure_score * vocabulary_score * readability_score, 1/3) if (sentence_structure_score > 0 and vocabulary_score > 0 and readability_score > 0) else 0


        return geometric_mean
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise
```