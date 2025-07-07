# Text Difficulty Analyzer

A backend service that analyzes text and returns a difficulty score based on sentence structure, vocabulary, and readability.

## Getting Started

1.  Clone the repository: `git clone <repository_url>`
2.  Create a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate # Linux/macOS
    # venv\Scripts\activate # Windows (PowerShell)
    ```
3.  Install dependencies: `pip install -r requirements.txt`
4.  Run the application: `python main.py`

## API Endpoints

*   **/analyze**

    *   Method: `POST`
    *   Content-Type: `application/json`
    *   Request Body:

        ```json
        {
          "text": "Enter text for analysis here."
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

The API uses standard HTTP status codes:

*   `200 OK`: Successful analysis.
*   `400 Bad Request`: Invalid request. Verify the `text` field exists and is a string.
*   `500 Internal Server Error`: An unexpected error occurred. Check server logs.

## License

See LICENSE file for license information.