"""
This script demonstrates how to use Azure's Conversational Language Understanding service to analyze user input and extract intents and entities. 
It requires the Azure SDK for Python, specifically the `azure-ai-language-conversations` package. 
To run this code, you need:
- An Azure Cognitive Services resource with the Conversational Language Understanding feature enabled.
- The endpoint URL and API key for your Azure resource.
- A project name and deployment name configured in your Azure resource.

Replace the placeholders with your actual Azure resource details before running the script.
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

# Replace the placeholders with your Azure resource details
endpoint = "https://<your-endpoint>.cognitiveservices.azure.com"
api_key = "<your-api-key>"
project_name = "<your-project-name>"
deployment_name = "<your-deployment-name>"

client = ConversationAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

user_input = "<user-input-text>"

with client:
    result = client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "user1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": user_input
                }
            },
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name,
                "verbose": True
            }
        }
    )

top_intent = result["result"]["prediction"]["topIntent"]
entities = result["result"]["prediction"]["entities"]

print(f"Top Intent: {top_intent}")
print("Entities:")
for entity in entities:
    print(f" - {entity['category']}: {entity['text']} (Confidence: {entity['confidenceScore']:.2f})")
