"""
Unified document loader
Supports pdf, txt, docx, pptx, xlsx
"""

import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
    UnstructuredExcelLoader,
)


def load_documents(file_path: str):
    """
    Loads file and returns LangChain documents
    """

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)

    elif ext == ".txt":
        loader = TextLoader(file_path)

    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)

    elif ext == ".pptx":
        loader = UnstructuredPowerPointLoader(file_path)

    elif ext == ".xlsx":
        loader = UnstructuredExcelLoader(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return loader.load()
