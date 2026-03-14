from sqlalchemy import ForeignKey, Integer, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Referal(BaseModel):
    __tablename__ = "referals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    inviter_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    code: Mapped[str] = mapped_column(String(10), nullable=True, server_default="usr")
    source: Mapped[str] = mapped_column(String(100), nullable=True, server_default="Telegram user")

    @staticmethod
    async def get_invites_count(session: AsyncSession, inviter_id: int) -> int:
        """Получает количество людей, которых пригласил пользователь"""
        query = select(func.count(Referal.id)).where(Referal.inviter_id == inviter_id)
        result = await session.execute(query)
        count = result.scalar()
        return count or 0
