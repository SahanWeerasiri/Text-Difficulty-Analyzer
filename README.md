# Text Difficulty Analyzer

A backend service that analyzes user-submitted text and returns a difficulty score based on sentence structure, vocabulary, and readability metrics.

## Getting Started

1. Clone the repository: `git clone <repository_url>`
2. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`

## API Endpoints

*   `/analyze`:
    *   Method: `POST`
    *   Content-Type: `application/json`
    *   Request body:
        ```json
        {
            "text": "Your text to analyze goes here."
        }
        ```
    *   Response:
        ```json
        {
            "difficulty_score": 0.75,
            "readability_metrics": {
                "flesch_reading_ease": 60.5,
                "smog_index": 9.2
            },
            "sentence_complexity": 0.6
        }
        ```

## Error Handling

*   The API returns standard HTTP status codes:
    *   `200 OK`: Successful analysis.
    *   `400 Bad Request`: Invalid request body.  Ensure the `text` field is present.
    *   `500 Internal Server Error`: An unexpected error occurred during analysis.

## License

See LICENSE file for details.