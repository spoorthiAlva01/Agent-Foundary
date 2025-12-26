from core.critic_schema import CriticResult, CriticFeedback


class CriticAgent:
    def evaluate(self, recommendations) -> CriticResult:
        feedback = []

        for r in recommendations.recommendations:
            verdict = "accept"
            confidence = r.confidence
            reason = "Recommendation is clear and actionable."

            if confidence < 0.5:
                verdict = "revise"
                reason = "Low confidence; needs stronger justification."

            if not r.recommendation or len(r.recommendation) < 10:
                verdict = "reject"
                confidence = 0.2
                reason = "Recommendation is too vague."

            feedback.append(
                CriticFeedback(
                    recommendation=r.recommendation,
                    verdict=verdict,
                    reason=reason,
                    confidence=confidence
                )
            )

        return CriticResult(feedback=feedback)
