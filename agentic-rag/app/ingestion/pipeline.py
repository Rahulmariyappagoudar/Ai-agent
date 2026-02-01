"""
Complete ingestion pipeline

Flow:
load → clean → chunk → metadata → index
Supports:
- single file
- directory of files
"""

import os

from .loader import load_documents
from .cleaner import clean_text
from .chunker import chunk_documents
from .indexer import index_documents


# =========================
# Single file ingestion
# =========================
def ingest_file(file_path: str):

    docs = load_documents(file_path)

    # clean
    for doc in docs:
        doc.page_content = clean_text(doc.page_content)

    # chunk
    chunks = chunk_documents(docs)

    # metadata
    for i, chunk in enumerate(chunks):
        chunk.metadata["source_file"] = os.path.basename(file_path)
        chunk.metadata["chunk_id"] = i

    # index
    index_documents(chunks)


# =========================
# Directory ingestion
# =========================
def ingest_directory(folder_path: str):
    """
    Ingest all supported files inside a folder
    """

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            ingest_file(full_path)
