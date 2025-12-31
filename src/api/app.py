from fastapi import FastAPI
from pydantic import BaseModel
from src.orchestrator.intent_router import handle_question
import uuid

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def health():
    return {"status": "AskVBC is running"}

@app.post("/ask")
def ask(req: QuestionRequest):
    trace_id = str(uuid.uuid4())
    return handle_question(req.question, trace_id)
