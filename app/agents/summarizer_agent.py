from app.utils.gemini_client import GeminiClient

client = GeminiClient()


class SummarizerAgent:

    @staticmethod
    def execute(structured_data):

        prompt = f"""
You are a senior program manager preparing an executive update.

Combine the following inputs into a structured response:

Summary:
{structured_data.get("summary", "")}

Risks:
{structured_data.get("risks", "")}

Actions:
{structured_data.get("actions", "")}

Output format:

Summary:
<concise summary>

Key Risks:
- ...

Recommended Actions:
- ...
"""

        return client.generate(prompt)
