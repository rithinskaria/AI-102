# This script demonstrates text-to-speech synthesis using Azure Cognitive Services.
# It converts a given text into speech and plays it through the default speaker.
# Additionally, it saves the synthesized speech to an audio file.
# Requirements:
# - Install the Azure Cognitive Services Speech SDK (`pip install azure-cognitiveservices-speech`).
# - Replace `<YOUR_SPEECH_KEY>` and `<YOUR_SERVICE_REGION>` with your Azure Speech key and region.

import azure.cognitiveservices.speech as speechsdk

speech_key = "<YOUR_SPEECH_KEY>"
service_region = "<YOUR_SERVICE_REGION>"

if not speech_key:
    raise ValueError("You must set your Azure Speech key.")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
text = "Welcome to the AI-102 course — your gateway to building smart apps with Azure AI! From computer vision to chatbots... we'll cover it all. Let’s get started and level up your AI skills"

result = synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized successfully to speaker.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print("Speech synthesis canceled:", cancellation.reason)
    if cancellation.reason == speechsdk.CancellationReason.Error:
        print("Error details:", cancellation.error_details)

audio_config = speechsdk.audio.AudioOutputConfig(filename="output_audio.wav")
file_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

file_result = file_synthesizer.speak_text_async(text).get()

if file_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Audio saved to 'output_audio.wav'")
elif file_result.reason == speechsdk.ResultReason.Canceled:
    cancellation = file_result.cancellation_details
    print("File synthesis canceled:", cancellation.reason)
    if cancellation.reason == speechsdk.CancellationReason.Error:
        print("Error details:", cancellation.error_details)
