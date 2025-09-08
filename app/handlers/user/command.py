from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from app.routers import user_router


@user_router.message(StateFilter(None), Command("command"))
async def _example_command(message: types.Message) -> None:
    """Функционал бота ..."""
    await message.answer("...")
