from .auth_routes import authenticate
from fastapi import APIRouter, Depends, HTTPException
from database.crud import get_employee_by_phone
from services.graph_service import generate_score_graph
from fastapi.responses import StreamingResponse
from services.graph_service import calculate_visa_logic


router = APIRouter()

@router.get("/visa/{phone}/graph")
def visa_score_graph(phone: str, user=Depends(authenticate)):

    employee = get_employee_by_phone(phone)
    if not employee:
        raise HTTPException(status_code=404, detail="Profile not found")
  

    age = employee["age"]
    education_level = employee["education_level"]
    aus_experience = employee["aus_experience"]
    overseas_exp = employee["overseas_exp"]
    marital_status = employee["marital_status"]
    english_test_type = employee["english_test_type"]
    english_test_score = employee["english_test_score"]

    #Calculate score + breakdown
    total_score, score_breakdown = calculate_visa_logic(
        age,
        education_level,
        aus_experience,
        overseas_exp,
        marital_status,
        english_test_type,
        english_test_score
    )

    image = generate_score_graph(score_breakdown)

    return StreamingResponse(image, media_type="image/png")