from fastapi import APIRouter, Depends
from .model import visaSchema
from auth.routes import authenticate
from .calculate_visa_score import calculate_visa_logic
from .visa_explanation import generate_ai_explanation
from .insert_database import insert_data

router = APIRouter()

@router.post('/visa')
def visa_assessment(req:visaSchema,user=Depends(authenticate)):
    name = req.name
    age = req.age
    education = req.education
    aus_experience = req.aus_experience
    language = req.language

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

    insert_data(name, score, visa_code, explanation)

    return {
        "message": "Assessment completed & saved in database",
        "score": score,
        "visa": visa_code,
        "explanation": explanation
    }
