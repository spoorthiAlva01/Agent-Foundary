import json
import re
from core.planner_schema import PlannerOutput


class PlannerAgent:
    def __init__(self, llm, prompt_path="prompts/planner.txt"):
        self.llm = llm
        with open(prompt_path, "r") as f:
            self.system_prompt = f.read()

    def plan(self, user_input: str) -> PlannerOutput:
        prompt = f"""
{self.system_prompt}

USER REQUEST:
{user_input}
"""

        raw_output = self.llm.generate(prompt)

        try:
            json_text = self._extract_json(raw_output)
            data = json.loads(json_text)
            return PlannerOutput(**data)

        except Exception as e:
            raise RuntimeError(
                "Planner failed to produce valid structured output\n"
                f"Error: {e}\n\n"
                f"Raw LLM output:\n{raw_output}"
            )

    @staticmethod
    def _extract_json(text: str) -> str:
        """
        Extract the first JSON object from LLM output.
        """
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("No JSON object found in LLM output")
        return match.group(0)
