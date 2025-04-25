"""
This script uses the Azure Face API to detect faces in an image and extract specific attributes and landmarks. 
It requires the Azure Cognitive Services Face API endpoint and key, along with the URL of the image to analyze.

Requirements:
- Install the following Python packages:
    - azure-cognitiveservices-vision-face
    - msrest
- Replace the placeholders for API endpoint, API key, and image URL with actual values.
"""

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials
import json

ENDPOINT = "<FACE_API_ENDPOINT>"
KEY = "<FACE_API_KEY>"
IMAGE_URL = "<IMAGE_URL>"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

face_attributes = [FaceAttributeType.head_pose]

detected_faces = face_client.face.detect_with_url(
        url=IMAGE_URL,
        return_face_id=False,
        return_face_landmarks=True,
        return_face_attributes=face_attributes
)

print(f"Detected {len(detected_faces)} face(s) in the image.")

if not detected_faces:
        print("No face detected.")
else:
        for face in detected_faces:
                print(f"\nFace ID: {face.face_id}")
                print(f"Glasses: {face.face_attributes.glasses}")
                print("Landmarks:")
                print(f" - Pupil Left: {face.face_landmarks.pupil_left.x}, {face.face_landmarks.pupil_left.y}")
                print(f" - Nose Tip: {face.face_landmarks.nose_tip.x}, {face.face_landmarks.nose_tip.y}")
                print(f" - Mouth Left: {face.face_landmarks.mouth_left.x}, {face.face_landmarks.mouth_left.y}")
                print(f" - Mouth Right: {face.face_landmarks.mouth_right.x}, {face.face_landmarks.mouth_right.y}")

all_faces_json = [face.serialize() for face in detected_faces]
print("\nFull JSON response for all faces:\n")
print(json.dumps(all_faces_json, indent=2))
