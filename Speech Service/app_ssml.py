"""
This script demonstrates how to use Azure Cognitive Services Speech SDK to synthesize speech from SSML (Speech Synthesis Markup Language) content. 
It requires an Azure Speech resource with a valid subscription key and region. 
Ensure the `azure-cognitiveservices-speech` module is installed before running the script.

Required:
- Azure Speech resource subscription key and region
- Install the Speech SDK: `pip install azure-cognitiveservices-speech`
"""

import azure.cognitiveservices.speech as speechsdk

speech_key = "<YOUR_AZURE_SPEECH_KEY>"
service_region = "<YOUR_SERVICE_REGION>"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

ssml = """
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis'
  xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>
  <voice name='en-US-JennyNeural'>
    <mstts:express-as style='cheerful'>
      <prosody rate='-10%' pitch='+4%'>
   Welcome to the AI-102 course — your gateway to building smart apps with Azure AI.
      </prosody>
    </mstts:express-as>
    <break time='500ms'/>
    <prosody rate='-12%'>
      From computer vision... to chatbots... we’ll cover it all.
    </prosody>
    <break time='400ms'/>
    <mstts:express-as style='excited'>
      <prosody rate='-10%'>
   Let’s get started — and level up your AI skills.
      </prosody>
    </mstts:express-as>
  </voice>
</speak>
"""

result = speech_synthesizer.speak_ssml_async(ssml).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized and played through speaker.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation.reason))
    if cancellation.reason == speechsdk.CancellationReason.Error:
      print("Error details: {}".format(cancellation.error_details))
