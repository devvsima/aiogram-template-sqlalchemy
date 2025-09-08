from aiogram import F, types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from app.keyboards.inline.lang import lang_ikb
from app.routers import common_router
from app.text import message_text as mt
from database.models import UserModel
from database.services import User


@common_router.message(StateFilter(None), Command("language"))
@common_router.message(StateFilter(None), Command("lang"))
async def _lang(message: types.Message) -> None:
    """Предлагает клавиатуру с доступными языками"""
    await message.answer(mt.CHANGE_LANG, reply_markup=lang_ikb())


@common_router.callback_query(F.data.in_(("ru", "uk", "en")))
async def _lang_change(callback: types.CallbackQuery, user: UserModel, session) -> None:
    """Меняет язык пользователя на выбранный"""
    await User.update_language(session, user=user, language=callback.data)
    await callback.message.edit_text(mt.DONE_CHANGE_LANG)
