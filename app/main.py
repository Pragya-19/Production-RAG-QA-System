from fastapi import FastAPI
from pydantic import BaseModel

from generation.answer import answer_question


app = FastAPI(
    title="Production RAG QA System",
    description="Hybrid RAG system with citations for AI-QA use cases",
    version="0.1.0",
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Production RAG QA System is running"
    }


@app.post("/ask")
def ask(request: QuestionRequest):
    return answer_question(request.question)