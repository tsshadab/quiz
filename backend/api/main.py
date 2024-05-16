import os
import sys
# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routers.v1 import quiz
from backend.database.db_operations import init_db


app = FastAPI(debug=True, docs_url="/quiz/api/docs", openapi_url="/quiz/api/openapi.json")
router = APIRouter(prefix="/quiz/api")

# Add CORS middleware
origins = [
    "http://127.0.0.1:8090",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz.quiz_router, tags=["Quiz"])

@app.on_event("startup")
async def startup_event():
    init_db()
    
