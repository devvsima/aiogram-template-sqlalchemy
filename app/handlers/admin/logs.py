from aiogram import types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram.types import FSInputFile

from app.routers import admin_router
from app.text import message_text as mt
from data.config import LOG_FILE_PATH


@admin_router.message(StateFilter(None), Command("log"))
@admin_router.message(StateFilter(None), Command("logs"))
async def _logs_command(message: types.Message) -> None:
    """Отправляет администратору последний файл логов бота"""
    await message.answer(mt.LOG_SENDING)
    await message.answer_document(document=FSInputFile(LOG_FILE_PATH))
