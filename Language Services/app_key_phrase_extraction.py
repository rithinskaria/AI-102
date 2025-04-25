# This script demonstrates how to use Azure's Text Analytics API to extract key phrases from a given text. 
# Requirements:
# - Install the Azure SDK modules: `azure-ai-textanalytics` and `azure-core`
# - Replace `<YOUR_ENDPOINT>` and `<YOUR_API_KEY>` with your Azure Text Analytics endpoint and API key.

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "<YOUR_ENDPOINT>"
key = "<YOUR_API_KEY>"

documents = [
    "Golden retrievers are one of the most popular dog breeds, known for their friendly, intelligent, and devoted nature. They are excellent family pets and are often used as guide dogs, therapy dogs, and in search-and-rescue operations due to their trainability and gentle temperament.",
]

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

response = client.extract_key_phrases(documents=documents)

for idx, doc in enumerate(response):
    print(f"\nText: {documents[idx]}")
    if not doc.is_error:
        print("\n\nKey Phrases:")
        for phrase in doc.key_phrases:
            print(f" - {phrase}")
    else:
        print(f"Error: {doc.error}")
