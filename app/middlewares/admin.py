from typing import Any, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from data.config import tgbot
from database.services.user import User

ADMINS_ID = tgbot.ADMINS


class AdminMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, message: Message, data: dict) -> Any:
        session = data["session"]
        if user := await User.get_by_id(session, message.from_user.id):
            if user.id in ADMINS_ID:
                data["user"] = user
                return await handler(message, data)
        return
