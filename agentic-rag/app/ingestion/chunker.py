"""
Smart chunking strategy

Reasoning:
- resumes/docs are paragraph heavy
- bigger chunks preserve meaning
- overlap keeps context continuity
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    return splitter.split_documents(docs)
