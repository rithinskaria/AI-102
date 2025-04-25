"""
This script demonstrates how to use Azure Cognitive Services Speech SDK to perform speech-to-text recognition on an audio file. 
It requires the Azure Speech SDK, an Azure subscription key, a service region, and an audio file for processing.

Requirements:
- Install the Azure Speech SDK: `pip install azure-cognitiveservices-speech`
- Replace `<YOUR_SUBSCRIPTION_KEY>` and `<YOUR_SERVICE_REGION>` with your Azure Speech service subscription key and region.
- Provide the path to the audio file in `<AUDIO_FILE_PATH>`.
"""

import azure.cognitiveservices.speech as speechsdk

speech_key = "<YOUR_SUBSCRIPTION_KEY>"
service_region = "<YOUR_SERVICE_REGION>"
audio_filename = "<AUDIO_FILE_PATH>"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioConfig(filename=audio_filename)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

result = speech_recognizer.recognize_once_async().get()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(result.text)
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print("Speech recognition canceled:", cancellation.reason)
    if cancellation.reason == speechsdk.CancellationReason.Error:
        print("Error details:", cancellation.error_details)
