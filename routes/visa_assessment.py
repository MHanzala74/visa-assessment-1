from fastapi import APIRouter
from services.visa_logic import calculate_visa_logic
from services.ai_service import generate_ai_explanation
from services.save_assessment import save_visa_assessment

router = APIRouter()

@router.post('/visa-assessment')
def visa_assessment(data:dict):
    user_id = data.get('user_id')
    age = data.get('age')
    education = data.get('education')
    aus_experience = data.get('aus_experience')
    language = data.get('language')

    score = calculate_visa_logic(age,education,aus_experience,language)

    """Recommend Australian visa based on points score"""
    if score >= 85:
        visa_code = "189"
        # visa = {
        #     "visa_code": "189",
        #     "visa_name": "Skilled Independent Visa",
        #     "english_explanation": "Your score is 85+ points - you are eligible for direct permanent residency",
        #     "minimum_score": 65
        # }
    elif score >= 70:
        visa_code = "190"
        # visa = {
        #     "visa_code": "190",
        #     "visa_name": "Skilled Nominated Visa",
        #     "english_explanation": "Your score is 70-84 points - state nomination can give you additional points",
        #     "minimum_score": 65
        # }
    elif score >= 55:
        visa_code = "491"
        # visa = {
        #     "visa_code": "491",
        #     "visa_name": "Skilled Work Regional Visa",
        #     "english_explanation": "Your score is 55-69 points - more opportunities available in regional areas",
        #     "minimum_score": 65
        # }
    else:
        visa_code = "482"
        # visa = {
        #     "visa_code": "482",
        #     "visa_name": "Temporary Skill Shortage Visa",
        #     "english_explanation": "Points are low - start with temporary visa, shift to permanent later",
        #     "minimum_score": "Employer sponsorship required"
        # }
  

    explanation = generate_ai_explanation(age,education,aus_experience,language,score,visa_code)

    save_visa_assessment(user_id,score,visa_code,explanation)

    return {
        "message" : "Assessment completed & save in database",
        "Score" : score,
        "Recommend Visa" : visa_code,
        "AI Explanation" : explanation
    }
