from pydantic import BaseModel

class visaSchema(BaseModel):
    name: str
    age: int
    education: str
    aus_experience: int
    language: str