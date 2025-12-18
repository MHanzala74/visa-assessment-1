from fastapi import FastAPI
from routes.visa_assessment import router as visa_router

app = FastAPI()

app.include_router(visa_router)

@app.get("/")
def home():
    return {"message":"Visa assessment backend running"}