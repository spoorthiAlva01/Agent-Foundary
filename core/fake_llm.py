class FakeLLM:
    def generate(self, prompt: str) -> str:
        print("🔥🔥🔥 FakeLLM CALLED 🔥🔥🔥")

        # Extract user request only
        user_input = prompt.split("USER REQUEST:")[-1].strip().lower()


        if "analyze" in user_input or "campaign" in user_input:
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
        return """
        {
          "intent": "unknown_request",
          "actions": [],
          "success_criteria": "User intent could not be determined"
        }
        """
