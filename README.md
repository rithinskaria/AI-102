# AI-102: Designing and Implementing an Azure AI Solution

This repository contains hands-on code samples, datasets, and demo projects designed to support learning and exam preparation for **AI-102: Designing and Implementing an Azure AI Solution** certification.

Each module aligns with the core topics of the AI-102 exam, featuring practical implementations of Azure Cognitive Services and Azure Machine Learning components.

---

## 📁 Project Structure

### 🔹 Azure Open AI
- Simple app using Azure OpenAI for prompt completion and text generation.
- `templates/`, `app.py`, and `requirements.txt` provided for quick deployment.

### 🔹 Conversational Language Understanding (CLU)
- Demo project using CLU to understand user intents and extract entities.
- Includes a JSON file (`pizza_clu_sample_utterances.json`) with training utterances.

### 🔹 Custom NER (Named Entity Recognition)
- Custom NER implementation using labeled `.txt` samples from `financial_entities_txt`.
- Useful for training Azure Language Studio to recognize financial terms like stock tickers, forex, and cryptocurrencies.

### 🔹 Custom QnA
- Question Answering app using custom knowledge bases.
- Built to integrate with Azure Language Services.

### 🔹 Custom Skill Set (Azure AI Search)
- Demonstrates how to create a custom skillset using:
  - `index.json`, `indexer.json`, `skillset.json`
  - Example files: `employee-report.txt`, `project-plan.txt`, `meeting-minutes.txt`

### 🔹 Custom Text Classification
- Uses `training_data_custom` to train a classification model in Azure Language Studio.
- Classifies documents into predefined categories.

### 🔹 Document Intelligence
- Analyze US Green Card documents (`id1.jpeg`, `id2.jpg`) using Azure Document Intelligence.
- `app.py` implements document analysis and field extraction.

### 🔹 Enrichment Pipeline
- Azure Cognitive Search pipeline example to extract structured data from resumes.
- Includes PDF files and complete `index.json`, `indexer.json`, and `skillset.json`.

### 🔹 Face Detection using Face API
- Detect faces from images using Azure Face Service.
- `app_face_detection.py` for the Face API demo.

### 🔹 Image Analysis using Azure Vision
- Analyze images for objects, OCR, and tags using:
  - `app_image_analysis.py`
  - `app_ocr.py`

### 🔹 Language Services Demos
- Scripts showcasing various Azure Language services:
  - `app_entity_linking.py`
  - `app_key_phrase_extraction.py`
  - `app_lang_detection.py`
  - `app_ner.py`
  - `app_pii_detection.py`
  - `app_sentiment_analysis.py`
  - `app_summarization.py`

### 🔹 RAG (Retrieval-Augmented Generation)
- Example app for combining Azure OpenAI with Azure AI Search.
- PDF `Project_Orion_Confidential.pdf` used for RAG implementation.

### 🔹 Speech Services
- Text-to-speech (`app_tts.py`)
- Speech-to-text (`app_stt.py`)
- Translation (`app_translate.py`)
- SSML custom voices (`app_ssml.py`)
- Output file: `output_audio.wav`

### 🔹 Translation Services
- Translate text using Azure Translation API.

---

