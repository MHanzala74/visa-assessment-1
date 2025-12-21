from fastapi import APIRouter, Depends
from services.visa_logic import calculate_visa_logic
from services.ai_service import generate_ai_explanation
from database.python_to_postgre import insert_data
from pydantic import BaseModel
from auth.auth_flow import get_current_user

class visaassessmentSchema(BaseModel):
    user_id : int
    name : str
    age : int
    education : str
    aus_experience : int
    language : str

router = APIRouter()

@router.post('/visa-assessment')
def visa_assessment(data: visaassessmentSchema,user=Depends(get_current_user)):

    name = data.name
    user_id = data.user_id
    age = data.age
    education = data.education
    aus_experience = data.aus_experience
    language = data.language

    score = calculate_visa_logic(age, education, aus_experience, language)

    if score >= 85:
        visa_code = 189
    elif score >= 70:
        visa_code = 190
    elif score >= 55:
        visa_code = 491
    else:
        visa_code = 482

    explanation = generate_ai_explanation(
        age, education, aus_experience, language, score, visa_code
    )

    insert_data(user_id, name, score, visa_code, explanation)

    return {
        "message": "Assessment completed & saved in database",
        "score": score,
        "visa": visa_code,
        "explanation": explanation
    }
