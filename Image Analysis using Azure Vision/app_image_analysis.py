"""
This script demonstrates how to use the Azure AI Vision SDK to analyze an image for people detection, 
caption generation, and tag extraction. It connects to the Azure Vision service using a specified 
endpoint and key, analyzes an image from a given URL, and processes the results.

Requirements:
- Install the Azure AI Vision SDK and its dependencies.
- Replace the placeholders for `endpoint`, `key`, and `image_url` with appropriate values.
- Ensure the Azure Vision service is properly configured.

Key Features:
- Detects people in the image and prints their bounding boxes and confidence scores.
- Generates a caption for the image with a confidence score.
- Outputs the raw response from the Azure Vision service as formatted JSON.
"""

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import json

# Replace with your Azure Vision endpoint and key
endpoint = "<YOUR_AZURE_VISION_ENDPOINT>"
key = "<YOUR_AZURE_VISION_KEY>"

# Replace with the URL of the image to analyze
image_url = "<IMAGE_URL>"

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

result = client.analyze_from_url( 
    image_url=image_url,
    visual_features=[VisualFeatures.PEOPLE, VisualFeatures.CAPTION, VisualFeatures.TAGS],
    language="en",
    gender_neutral_caption=True
)

try:
    if hasattr(result, "as_dict"):
        result_dict = result.as_dict()
    else:
        result_dict = result
    
    print("Raw response as formatted JSON:")
    print(json.dumps(result_dict, indent=2))
    print("\n")
except Exception as e:
    print(f"Could not format result as JSON: {str(e)}")
    print(f"Raw response: \n {result} \n\n")

if 'peopleResult' in result and 'values' in result['peopleResult']:
    people = result['peopleResult']['values']
    if people:
        print("People detected!")
        for person in people:
            bounding_box = person.get('boundingBox', {})
            confidence = person.get('confidence', 0)
            print(f"  Bounding Box: x={bounding_box.get('x')}, y={bounding_box.get('y')}, "
                  f"width={bounding_box.get('w')}, height={bounding_box.get('h')}")
            print(f"  Confidence: {confidence:.2f}")
    else:
        print("No people detected.")
else:
    print("No people detected.")

if 'captionResult' in result:
    caption = result['captionResult'].get('text', 'No caption')
    confidence = result['captionResult'].get('confidence', 0)
    print(f"Caption: {caption} (Confidence: {confidence:.2f})")
else:
    print("No caption generated.")
