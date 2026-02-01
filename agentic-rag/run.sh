#!/bin/bash

echo "===================================="
echo "Starting Agentic RAG System"
echo "===================================="

# Activate virtualenv
echo "Activating virtual environment..."
source venv/bin/activate


# Start Ollama if not running (safe no-op if already running)
echo "Starting Ollama server..."
ollama serve > /dev/null 2>&1 &


# Start FastAPI backend
echo "Starting FastAPI backend on http://127.0.0.1:8000 ..."
uvicorn app.main:app --host 127.0.0.1 --port 8000 &


# Small delay so backend boots first
sleep 2


# Start Streamlit frontend
echo "Starting Streamlit UI on http://localhost:8501 ..."
streamlit run ui/app.py


echo "System stopped."
