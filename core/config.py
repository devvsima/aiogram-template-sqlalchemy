from pathlib import Path

from environs import Env

DIR = Path(__file__).absolute().parent.parent

env = Env()
env.read_env()


# -< Database >-
class DatabaseSettings:
    NAME: str = env.str("DB_NAME", default=None)
    HOST: str = env.str("DB_HOST", default="localhost")
    PORT: int = env.int("DB_PORT", default=5432)
    USER: str = env.str("DB_USER", default="postgres")
    PASS: str = env.str("DB_PASS", default="postgres")

    URL: str = env.str("DB_URL", default=f"sqlite+aiosqlite:///{DIR}/database/db.sqlite3")

    if all((NAME, HOST, PORT, USER, PASS)):
        URL = f"postgresql+asyncpg://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"

    ECHO = False
    POOL_SIZE = 5
    MAX_OVERFLOW = 10


# -< Redis >-
class RedisSettings:
    HOST: str = env.str("REDIS_HOST", default=None)
    PORT: int = env.int("REDIS_PORT", default=6379)
    DB: int = env.int("REDIS_DB", default=5)

    URL: str = env.str("RD_URL", default=None)

    if all((HOST, PORT, DB)):
        URL = f"redis://{HOST}:{PORT}/{DB}"


# -< Telegram bot >-
class TelegramBotSettings:
    BOT_TOKEN: str = env.str("TELEGRAM_BOT_TOKEN", default=None)
    SKIP_UPDATES: bool = env.bool("SKIP_UPDATES", default=False)
    SET_COMMANDS: bool = env.bool("SET_COMMANDS", default=True)

    # Throtling
    RATE_LIMIT: int = env.int("RATE_LIMIT", default=3)
    TIME_WINDOW: int = env.int("TIME_WINDOW", default=1)

    # Admin
    ADMINS: list = env.list("ADMINS", default=None, subcast=int)
    NEW_USER_ALET_TO_GROUP: bool = env.bool("NEW_USER_ALET_TO_GROUP", default=True)
    MODERATOR_GROUP_ID: int = env.int("MODERATOR_GROUP_ID", default=None)
    BOT_CHANNEL_URL: str = env.str("BOT_CHANNEL_URL", default=None)

    # Webhook
    WEBHOOK_HOST: str = env.str("WEBHOOK_HOST", default=None)
    WEBHOOK_PORT: int = env.int("WEBHOOK_PORT", default=None)
    WEBHOOK_URL: str = env.str("WEBHOOK_URL", default=None)
    WEBHOOK_SECRET: str = env.str("WEBHOOK_SECRET", default=None)

    WEBHOOK_PATH: str = env.str("WEBHOOK_PATH", default=f"/webhook/{BOT_TOKEN}")

    IS_WEBHOOK = False
    if all((WEBHOOK_HOST, WEBHOOK_PORT, WEBHOOK_URL, WEBHOOK_SECRET, WEBHOOK_PATH)):
        IS_WEBHOOK = True

    # Other
    TIME_ZONE = "UTC"
    I18N_DOMAIN = "bot"


# -< Path\Dir >-
IMAGES_DIR = rf"{DIR}/images"
LOCALES_DIR = f"{DIR}/core/locales"
LOG_FILE_PATH: Path = DIR / "logs" / "logs.log"


# -< Other >-
database = DatabaseSettings()
redis = RedisSettings()
tgbot = TelegramBotSettings()
