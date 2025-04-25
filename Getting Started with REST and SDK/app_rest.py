"""
This script performs sentiment analysis using a REST API. It sends a text input to the API and retrieves the sentiment analysis results, including overall sentiment and confidence scores.

Requirements:
- Install the `requests` module (`pip install requests`).
- Replace placeholders `YOUR_ENDPOINT_URL`, `YOUR_SUBSCRIPTION_KEY`, and `YOUR_SAMPLE_TEXT` with appropriate values.
- The API endpoint must support sentiment analysis with the specified request format.

Functions:
- `sentiment_analysis(endpoint, key, text)`: Sends a request to the API and processes the response.
- `main()`: Entry point to execute the sentiment analysis with placeholder values.
"""

import json
import requests

def sentiment_analysis(endpoint, key, text):
    url = f"{endpoint}language/:analyze-text?api-version=2023-04-15-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/json"
    }
    body = {
        "kind": "SentimentAnalysis",
        "parameters": {
            "modelVersion": "latest",
            "opinionMining": "True"
        },
        "analysisInput": {
            "documents": [
                {
                    "id": "1",
                    "language": "en",
                    "text": text
                }
            ]
        }
    }
    try:
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            sentiment_data = response.json()
            document = sentiment_data["results"]["documents"][0]
            print(f"Document Sentiment: {document['sentiment']}")
            scores = document["confidenceScores"]
            print(f"Overall scores: positive={scores['positive']:.2f}, "
                  f"neutral={scores['neutral']:.2f}, "
                  f"negative={scores['negative']:.2f}")
            return document
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    except Exception as err:
        print(f"Encountered exception: {err}")
        return None

def main():
    endpoint = "YOUR_ENDPOINT_URL"
    key = "YOUR_SUBSCRIPTION_KEY"
    sample_text = "YOUR_SAMPLE_TEXT"
    sentiment_analysis(endpoint, key, sample_text)

if __name__ == "__main__":
    main()
