from datetime import datetime
from sqlalchemy import func
from src.database.database import Model
from sqlalchemy.orm import Mapped, mapped_column


class FAQ_question(Model):
    __tablename__ = 'faq'

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column()
    answer: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=None
    )


