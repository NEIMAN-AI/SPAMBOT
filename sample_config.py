from os import getenv

from decouple import config

APP_ID = getenv("APP_ID", "16942102")

API_HASH = getenv("API_HASH", "eb72f958fd9dbad872a9ff1836ad96e6")

HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)

BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
BOT_TOKEN21 = config("BOT_TOKEN21", default=None)
BOT_TOKEN22 = config("BOT_TOKEN22", default=None)
BOT_TOKEN23 = config("BOT_TOKEN23", default=None)
BOT_TOKEN24 = config("BOT_TOKEN24", default=None)
BOT_TOKEN25 = config("BOT_TOKEN25", default=None)
try:
    SUDO_USERS = str(getenv("SUDO_USERS", "123 456")).split(" ")
except Exception:
    SUDO_USERS = str(getenv("SUDO_USERS", "123 456"))

START_MESSAGE = getenv("START_MESSAGE", None)

PING_PIC = getenv("PING_PIC", None)

START_PIC = getenv("START_PIC", None)


HELP_MSG = getenv("HELP_MSG", None)
HELP_PIC = getenv("HELP_PIC", "https://graph.org/file/bf3fb268e32f565697e39.jpg")
LOG_CHANNEL = getenv("LOG_CHANNEL", None)

HANDLER = getenv("HANDLER", "/")
