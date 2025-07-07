import nltk
from nltk.tokenize import sent_tokenize
import math

def ensure_nltk_resources():
    """Ensure all required NLTK resources are downloaded."""
    resources = [
        ('tokenizers/punkt_tab', 'punkt_tab'),
        ('corpora/wordnet', 'wordnet'),
        ('averaged_perceptron_tagger_eng', 'averaged_perceptron_tagger_eng'),
        # Fallback for older NLTK versions
        ('tokenizers/punkt', 'punkt'),
        ('averaged_perceptron_tagger', 'averaged_perceptron_tagger')
    ]
    
    for resource_path, download_name in resources:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            try:
                nltk.download(download_name, quiet=True)
            except:
                pass  # Continue if download fails

# Ensure resources are available
ensure_nltk_resources()

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
            print("No sentences found in the text.")
            return 0.0

        structure_score = sentence_structure.analyze_sentence_structure(sentences)
        vocab_score = vocabulary.analyze_vocabulary(text)
        readability_score = readability.calculate_readability(text)

        if any(score <= 0 for score in [structure_score, vocab_score, readability_score]):
            print("One or more scores are non-positive, returning 0.0.")
            print(f"Structure Score: {structure_score}, Vocabulary Score: {vocab_score}, Readability Score: {readability_score}")
            return 0.0

        geometric_mean = math.pow(structure_score * vocab_score * readability_score, 1/3)
        print(f"Structure Score: {structure_score}, Vocabulary Score: {vocab_score}, Readability Score: {readability_score}, Geometric Mean: {geometric_mean}")
        return geometric_mean
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise