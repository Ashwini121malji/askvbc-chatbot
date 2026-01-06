"""
AskVBC Chatbot - FastAPI Entry Point
"""

from fastapi import FastAPI
from pydantic import BaseModel
from src.orchestrator.intent_router import handle_question

app = FastAPI(title="AskVBC Chatbot")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(payload: QuestionRequest):
    return handle_question(payload.question)
