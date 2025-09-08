from sqlalchemy.ext.asyncio import AsyncSession

from database.services.base import BaseService
from utils.logging import logger

from ..models.user import UserModel


class User(BaseService):
    model = UserModel

    async def get_or_create(
        session: AsyncSession, id: int, username: str = None, language: str = None
    ) -> UserModel:
        if user := await User.get_by_id(session, id):
            return user, False
        await User.create(session, id=id, username=username, language=language)
        user = await User.get_by_id(session, id)
        return user, True

    @staticmethod
    async def increment_referral_count(
        session: AsyncSession, user: UserModel, num: int = 1
    ) -> None:
        """Добавляет приведенного реферала к пользователю {inviter_id}"""
        user.referral += num
        await session.commit()
        logger.log("DATABASE", f"{user.id} (@{user.username}): привел нового пользователя")
