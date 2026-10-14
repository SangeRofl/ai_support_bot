from fastapi import APIRouter, HTTPException, status
from src.repository.addquestiontodb import AddQuestionAnswers
from src.database.database import SessionDep
from src.schemas.faq_question import CreateQuestion


router = APIRouter(
    prefix="/faq",
    tags=["faq"],
)

@router.get("/")
async def get_faq(session: SessionDep):
    return await AddQuestionAnswers.get_all_questions(session=session)

@router.post("/v1/", status_code=status.HTTP_201_CREATED)
async def create_faq(
        question: CreateQuestion,
        session: SessionDep
):
    question_post = await AddQuestionAnswers.add(
        question,
        session=session
    )

    return question_post