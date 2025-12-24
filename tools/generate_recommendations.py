from tools.base_tool import BaseTool

class GenerateRecommendations(BaseTool):
    name = "generate_recommendations"
    required_inputs = ["analyze_data"]

    def execute(self, analyze_data):
        if not analyze_data:
            return ["No action needed"]

        return [
            "Improve creatives to increase CTR",
            "Reallocate budget to better segments"
        ]
