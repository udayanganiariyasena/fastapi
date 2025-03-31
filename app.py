from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore


app = FastAPI()

class Question(BaseModel):
    question: str


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/ask")
async def ask_hr(question: Question):
    answer = (question.question)
    return {"question": question.question, "answer": answer}

