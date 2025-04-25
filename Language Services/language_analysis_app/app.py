import os
from flask import Flask, request, render_template
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load Azure credentials from .env
load_dotenv()
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")

# Authenticate
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        text = request.form.get("text_input", "").strip()
        print(f"\n📝 Input Text:\n{text}\n")

        if text:
            try:
                # Language Detection
                try:
                    lang = client.detect_language([text])[0]
                    result["language"] = lang.primary_language
                except Exception as e:
                    print("Language detection error:", e)

                # Sentiment
                try:
                    sentiment = client.analyze_sentiment([text])[0]
                    result["sentiment"] = {
                        "sentiment": sentiment.sentiment,
                        "confidence": sentiment.confidence_scores
                    }
                except Exception as e:
                    print("Sentiment analysis error:", e)

                # Key Phrases
                try:
                    result["key_phrases"] = client.extract_key_phrases([text])[0].key_phrases
                except Exception as e:
                    print("Key phrase extraction error:", e)

                # Named Entities
                try:
                    result["ner"] = client.recognize_entities([text])[0].entities
                except Exception as e:
                    print("NER error:", e)

                # Entity Linking
                try:
                    result["linked_entities"] = client.recognize_linked_entities([text])[0].entities
                except Exception as e:
                    print("Entity linking error:", e)

                # PII
                try:
                    result["pii"] = client.recognize_pii_entities([text])[0].entities
                except Exception as e:
                    print("PII detection error:", e)

                # Summarization
                try:
                    summary_poller = client.begin_abstract_summary([text], sentence_count=3)
                    result["summary"] = summary_poller.result()[0].summaries
                except Exception as e:
                    print("Summarization error:", e)

            except Exception as ex:
                print("Global error:", ex)
                result["error"] = str(ex)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
