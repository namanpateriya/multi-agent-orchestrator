from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class RAGAgent:

    @staticmethod
    def execute(query: str, file_path: str = None):

        # Step 2 simplification: no real RAG yet (kept stable)
        # We simulate document-based reasoning

        prompt = f"""
You are a program management assistant.

Summarize the project update and extract key points.

Query:
{query}

Provide:
- summary
- key highlights
"""

        return client.generate(prompt)
