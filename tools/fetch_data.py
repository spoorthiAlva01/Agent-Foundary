from tools.base_tool import BaseTool

class FetchData(BaseTool):
    name = "fetch_data"
    required_inputs = []

    def execute(self):
        return {
            "ctr": 0.65,
            "cpc": 15.1,
            "roas": 1.2
        }
