from langchain.tools import Tool
from app.retrieval.search_pipeline import search


def retrieval_tool():
    """
    Returns ALL relevant chunks combined
    This is critical for good answers
    """

    def retrieve(query: str):
        docs = search(query)

        return "\n\n".join([d.page_content for d in docs])

    return Tool(
        name="document_search",
        func=retrieve,
        description="Read the document properly and understand the query search and return relevant information from uploaded documents",
    )
