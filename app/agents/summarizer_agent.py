from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class SummarizerAgent:

    @staticmethod
    def execute(data):

        prompt = f"""
You are a senior program manager.

STRICT RULES:
- Use ONLY provided inputs
- Do NOT add new info
- If missing, say "Not available"

Summary:
{data.get("summary", "")}

Risks:
{data.get("risks", "")}

Actions:
{data.get("actions", "")}

Output:

Summary:
...

Key Risks:
...

Recommended Actions:
...
"""

        return client.generate(prompt)
