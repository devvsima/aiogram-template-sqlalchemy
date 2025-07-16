from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from app.routers import admin_router as router
from app.text import message_text as mt


@router.message(Command("admin"), StateFilter(None))
async def _admin_command(message: types.Message) -> None:
    """Админ панель"""
    await message.answer(mt.ADMIN_WELCOME)
