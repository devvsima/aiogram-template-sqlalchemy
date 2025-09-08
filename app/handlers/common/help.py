from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from app.routers import common_router
from app.text import message_text as mt


@common_router.message(StateFilter(None), Command("help"))
async def _help_command(message: types.Message) -> None:
    """Дает дополнительную информацию про бота"""
    await message.answer(mt.INFO)
