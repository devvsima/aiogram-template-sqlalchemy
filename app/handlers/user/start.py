from aiogram import types
from aiogram.filters import CommandStart
from aiogram.filters.state import StateFilter

from app.handlers.msg_text import msg_text
from app.routers import start_router


@start_router.message(CommandStart(), StateFilter(None))
async def _start_command(message: types.Message) -> None:
    await message.answer(msg_text.WELCOME.format(message.from_user.id, message.from_user.full_name))
