from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient

# Service endpoint and key
endpoint = "https://aiservicesai900.cognitiveservices.azure.com/"
key = "2nDOsJoeWNZscliGmRVpC88rpvMsF3wF5KjGqcrSUqmjAX1N6zrlJQQJ99AKACYeBjFXJ3w3AAAAACOGr0oi"

# Initialize client
credential = AzureKeyCredential(key)
client = TextTranslationClient(endpoint=endpoint, credential=credential)

# Text to translate
input_text = "좋은 아침입니다. 잘 지내세요?"

body = [
    {
        "text": input_text
    }
]

# Call the translate method
response = client.translate(body=body, to_language=["en", "fr"])


transliteration_response = client.transliterate(
        body=[input_text],
        language="ko",
        from_script="Kore",
        to_script="Latn"
    )
transliteration = transliteration_response[0].text


# Output
print(f"Detected Language: {response[0]['detectedLanguage']['language']} (Score: {response[0]['detectedLanguage']['score']})")
print("\n=== Translation & Transliteration Output ===")
for translation in response[0].translations:
    print(f"\n→ {translation.to.upper()}: {translation.text}")

print(f"\nTransliteration (Latin Script): {transliteration}")
