from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from .auth_routes import authenticate
import tempfile
import os
import json
from services.cv_service import resume_analyze

router = APIRouter()

@router.post("/analyze-resume")
async def analyze_resume(
    file: UploadFile = File(...),
    user=Depends(authenticate)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
            contents = await file.read()
            temp.write(contents)
            temp_path = temp.name

        ai_response = resume_analyze(temp_path)

        ai_response = ai_response.strip().replace("```json", "").replace("```", "")
        return json.loads(ai_response)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="AI returned invalid JSON")

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)