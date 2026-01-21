from .auth_routes import authenticate
from fastapi import APIRouter, Depends, HTTPException
from database.crud import get_employee_by_phone
from services.graph_service import generate_score_graph
from fastapi.responses import StreamingResponse


router = APIRouter()

@router.get("/visa/{phone}/graph")
def visa_score_graph(phone: str, user=Depends(authenticate)):

    employee = get_employee_by_phone(phone)
    if not employee:
        raise HTTPException(status_code=404, detail="Profile not found")

    score_breakdown = {
        "Age": 25,
        "Education": 20,
        "Aus Experience": 10,
        "Overseas Experience": 10,
        "Language": 15,
        "Marital Status": 5
    }

    image = generate_score_graph(score_breakdown)

    return StreamingResponse(image, media_type="image/png")