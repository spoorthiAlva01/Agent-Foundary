from pydantic import BaseModel
from typing import List


class CriticFeedback(BaseModel):
    recommendation: str
    verdict: str           # "accept" | "revise" | "reject"
    reason: str
    confidence: float      # 0.0 - 1.0


class CriticResult(BaseModel):
    feedback: List[CriticFeedback]
