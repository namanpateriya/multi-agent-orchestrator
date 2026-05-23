from app.utils.gemini_client import GeminiClient

from sentence_transformers import SentenceTransformer
import numpy as np
import fitz  # PyMuPDF

client = GeminiClient()
model = SentenceTransformer("all-MiniLM-L6-v2")


class RAGAgent:

    @staticmethod
    def extract_text(file_path):

        doc = fitz.open(file_path)
        return "\n".join([p.get_text() for p in doc])

    @staticmethod
    def chunk(text, size=500):

        return [text[i:i+size] for i in range(0, len(text), size)]

    @staticmethod
    def embed(texts):

        return model.encode(texts)

    @staticmethod
    def retrieve(query, chunks, embeddings, top_k=3):

        q_emb = model.encode([query])[0]

        scores = [
            np.dot(q_emb, e) / (np.linalg.norm(q_emb)*np.linalg.norm(e))
            for e in embeddings
        ]

        idx = np.argsort(scores)[-top_k:][::-1]

        return [chunks[i] for i in idx]

    @staticmethod
    def execute(query: str, file_path: str = None):

        if not file_path:
            return "No document provided"

        text = RAGAgent.extract_text(file_path)
        chunks = RAGAgent.chunk(text)
        embeddings = RAGAgent.embed(chunks)

        relevant = RAGAgent.retrieve(query, chunks, embeddings)

        context = "\n\n".join(relevant)

        prompt = f"""
You are a program manager.

Use ONLY the context below.

Context:
{context}

Query:
{query}

Return:
- concise summary
"""

        return client.generate(prompt)
