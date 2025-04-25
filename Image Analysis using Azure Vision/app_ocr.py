"""
This script performs Optical Character Recognition (OCR) on an image using Azure's Vision API. 
It extracts text from an image provided via a URL. 

Requirements:
- Install the required Python modules: azure-ai-vision, azure-core.
- Set up your Azure Vision API endpoint and key.
- Provide the URL of the image to be analyzed.

Variables:
- `endpoint`: Azure Vision API endpoint (replace with your endpoint).
- `key`: Azure Vision API key (replace with your key).
- `image_url`: URL of the image to be analyzed.
"""

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Replace with your Azure Vision API endpoint and key
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
    visual_features=[VisualFeatures.READ]
)

try:
    if hasattr(result, "as_dict"):
        result_dict = result.as_dict()
    else:
        result_dict = result

    extracted_text = ""
    if "readResult" in result_dict and "blocks" in result_dict["readResult"]:
        for block in result_dict["readResult"]["blocks"]:
            for line in block["lines"]:
                extracted_text += line["text"] + "\n"

    print("Extracted Text:\n")
    print("\033[92m" + extracted_text + "\033[0m")
    print("\n")

except Exception as e:
    print(f"Could not format result as JSON: {str(e)}")
    print(f"Raw response: \n {result} \n\n")
