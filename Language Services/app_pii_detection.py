"""
This script demonstrates how to use Azure's Text Analytics API to detect Personally Identifiable Information (PII) in text. 
To run this code, you need:
- Azure SDK for Python (`azure-ai-textanalytics` and `azure-core` modules)
- An Azure Cognitive Services resource with the Text Analytics API enabled
- Replace `<your_endpoint>` and `<your_key>` with your Azure resource endpoint and key.

The script authenticates the client, sends a text document for PII detection, and prints the detected PII entities along with their categories and confidence scores.
"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "<your_endpoint>"
key = "<your_key>"

documents = [
    "Sample text containing PII information."
]

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response = client.recognize_pii_entities(documents=documents)

for idx, doc in enumerate(response):
    print(f"\nText: {documents[idx]}")
    if not doc.is_error:
        print("\n\nDetected PII Entities:")
        for entity in doc.entities:
            print(f" - {entity.text} ({entity.category}, Confidence: {entity.confidence_score:.2f})")
    else:
        print(f"Error: {doc.error}")
