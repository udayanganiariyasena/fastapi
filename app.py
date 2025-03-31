from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

# FastAPI setup
app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_hr(question: Question):
    answer = (question.question)
    return {"question": question.question, "answer": answer}

