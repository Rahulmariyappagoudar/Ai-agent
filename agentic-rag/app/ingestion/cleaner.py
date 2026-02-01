"""
Text cleaning / normalization
Improves embedding quality significantly
"""

import re


def clean_text(text: str) -> str:
    """
    Normalize text before embedding

    Why?
    - removes weird whitespace
    - removes extra newlines
    - makes embeddings more semantic
    """

    text = re.sub(r"\s+", " ", text)   # collapse whitespace
    text = text.replace("\n", " ")
    text = text.strip()

    return text
