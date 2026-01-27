from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.visa_routes import router as visa_router
from routes.profile_routes import router as profile_router
from routes.graph_routes import router as graph_router
from routes.cv_routes import router as cv_router
import matplotlib
matplotlib.use("Agg")
app = FastAPI()

app.include_router(auth_router)
app.include_router(visa_router)
app.include_router(profile_router)
app.include_router(graph_router)
app.include_router(cv_router)

@app.get("/health")
def home():
    return {"message":"Visa assessment backend running"}