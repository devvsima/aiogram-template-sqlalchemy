from aiogram import Dispatcher

from app.middlewares.i18n import i18n_middleware
from app.routers import admin_router, common_router, user_router
from database.connect import async_session

from .admin import AdminMiddleware
from .common import CommonMiddleware
from .database import DatabaseMiddleware
from .user import UsersMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(DatabaseMiddleware(async_session))

    user_router.message.middleware(UsersMiddleware())
    user_router.callback_query.middleware(UsersMiddleware())

    common_router.message.middleware(CommonMiddleware())

    admin_router.message.middleware(AdminMiddleware())

    common_router.message.middleware(i18n_middleware)
    admin_router.message.middleware(i18n_middleware)
    user_router.message.middleware(i18n_middleware)
