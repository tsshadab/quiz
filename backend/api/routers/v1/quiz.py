from fastapi import APIRouter, HTTPException
from models.quiz_model import QuizAnswer
from database.db_operations import get_quiz_data, evaluate_quiz, init_db

quiz_router = APIRouter(prefix="/quiz/api", tags=["Quiz"])

@quiz_router.get("/questions", summary="Get quiz questions")
async def get_quiz():
    return get_quiz_data()

@quiz_router.post("/submit", summary="Submit quiz answers")
async def submit_quiz(answers: QuizAnswer):
    try:
        answers_dict = {answer.question_id: answer.selected_option for answer in answers.answers}
        score, results = evaluate_quiz(answers_dict)
        return {
            "score": score,
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@quiz_router.post("/restart", summary="Restart the quiz session")
async def restart_quiz():
    try:
        init_db()  # Initialize the database to restart the quiz
        return {"message": "Quiz session restarted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))