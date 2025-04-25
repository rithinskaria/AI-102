"""
This script demonstrates how to use Azure Document Intelligence to analyze ID documents. 
It connects to the Azure Document Intelligence service, processes a document, and extracts 
fields and their confidence scores.

Requirements:
- Install the Azure SDK modules: `azure-core` and `azure-ai-documentintelligence`.
- Set up an Azure Document Intelligence resource and obtain the endpoint and key.
- Replace placeholders for `DOCUMENT_URL`, `DOC_INTEL_ENDPOINT`, and `DOC_INTEL_KEY` with actual values.
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

DOCUMENT_URL = "<DOCUMENT_URL>"
DOC_INTEL_ENDPOINT = "<DOC_INTEL_ENDPOINT>"
DOC_INTEL_KEY = "<DOC_INTEL_KEY>"

client = DocumentIntelligenceClient(
    endpoint=DOC_INTEL_ENDPOINT,
    credential=AzureKeyCredential(DOC_INTEL_KEY)
)

poller = client.begin_analyze_document(
    model_id="prebuilt-idDocument",
    body={"urlSource": DOCUMENT_URL}
)
result = poller.result()

for i, doc in enumerate(result.documents, start=1):
    print(f"\n── Document #{i} (type: {doc.doc_type}) ─────────────────────────")
    for name, field in doc.fields.items():
        value = field.content if field.content is not None else "<no value>"
        print(f"{name:20s}: {str(value):30s}  (confidence: {field.confidence:.2f})")
