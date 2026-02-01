"""
Search pipeline used by agent tool
"""

from .retriever import get_retriever


def search(query: str):
    retriever = get_retriever()

    docs = retriever.get_relevant_documents(query)

    # debug
    print("\n=== RETRIEVED ===")
    print("count:", len(docs))
    for d in docs:
        print(d.page_content[:200])
    print("===============\n")

    return docs
