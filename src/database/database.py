from sqlalchemy.ext.asyncio import(
    create_async_engine, async_sessionmaker,
    AsyncSession

)

from sqlalchemy.orm import DeclarativeBase
from src.config import settings
from fastapi import Depends
from typing import Annotated



engine = create_async_engine(settings.database_url,
                             echo=True,  # Покажет все SQL-запросы в консоли (удобно для тестов)
                             pool_pre_ping=True  # Тот самый "антипротухатель": проверяет соединение перед каждым использованием
                             )

async_new_session = async_sessionmaker(engine,
                                       expire_on_commit=False)


class Model(DeclarativeBase):
    pass

#?тут зачем
import src.models.faq




async def get_db():
    async with async_new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]