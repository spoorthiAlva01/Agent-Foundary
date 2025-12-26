from google import genai
from google.genai import types
import os


class GeminiLLM:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY not set")

        self.model_name = "gemini-2.0-flash-lite"
       

        self.client = genai.Client(api_key=api_key)

        print(f"🔥 GeminiLLM using model: {self.model_name}")

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.0
            )
        )

        if not response.text:
            raise RuntimeError("Empty response from Gemini")

        return response.text
