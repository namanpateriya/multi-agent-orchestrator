from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class RiskAgent:

    @staticmethod
    def execute(query: str):

        prompt = f"""
You are a senior program manager.

Identify risks from the context below.

Query:
{query}

Return:
- list of risks
- keep concise
- focus on delivery, timeline, dependencies, stakeholders
"""

        return client.generate(prompt)
