"""
This script sends a question to an Azure Cognitive Services QnA Maker knowledge base and retrieves the best answer. 
It requires the following:
- An Azure Cognitive Services endpoint URL
- A valid subscription key for the QnA Maker service
- The project name and deployment name of the knowledge base
- The `requests` Python library installed (`pip install requests`)

Replace the placeholders with your specific values before running the script.
"""

import requests

endpoint = "<your-endpoint-url>"
prediction_key = "<your-prediction-key>"
project_name = "<your-project-name>"
deployment_name = "<your-deployment-name>"
question = "<your-question>"

prediction_url = f"{endpoint}/language/:query-knowledgebases?projectName={project_name}&deploymentName={deployment_name}&api-version=2021-10-01"

headers = {
    "Ocp-Apim-Subscription-Key": prediction_key,
    "Content-Type": "application/json"
}

body = {
    "question": question,
    "top": 1
}

response = requests.post(prediction_url, headers=headers, json=body)

if response.status_code == 200:
    data = response.json()
    if data["answers"]:
        best_answer = data["answers"][0]
        print(f"Q: {question}")
        print(f"A: {best_answer['answer']}")
    else:
        print("No answers found.")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
