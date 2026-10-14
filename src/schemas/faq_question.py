from pydantic import BaseModel


class Answers(BaseModel):
    answer: str


class CreateQuestion(Answers):
    question: str




