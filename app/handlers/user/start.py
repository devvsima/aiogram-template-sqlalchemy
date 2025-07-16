from aiogram import types
from aiogram.filters import CommandStart
from aiogram.filters.state import StateFilter

from app.routers import start_router
from app.text import message_text as mt


@start_router.message(CommandStart(), StateFilter(None))
async def _start_command(message: types.Message) -> None:
    text = mt.WELCOME.format(
        message.from_user.id,
        message.from_user.full_name,
    )
    await message.answer(text)
