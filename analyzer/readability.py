import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

stop_words = set(stopwords.words('english'))


def calculate_readability(text: str) -> float:
    """Calculates readability metrics for the text using a simplified approach.

    Args:
        text (str): The text to analyze.

    Returns:
        float: A score representing the readability of the text.
               A higher score indicates lower readability (more difficult).
    """
    try:
        sentences = sent_tokenize(text)
        words = [w.lower() for w in word_tokenize(text) if w.isalpha() and w.lower() not in stop_words]

        if not sentences or not words:
            print("No sentences or words found in the text.")
            return 0.0

        num_sentences = len(sentences)
        num_words = len(words)

        avg_sentence_length = num_words / num_sentences
        complex_words = sum(1 for word in words if len(word) > 6)
        percent_complex_words = (complex_words / num_words) * 100

        # Calculate Flesch Reading Ease score
        readability_score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (complex_words / num_words))
        print(f"Readability Score: {readability_score}, Avg Sentence Length: {avg_sentence_length}, Percent Complex Words: {percent_complex_words}")
        # Ensure the score is within typical Flesch bounds (0-100)
        normalized_score = max(0.0, min(100.0, readability_score))
        return normalized_score

    except Exception as e:
        print(f"Error calculating readability: {e}")
        return 0.0