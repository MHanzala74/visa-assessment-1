from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router as auth_router
from routes.visa_routes import router as visa_router
from routes.profile_routes import router as profile_router
from routes.graph_routes import router as graph_router
from routes.cv_routes import router as cv_router
from routes.rag_routes import router as rag_router
import matplotlib
matplotlib.use("Agg")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(visa_router)
app.include_router(profile_router)
app.include_router(graph_router)
app.include_router(cv_router)
app.include_router(rag_router)

@app.get("/health")
def home():
    return {"message":"Visa assessment backend running"}