from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from utils.logging import logger

from ..models.users import UserModel


async def get_user(session: AsyncSession, user_id: int) -> UserModel | None:
    """Возвращает пользователя по его id"""
    result = await session.execute(select(UserModel).where(UserModel.id == user_id))
    return result.scalars().first()


async def get_or_create_user(
    session: AsyncSession, user_id: int, username: str = None, language: str = None
) -> UserModel:
    """Возвращает пользователя по его id, если его нет - создает"""
    if user := await get_user(session, user_id):
        return user

    return await create_user(session, user_id, username, language)


async def create_user(
    session: AsyncSession, user_id: int, username: str = None, language: str = None
) -> UserModel:
    """Создает нового пользователя"""
    logger.info(f"New user: {user_id} | {username}")
    user = UserModel(id=user_id, username=username, language=language)
    session.add(user)
    await session.commit()
    return user


async def update_user_username(session: AsyncSession, user_id: int, username: str = None) -> None:
    """Обновляет данные пользователя"""
    await session.execute(
        update(UserModel).where(UserModel.id == user_id).values(username=username)
    )
    await session.commit()
    logger.info(f"Update user: {user_id} | {username}")


async def new_referral(session: AsyncSession, inviter_id: int) -> None:
    """Добавляет приведенного реферала к пользователю inviter_id"""
    await session.execute(
        update(UserModel).where(UserModel.id == inviter_id).values(referral=UserModel.referral + 1)
    )
    await session.commit()
    logger.info(f"UserModel: {inviter_id} | привел нового пользователя")


async def change_language(session: AsyncSession, user_id: int, language: str) -> None:
    """Изменяет язык пользователя на language"""
    await session.execute(
        update(UserModel).where(UserModel.id == user_id).values(language=language)
    )
    await session.commit()
    logger.info(f"UserModel: {user_id} | изменил язык на - {language}")


async def ban_or_unban_user(session: AsyncSession, user_id: int, is_banned: bool) -> None:
    """Меняет статус блокировки пользователя на заданный"""
    await session.execute(
        update(UserModel).where(UserModel.id == user_id).values(is_banned=is_banned)
    )
    await session.commit()
    logger.info(f"UserModel: {user_id} | статус блокировки изменен на - {is_banned}")
