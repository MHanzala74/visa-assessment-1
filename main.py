from fastapi import FastAPI
from routes.visa_assessment import router as visa_router
from routes.login import router as login_router
from routes.register import router as register_router

app = FastAPI()

app.include_router(visa_router)
app.include_router(login_router)
app.include_router(register_router)

@app.get("/")
def home():
    return {"message":"Visa assessment backend running"}