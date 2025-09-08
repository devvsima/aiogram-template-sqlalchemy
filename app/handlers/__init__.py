from aiogram import Dispatcher
from aiogram.types import ErrorEvent

from utils.logging import logger

from .admin import admin_router
from .common import common_router
from .user import user_router
from .voide import voide_router


def setup_handlers(dp: Dispatcher) -> None:
    @dp.error()
    async def _error(event: ErrorEvent):
        logger.exception(event.exception)

    "В порядке срабатывания"
    dp.include_routers(
        common_router,  # 1
        user_router,  # 2
        admin_router,  # 3
        voide_router,  # 4
    )
