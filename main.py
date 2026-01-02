from fastapi import FastAPI
from auth.routes import router as auth_router
from visa_assessments.routes import router as visa_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(visa_router)

@app.get("/health")
def home():
    return {"message":"Visa assessment backend running"}

