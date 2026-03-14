import re

from aiogram import types
from aiogram.filters import Command, CommandObject
from aiogram.filters.state import StateFilter
from sqlalchemy.ext.asyncio import AsyncSession

from app.routers import admin_router
from database.models import User, UserStatus


@admin_router.message(StateFilter(None), Command("ban"))
@admin_router.message(StateFilter(None), Command("unban"))
async def ban_unban_users_command(
    message: types.Message, command: CommandObject, session: AsyncSession
) -> None:
    """Блокирует или разблокирует пользователей, принимает список id через ','"""

    command_name = command.command.lower()
    is_banned = command_name == "ban"
    text_success, text_action, text_error = get_ban_text(is_banned)

    if args := check_args_type(type=int, data_list=command.args):
        for id in args:
            try:
                if is_banned:
                    await User.update(session, id=id, status=UserStatus.Banned)
                else:
                    await User.update(session, id=id, status=UserStatus.User)
                await message.answer(f"✅ User <code>{id}</code> has been {text_action}.")
            except Exception:
                await message.answer(f"{text_error} for user <code>{id}</code>.")
    else:
        await message.answer(text_success)


def check_args_type(type: type, data_list: str) -> list | bool:
    try:
        return list(map(type, re.split(r"[ ,]+", data_list)))
    except:
        return False


def get_ban_text(is_banned: bool):
    text_success = (
        "✅ Send user IDs separated by ',' to ban users.\nExample: <code>/ban 123456, 789012</code>"
        if is_banned
        else "✅ Send user IDs separated by ',' to unban users.\nExample: <code>/unban 123456, 789012</code>"
    )

    text_action = "🔒 Banned" if is_banned else "🔓 Unbanned"
    text_error = "⚠️ Error while updating status"
    return text_success, text_action, text_error
