"""
This script demonstrates how to use Azure Cognitive Services Speech SDK to perform speech-to-text translation and text-to-speech synthesis. 
It translates speech from an audio file into a target language and plays the translated text as synthesized speech.

Requirements:
- Install the Azure Cognitive Services Speech SDK (`pip install azure-cognitiveservices-speech`).
- Replace `<YOUR_SPEECH_KEY>` and `<YOUR_SERVICE_REGION>` with your Azure Speech service subscription key and region.
- Provide the path to the input audio file in WAV format (`<YOUR_AUDIO_FILE>`).
- Ensure the target language and voice name are correctly set for translation and synthesis.

Modules:
- azure.cognitiveservices.speech
"""

import azure.cognitiveservices.speech as speechsdk

speech_key = "<YOUR_SPEECH_KEY>"
service_region = "<YOUR_SERVICE_REGION>"
audio_file = "<YOUR_AUDIO_FILE>"

translation_config = speechsdk.translation.SpeechTranslationConfig(
    subscription=speech_key,
    region=service_region
)
translation_config.speech_recognition_language = "en-US"
translation_config.add_target_language("es")

audio_input = speechsdk.audio.AudioConfig(filename=audio_file)

translator = speechsdk.translation.TranslationRecognizer(
    translation_config=translation_config,
    audio_config=audio_input
)

result = translator.recognize_once_async().get()

if result.reason == speechsdk.ResultReason.TranslatedSpeech:
    translated_text = result.translations["es"]

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = "es-ES-ElviraNeural"
    speaker_output = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=speaker_output
    )

    synthesis_result = speech_synthesizer.speak_text_async(translated_text).get()

    if synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Translation and synthesis completed successfully.")
    else:
        print("Synthesis failed:", synthesis_result.reason)

elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech recognized.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print("Translation canceled:", cancellation.reason)
    if cancellation.reason == speechsdk.CancellationReason.Error:
        print("Error details:", cancellation.error_details)