from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class ActionAgent:

    @staticmethod
    def execute(query: str):

        prompt = f"""
You are a program manager.

Based on the situation below, suggest next steps.

Query:
{query}

Return:
- clear action items
- practical and concise
"""

        return client.generate(prompt)
