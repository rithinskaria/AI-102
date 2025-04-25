"""
This script demonstrates a Retrieval-Augmented Generation (RAG) workflow using Azure OpenAI and Azure Cognitive Search. 
It retrieves relevant documents from Azure Cognitive Search and uses Azure OpenAI to generate answers based on the retrieved context.

Requirements:
- Install required Python modules: `openai`, `azure-core`, `azure-search-documents`
- Set up Azure OpenAI and Azure Cognitive Search services
- Replace placeholders with actual values for endpoints, API keys, and deployment names
"""

import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Azure OpenAI settings
azure_openai_endpoint = "<AZURE_OPENAI_ENDPOINT>"
azure_openai_api_key = "<AZURE_OPENAI_API_KEY>"
deployment_name = "<DEPLOYMENT_NAME>"

# Azure Cognitive Search settings
search_endpoint = "<AZURE_SEARCH_ENDPOINT>"
search_key = "<AZURE_SEARCH_API_KEY>"
search_index_name = "<SEARCH_INDEX_NAME>"

client = AzureOpenAI(
    api_key=azure_openai_api_key,
    api_version="2024-02-15-preview",
    azure_endpoint=azure_openai_endpoint
)

def query_search_service(query_text, top_n=5):
    search_client = SearchClient(
        endpoint=search_endpoint,
        index_name=search_index_name,
        credential=AzureKeyCredential(search_key)
    )
    results = search_client.search(
        search_text=query_text,
        top=top_n,
        include_total_count=True
    )
    documents = [result for result in results]
    return documents

def format_documents_for_prompt(documents):
    formatted_docs = []
    for i, doc in enumerate(documents):
        content = f"Document {i+1}:\n"
        for key, value in doc.items():
            if key != "@search.score":
                content += f"{key}: {value}\n"
        formatted_docs.append(content)
    return "\n\n".join(formatted_docs)

def ask_question_with_rag(question):
    relevant_docs = query_search_service(question)
    if not relevant_docs:
        return "No relevant information found to answer your question."
    context = format_documents_for_prompt(relevant_docs)
    system_message = """You are an assistant that answers questions based only on the provided documents. 
If the answer cannot be found in the documents, respond with: 'I don't have information on that topic.'
Use the context to provide accurate, helpful, and concise answers."""
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ],
        temperature=0.3,
        max_tokens=800
    )
    return response.choices[0].message.content

def main():
    print("Azure OpenAI RAG Demo")
    print("---------------------")
    question = "What project arcade?"
    print(f"\nQuestion: {question}")
    print("\nRetrieving information and generating answer...")
    answer = ask_question_with_rag(question)
    print("\nAnswer:")
    print(answer)

if __name__ == "__main__":
    main()
