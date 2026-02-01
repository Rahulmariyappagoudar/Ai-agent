# Agentic RAG

A lightweight Agentic Retrieval-Augmented Generation (RAG) system that answers questions from your uploaded documents.

Tech stack:
- FastAPI (backend API)
- Streamlit (UI)
- LangChain (agent + tools)
- Chroma (vector database)
- Ollama (local LLM)

---

## Features

- Upload File
- Automatic chunk → embed → index
- Semantic search using embeddings
- Answers
- Fully local

---

## Project Structure

agentic-rag/

app/
  agents/      → agent logic and tools  
  api/         → FastAPI routes and schemas  
  ingestion/   → document processing pipeline  
  retrieval/   → retriever + vector store  

ui/            → Streamlit frontend  
data/raw_docs/ → uploaded files  
run.sh         → start services  

---

## Setup Instructions

### 1. Clone repository

git clone <repo-url>  
cd agentic-rag  

---

### 2. Create virtual environment

Mac/Linux:

python -m venv venv  
source venv/bin/activate  

Windows:

python -m venv venv  
venv\Scripts\activate  

---

### 3. Install dependencies

pip install -r requirements.txt  

---

### 4. Start local LLM (required)

Make sure Ollama is installed and running.

Example:

ollama run mistral

### 5. Run the application

bash run.sh  

This starts:
- FastAPI backend
- Streamlit UI

Open the URL shown in terminal.

---

## Usage

### Upload documents
Upload files from the UI.  
They are automatically chunked, embedded, and indexed.

### Ask questions
Ask questions about your documents.  
The system retrieves relevant chunks and generates answers using the LLM.

Example:

"What skills are mentioned in my resume?"


## How It Works

Upload flow:
file → chunk → embed → vector store  

Query flow:
question → retrieve chunks → LLM → answer  

Vector DB stores knowledge.  
Retriever finds context.  
LLM generates the response.

---

## Notes

- Works offline with local models
- Simple modular design.
