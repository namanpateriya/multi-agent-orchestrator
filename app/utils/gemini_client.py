import os
import time

from dotenv import load_dotenv
import google.generativeai as genai

from app.utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")

MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))


class GeminiClient:

    def __init__(self):

        if not GEMINI_API_KEY:
            logger.error("Missing GEMINI_API_KEY")
            self.model = None
            return

        try:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel(MODEL_NAME)
        except Exception as e:
            logger.error(f"Gemini init failed: {e}")
            self.model = None

    def generate(self, prompt: str):

        if self.model is None:
            return "error: model not initialized"

        for attempt in range(MAX_RETRIES):

            try:
                response = self.model.generate_content(prompt)

                if hasattr(response, "text") and response.text:
                    return response.text.strip()

            except Exception as e:
                logger.error(f"Attempt {attempt+1} failed: {e}")
                time.sleep(1)

        return "error: generation failed"
