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
      "description": "Analyze campaign metrics",
      "required": true
    },
    {
      "type": "generate_recommendations",
      "description": "Generate optimization suggestions",
      "required": true
    }
  ],
  "success_criteria": "Clear optimization recommendations produced"
}
"""
