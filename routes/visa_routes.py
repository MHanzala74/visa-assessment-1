from fastapi import APIRouter, Depends, HTTPException
from .auth_routes import authenticate
from services.visa_service import calculate_visa_logic
from services.ai_explanation_service import generate_ai_explanation
from database.crud import get_employee_by_phone, insert_data, create_table_if_not_exists


router = APIRouter()

@router.get("/visa/{phone}")
def visa_assessment(phone: str, user=Depends(authenticate)):

    employee = get_employee_by_phone(phone)

    if not employee:
        raise HTTPException(status_code=404, detail="Profile not found")

    first_name = employee["first_name"]
    last_name = employee["last_name"]
    age = employee["age"]
    education_level = employee["education_level"].strip().lower()
    aus_experience = employee["aus_experience"]
    overseas_exp = employee["overseas_exp"]
    marital_status = employee["marital_status"].strip().lower()
    english_test_type = employee["english_test_type"].strip().lower()
    english_test_score = employee["english_test_score"]

    user_name = f"{first_name} {last_name}"

    score = calculate_visa_logic(age=age, education_level=education_level, aus_experience=aus_experience,overseas_exp=overseas_exp, marital_status=marital_status,english_test_type=english_test_type,english_test_score=english_test_score)

    if score >= 85:
        subclass = 189
    elif score >= 70:
        subclass = 190
    elif score >= 55:
        subclass = 491
    else:
        subclass = 482

    explanation = generate_ai_explanation(
        age, education_level, aus_experience, english_test_score, score, subclass
    )

    create_table_if_not_exists()
    insert_data(user_name,score,subclass)

    return {
        "message": "Assessment fetched from database",
        "candidate": {
            "first_name": employee["first_name"],
            "last_name": employee["last_name"],
            "phone": employee["phone"]
        },
        "score": score,
        "visa": subclass,
        "explanation": explanation
    }