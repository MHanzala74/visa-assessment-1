from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class RAGQueryRequest(BaseModel):
    question: str = Field(..., example="What are the eligibility requirements for Canada Student Visa?")
    target_country: Optional[str] = Field(None, example="Canada")

class RAGQueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[Dict[str, Any]]