"""
This script demonstrates how to interact with Azure's Language service for custom text classification. 
It submits a text classification job, polls for the job's status, and retrieves the results upon completion.

Requirements:
- Install the `requests` module: `pip install requests`
- Replace placeholders with actual values:
    - <your-endpoint>: Azure Cognitive Services endpoint
    - <your-api-key>: Azure API key
    - <your-project-name>: Name of the custom project
    - <your-deployment-name>: Deployment name of the project
    - <your-document-text>: Text to classify
    - <your-language>: Language of the text (e.g., "en" for English)
"""

import requests
import json
import time

endpoint = "<your-endpoint>"
api_key = "<your-api-key>"
project_name = "<your-project-name>"
deployment_name = "<your-deployment-name>"
document_text = "<your-document-text>"
language = "<your-language>"

submit_url = f"{endpoint}/language/analyze-text/jobs?api-version=2024-11-15-preview"
headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/json"
}
payload = {
        "displayName": "CustomTextPortal_CustomSingleLabelClassification",
        "analysisInput": {
                "documents": [
                        {
                                "id": "1",
                                "language": language,
                                "text": document_text
                        }
                ]
        },
        "tasks": [
                {
                        "kind": "CustomSingleLabelClassification",
                        "parameters": {
                                "projectName": project_name,
                                "deploymentName": deployment_name
                        }
                }
        ]
}

response = requests.post(submit_url, headers=headers, data=json.dumps(payload))
if response.status_code != 202:
        exit(1)

operation_url = response.headers["Operation-Location"]

max_wait_seconds = 60
wait_interval = 3
elapsed = 0

while elapsed < max_wait_seconds:
        poll_response = requests.get(operation_url, headers={"Ocp-Apim-Subscription-Key": api_key})
        if poll_response.status_code != 200:
                break
        
        result = poll_response.json()
        status = result.get("status")
        
        if status in ["notStarted", "running"]:
                time.sleep(wait_interval)
                elapsed += wait_interval
                continue
        elif status == "succeeded":
                if "tasks" in result:
                        tasks = result["tasks"].get("items", [])
                        for task in tasks:
                                if "results" in task:
                                        documents = task["results"].get("documents", [])
                                        for doc in documents:
                                                for classification in doc.get("classifications", []):
                                                        pass
                
                if "results" in result:
                        documents = result["results"].get("documents", [])
                        for doc in documents:
                                for classification in doc.get("classifications", []):
                                        pass
                
                break
        else:
                break
else:
        pass
