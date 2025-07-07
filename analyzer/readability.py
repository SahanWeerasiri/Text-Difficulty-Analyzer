```python
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

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
        words = [word.lower() for word in word_tokenize(text) if word.isalpha() and word.lower() not in stop_words]

        if not sentences or not words:
            return 0.0

        num_sentences = len(sentences)
        num_words = len(words)

        #Simplified Flesch Reading Ease (modification)
        average_sentence_length = num_words / num_sentences

        # Number of complex words - approximation using word length (adjust threshold)
        complex_word_count = sum(1 for word in words if len(word) > 6)
        percentage_complex_words = (complex_word_count / num_words) * 100

        # Modified Flesch Reading Ease formula, incorporate complex words
        readability_score = 200 - (1.0 * average_sentence_length) - (1.5 * percentage_complex_words)


        return readability_score if readability_score > 0 else 0.1

    except Exception as e:
        print(f"Error calculating readability: {e}")
        return 0.0
```