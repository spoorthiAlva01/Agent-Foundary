from tools.base_tool import BaseTool

class AnalyzeData(BaseTool):
    name = "analyze_data"
    required_inputs = ["fetch_data"]

    def execute(self, fetch_data):
        insights = []
        if fetch_data["ctr"] < 0.8:
            insights.append("Low CTR")
        if fetch_data["roas"] < 1.5:
            insights.append("Low ROAS")
        return insights
