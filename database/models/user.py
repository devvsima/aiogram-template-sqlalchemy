from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from utils.logging import logger

from .base import BaseModel


class UserStatus:
    Banned = 0
    User = 1
    Sponsor = 2
    Moderator = 3
    Admin = 4
    Owner = 5


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(70), nullable=True)
    language: Mapped[str] = mapped_column(String(10), server_default="en")
    referral: Mapped[int] = mapped_column(Integer, server_default="0")
    status: Mapped[int] = mapped_column(Integer, server_default="1")

    @staticmethod
    async def get_or_create(
        session: AsyncSession, id: int, username: str = None, language: str = None
    ) -> "User":
        if user := await User.get_by_id(session, id):
            return user, False
        await User.create(session, id=id, username=username, language=language)
        user = await User.get_by_id(session, id)
        return user, True

    @staticmethod
    async def increment_referral_count(session: AsyncSession, user: "User", num: int = 1) -> None:
        """Добавляет приведенного реферала к пользователю {inviter_id}"""
        user.referral += num
        await session.commit()
        logger.log("DATABASE", f"{user.id} (@{user.username}): привел нового пользователя")
