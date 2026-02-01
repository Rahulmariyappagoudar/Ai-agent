"""
In-memory Chroma (no SQLite, no files, no permission issues)
"""

from langchain_community.vectorstores import Chroma
from app.ingestion.embedder import get_embeddings

_vectordb = None  # global singleton


def get_vector_store():
    global _vectordb

    if _vectordb is None:
        embeddings = get_embeddings()

        # 🔥 NO persist_directory
        _vectordb = Chroma(
            embedding_function=embeddings
        )

    return _vectordb
