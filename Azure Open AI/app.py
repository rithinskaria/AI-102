# Flask application for interacting with Azure OpenAI service

# This code sets up a Flask web application that integrates with Azure OpenAI to provide a chatbot interface.
# Requirements:
# - Install required Python modules: `flask`, `openai`
# - Replace placeholders with actual values:
#   - `API_KEY`, `API_VERSION`, `AZURE_ENDPOINT`, and `DEPLOYMENT_NAME`

from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI

app = Flask(__name__)

client = AzureOpenAI(
    api_key="API_KEY",
    api_version="API_VERSION",
    azure_endpoint="AZURE_ENDPOINT"
)

DEPLOYMENT_NAME = "DEPLOYMENT_NAME"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150
    )
    reply = response.choices[0].message.content.strip()
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
