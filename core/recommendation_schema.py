from pydantic import BaseModel
from typing import List


class Recommendation(BaseModel):
    recommendation: str
    reason: str
    confidence: float


class RecommendationOutput(BaseModel):
    recommendations: List[Recommendation]
