import os
import requests


class OpenRouterLLM:
    def __init__(self, model="meta-llama/llama-3.1-8b-instruct"):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENROUTER_API_KEY not set")

        self.model = model
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"

        print(f"🟢 OpenRouterLLM using model: {self.model}")

    def generate(self, prompt: str) -> str:
        response = requests.post(
            self.endpoint,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                # Optional but recommended by OpenRouter
                "HTTP-Referer": "http://localhost",
                "X-Title": "Agent-Foundary"
            },
            json={
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a Planner Agent.\n"
                            "You MUST return ONLY valid JSON.\n"
                            "Do NOT include explanations, markdown, or extra text."
                        )
                    },
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.0
            },
            timeout=60
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"OpenRouter API error {response.status_code}: {response.text}"
            )

        data = response.json()

        return data["choices"][0]["message"]["content"]
