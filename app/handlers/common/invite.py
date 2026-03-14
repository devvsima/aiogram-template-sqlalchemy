from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram.utils.deep_linking import create_start_link
from sqlalchemy.ext.asyncio import AsyncSession

from app.routers import common_router
from app.text import message_text as mt
from core.loader import bot
from database.models.referal import Referal
from database.models.user import User
from utils.base62 import encode_base62


@common_router.message(StateFilter(None), Command("invite"))
async def _invite_link_command(message: types.Message, user: User, session: AsyncSession) -> None:
    """Отправляет персональную реферальную ссылку для приглашения друзей.
    Ссылка создается на основе пользовательского id и кодировки base62"""
    user_code: str = encode_base62(message.from_user.id)
    url = await create_start_link(bot, f"usr_{user_code}")
    invites_count = await Referal.get_invites_count(session, user.id)

    await message.answer(mt.INVITE_FRIENDS.format(invites_count, url))
