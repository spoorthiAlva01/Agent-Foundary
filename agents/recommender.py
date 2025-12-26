from core.recommendation_schema import RecommendationOutput, Recommendation


class RecommendationAgent:
    def __init__(self, llm):
        self.llm = llm  # kept for future real LLMs

    def recommend(self, execution_result) -> RecommendationOutput:
        insights = []
        metrics = {}

        # Extract data from executor output
        for step in execution_result:
            if "fetch_data" in step:
                metrics = step["fetch_data"]
            if "analyze_data" in step:
                insights = step["analyze_data"]

        recommendations = []

        # Deterministic reasoning (this is GOOD)
        if "Low CTR" in insights:
            recommendations.append(
                Recommendation(
                    recommendation="Improve ad creatives and messaging",
                    reason="Low CTR indicates ads are not resonating with the audience",
                    confidence=0.8
                )
            )

        if "Low ROAS" in insights:
            recommendations.append(
                Recommendation(
                    recommendation="Reallocate budget to higher-performing segments",
                    reason="Low ROAS suggests inefficient spend allocation",
                    confidence=0.75
                )
            )

        if not recommendations:
            recommendations.append(
                Recommendation(
                    recommendation="Maintain current strategy with minor optimizations",
                    reason="No major performance issues detected",
                    confidence=0.6
                )
            )

        return RecommendationOutput(recommendations=recommendations)
