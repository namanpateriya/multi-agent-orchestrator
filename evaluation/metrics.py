import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(a: str, b: str):

    emb = model.encode([a, b])

    return float(
        np.dot(emb[0], emb[1]) /
        (np.linalg.norm(emb[0]) * np.linalg.norm(emb[1]))
    )


def list_coverage(output: str, expected_keywords: list):

    output = output.lower()

    matches = sum(
        1 for k in expected_keywords
        if k.lower() in output
    )

    return matches / len(expected_keywords) if expected_keywords else 0
