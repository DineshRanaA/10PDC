
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException

from questions import questions

app = FastAPI(
    title="Quiz Application API",
    description="Backend API for Quiz Application",
    version="1.0.0"
)

class AnswerSubmission(BaseModel):
    question_id: int
    answer: str


class QuizSubmission(BaseModel):
    answers: List[AnswerSubmission]

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Quiz Application API",
        "status": "success"
    }


# Health check API
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# Get all quiz questions
@app.get("/questions")
def get_questions():

    quiz_questions = []

    for question in questions:

        quiz_questions.append({
            "id": question["id"],
            "question": question["question"],
            "options": question["options"]
        })

    return {
        "total_questions": len(quiz_questions),
        "questions": quiz_questions
    }


# Get a single question by ID
@app.get("/questions/{question_id}")
def get_question(question_id: int):

    for question in questions:

        if question["id"] == question_id:

            return {
                "id": question["id"],
                "question": question["question"],
                "options": question["options"]
            }

    raise HTTPException(
        status_code=404,
        detail="Question not found"
    )

@app.post("/submit")
def submit_quiz(submission: QuizSubmission):

    score = 0
    results = []

    for submitted_answer in submission.answers:

        question_id = submitted_answer.question_id
        selected_answer = submitted_answer.answer.upper()

        question = next(
            (q for q in questions if q["id"] == question_id),
            None
        )

        if question is None:
            raise HTTPException(
                status_code=404,
                detail=f"Question {question_id} not found"
            )

        is_correct = selected_answer == question["correct_answer"]

        if is_correct:
            score += 1

        results.append({
            "question_id": question_id,
            "selected_answer": selected_answer,
            "correct_answer": question["correct_answer"],
            "is_correct": is_correct
        })

    return {
        "total_questions": len(submission.answers),
        "correct_answers": score,
        "wrong_answers": len(submission.answers) - score,
        "score": score,
        "results": results
    }
