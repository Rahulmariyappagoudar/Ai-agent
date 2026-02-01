"""
Retriever with tuned k
"""

from app.retrieval.vector_store import get_vector_store


def get_retriever():
    vectordb = get_vector_store()

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 6} 
    )

    return retriever
