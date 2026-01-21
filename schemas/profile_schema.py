from pydantic import BaseModel

class VisaProfile(BaseModel):
    first_name : str
    last_name : str
    email : str
    phone : str
    age : int
    nationality : str
    preferred_state: str
    current_occupation: str
    aus_experience: int
    overseas_exp : int
    education_level: str
    marital_status: str
    language: str