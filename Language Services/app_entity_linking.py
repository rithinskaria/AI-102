"""
This script demonstrates how to use Azure's Text Analytics API to perform entity linking on a set of documents. 
Entity linking identifies and links entities in text to their corresponding entries in a knowledge base.

Requirements:
- Install the Azure SDK for Python: `pip install azure-ai-textanalytics`
- Replace `<YOUR_ENDPOINT>` and `<YOUR_KEY>` with your Azure Cognitive Services endpoint and key.
- Provide a list of documents to analyze.

"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "<YOUR_ENDPOINT>"
key = "<YOUR_KEY>"

documents = [
    "Eiffel tower is located in Paris."
]

credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

response = client.recognize_linked_entities(documents=documents)

for idx, doc in enumerate(response):
    print(f"\nText: {documents[idx]}")
    if not doc.is_error:
        print("\n\nLinked Entities:")
        for entity in doc.entities:
            print(f" - Name: {entity.name}")
            print(f"   ID: {entity.data_source_entity_id}")
            print(f"   URL: {entity.url}")
            print(f"   Source: {entity.data_source}")
            print(f"   Matches:")
            for match in entity.matches:
                print(f"     > '{match.text}' (Confidence: {match.confidence_score:.2f})")
    else:
        print(f"Error: {doc.error}")
