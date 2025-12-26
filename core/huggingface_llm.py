import os
from huggingface_hub import InferenceClient


class HuggingFaceLLM:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.2"):
        api_key = os.getenv("HUGGINGFACE_API_KEY")
        if not api_key:
            raise RuntimeError("HUGGINGFACE_API_KEY not set")

        self.model_name = model_name
        self.client = InferenceClient(
            model=model_name,
            token=api_key,
            provider="hf-inference"  # 🔑 THIS LINE FIXES EVERYTHING
        )

        print(f"🤗 HuggingFaceLLM using model: {self.model_name}")

    def generate(self, prompt: str) -> str:
        response = self.client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Planner Agent.\n"
                        "You MUST output ONLY valid JSON.\n"
                        "Do NOT include explanations or markdown."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.0
        )

        if not response or not response.choices:
            raise RuntimeError("Empty response from Hugging Face")

        return response.choices[0].message.content
