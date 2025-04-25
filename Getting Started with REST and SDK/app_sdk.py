# This script demonstrates how to use the Azure Text Analytics SDK to perform sentiment analysis on a given text.
# Requirements:
# - Install the Azure SDK modules: `pip install azure-ai-textanalytics`
# - Replace the placeholders for `endpoint` and `key` with your Azure Text Analytics endpoint and API key.

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def authenticate_client(endpoint, key):
    credential = AzureKeyCredential(key)
    return TextAnalyticsClient(endpoint=endpoint, credential=credential)

def sentiment_analysis(client, text):
    try:
        response = client.analyze_sentiment([text])[0]
        print(f"Document Sentiment: {response.sentiment}")
        print(f"Scores: positive={response.confidence_scores.positive:.2f}, "
              f"neutral={response.confidence_scores.neutral:.2f}, "
              f"negative={response.confidence_scores.negative:.2f}")
        return response
    except Exception as err:
        print(f"Error: {err}")
        return None

def main():
    endpoint = "<YOUR_ENDPOINT>"
    key = "<YOUR_API_KEY>"
    sample_text = "The hotel is bad. The food and service were unacceptable."
    client = authenticate_client(endpoint, key)
    sentiment_analysis(client, sample_text)

if __name__ == "__main__":
    main()
