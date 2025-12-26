class FakeLLM:
    def generate(self, prompt: str) -> str:
        return """
        {
          "intent": "optimize_campaign_performance",
          "actions": [
            {
              "type": "fetch_data",
              "description": "Fetch campaign performance metrics",
              "required": true
            },
            {
              "type": "analyze_data",
              "description": "Analyze campaign performance metrics",
              "required": true
            }
          ],
          "success_criteria": "Clear insights generated for optimization"
        }
        """
