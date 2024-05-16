from pydantic import BaseModel
from typing import List, Dict

class Option(BaseModel):
    option_key: str
    option_text: str

class Question(BaseModel):
    id: int
    question: str
    options: List[Option]
    answerKey: str

class Answer(BaseModel):
    question_id: int
    selected_option: str

class QuizAnswer(BaseModel):
    answers: List[Answer]