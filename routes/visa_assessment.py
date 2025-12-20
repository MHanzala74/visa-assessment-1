from fastapi import APIRouter
from services.visa_logic import calculate_visa_logic
from services.ai_service import generate_ai_explanation
from database.python_to_postgre import insert_data

router = APIRouter()

@router.post('/visa-assessment')
def visa_assessment(data: dict):

    name = data.get('name')
    user_id = data.get('user_id')
    age = data.get('age')
    education = data.get('education')
    aus_experience = data.get('aus_experience')
    language = data.get('language')

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
