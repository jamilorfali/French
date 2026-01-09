"""
CEFR Level schemas for API validation.
"""
from pydantic import BaseModel
from typing import Optional


class CEFRLevelResponse(BaseModel):
    """Schema for CEFR level response."""
    id: int
    code: str
    name: str
    description: Optional[str] = None
    order: int
    af_levels: Optional[str] = None
    vocabulary_target: int

    class Config:
        from_attributes = True
