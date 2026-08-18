import os
import shutil
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from schemas.rag_schema import RAGQueryRequest, RAGQueryResponse
from services.rag.chain import generate_rag_response
from services.rag.ingest import ingest_documents, DATA_DIR
from routes.auth_routes import authenticate

router = APIRouter()

@router.post("/ask", response_model=RAGQueryResponse)
async def ask_visa_assistant(payload: RAGQueryRequest, user=Depends(authenticate)):
    try:
        response = generate_rag_response(payload.question)
        return response
    except FileNotFoundError as fnf:
        raise HTTPException(status_code=400, detail=str(fnf))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RAG processing failed: {str(e)}")


@router.post("/upload-doc")
async def upload_visa_document(file: UploadFile = File(...), user=Depends(authenticate)):
    """PDF Upload aur automated Chunking/Ingestion route."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    os.makedirs(DATA_DIR, exist_ok=True)
    file_path = os.path.join(DATA_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process immediately into Vector DB
    ingest_result = ingest_documents(pdf_path=file_path)

    return {
        "message": f"File '{file.filename}' uploaded and indexed successfully.",
        "ingest_details": ingest_result
    }