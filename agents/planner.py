import json
from core.planner_schema import PlannerOutput


class PlannerAgent:
    def __init__(self, llm):
        self.llm = llm

    def plan(self, user_input: str) -> PlannerOutput:
        raw_output = self.llm.generate(user_input)

        try:
            data = json.loads(raw_output)
            return PlannerOutput(**data)
        except Exception as e:
            raise RuntimeError(
                f"Planner failed to produce valid output.\nError: {e}\nOutput:\n{raw_output}"
            )
