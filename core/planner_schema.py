from typing import List
from pydantic import BaseModel, Field


class Action(BaseModel):
    type: str = Field(..., description="Type of action to perform")
    description: str
    required: bool = True


class PlannerOutput(BaseModel):
    intent: str
    actions: List[Action]
    success_criteria: str
