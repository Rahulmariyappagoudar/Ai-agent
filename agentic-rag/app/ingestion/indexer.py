"""
Indexes chunks into in-memory Chroma
"""

from app.retrieval.vector_store import get_vector_store


def index_documents(chunks):
    vectordb = get_vector_store()

    vectordb.add_documents(chunks)
