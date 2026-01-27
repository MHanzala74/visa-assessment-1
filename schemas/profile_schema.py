from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class VisaProfile(BaseModel):
    first_name: str = Field(..., example="Ali")
    last_name: str = Field(..., example="Khan")
    email: EmailStr
    phone: str = Field(..., example="03001234567")
    age: int = Field(..., ge=18, le=44)
    nationality: str
    preferred_state: str
    current_occupation: str
    aus_experience: int = Field(..., ge=0)
    overseas_exp: int = Field(..., ge=0)
    education_level: Literal["diploma", "bachelor", "masters", "doctorate"]
    marital_status: Literal[
        "single",
        "partner_pr_or_citizen",
        "partner_skilled",
        "partner_english_only"
    ]
    english_test_type: Literal["ielts", "pte"]
    english_test_score: float