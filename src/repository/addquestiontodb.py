from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import src.models.faq as faq_models
from src.schemas.faq_question import CreateQuestion, Answers



class AddQuestionAnswers:
    @staticmethod
    async def add(
            data: CreateQuestion, session: AsyncSession
    ):
        new_question = faq_models.FAQ_question(**data.model_dump())
        session.add(new_question)
        await session.commit()
        await session.refresh(new_question)


        return new_question


    @staticmethod
    async def get_questions(id: int, session: AsyncSession):
        query = select(faq_models.FAQ_question).where(faq_models.FAQ_question.id == id)
        result = await session.execute(query)

        answer = result.scalar_one_or_none()


        return answer

    @staticmethod
    async def get_all_questions(session: AsyncSession):
        query = select(faq_models.FAQ_question).order_by(faq_models.FAQ_question.id)
        result = await session.execute(query)
        return result.scalars().all()
