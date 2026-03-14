from logging import getLogger

from core.config import LOG_FILE_PATH
from loguru import logger

FORMAT = "[{time}] [{level}] [{file.name}:{line}]  {message}"
ROTATION = "1 month"
COMPRESSION = "zip"

logger.add(
    LOG_FILE_PATH,
    format=FORMAT,
    level="DEBUG",
    rotation=ROTATION,
    compression=COMPRESSION,
)

logger.level("BOT", no=18, color="<green>", icon="🚨")
logger.level("MESSAGE", no=15, color="<blue>", icon="✍️")
logger.level("CALLBACK", no=15, color="<blue>", icon="📩")
logger.level("DATABASE", no=17, color="<magenta>", icon="💾")
logger.level("MAILING", no=16, color="<yellow>", icon="📢")
logger.level("ANNOUNCE", no=14, color="<white>", icon="📣")
logger.level("API", no=19, color="<cyan>", icon="🌐")
logger.level("SCRIPT", no=20, color="<red>", icon="🔧")

getLogger("aiogram").addFilter(
    lambda r: r.getMessage().find("Field 'database_user' doesn't exist in") == -1
)
