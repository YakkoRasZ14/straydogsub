# Import all the necessary packages
import os
import time
from platform import node
from telethon.sessions import StringSession
from telethon import TelegramClient
from dotenv import load_dotenv
from logging import getLogger, basicConfig, DEBUG, INFO
from sys import version_info
from distutils.util import strtobool as sb
from platform import uname

load_dotenv("config.env")

Up_Time = time.time()
bot_version = "1.0b"

# Setting up bot log things
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get(
    "CONSOLE_LOGGER_VERBOSE") or "False")

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO)
LOGS = getLogger(__name__)

# Checking for new python version
if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info(
        "It seems you have python version below than 3.9,"
        "Oh shit this thing can't run in older python version."
        "Go and update Python now."
    )
    quit(1)

CONFIG_CHECK = os.environ.get("__REMOVE__THIS__LINE__" or None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the mentioned first line in config.env"
    )
    quit(1)

API_KEY = os.environ.get("API_KEY") or None
API_HASH = os.environ.get("API_HASH") or None

STRING_SESSION = os.environ.get("STRING_SESSION") or None

ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/a7d9ae50487b75a4fd672.jpg"
ALIVE_NAME = os.environ.get("ALIVE_NAME") or uname().node

BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID") or 0

BOTLOG = sb(os.environ.get("BOTLOG") or False)
if BOTLOG:
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER") or False)
else:
    LOGSPAMMER = False

U_GITHUB_LINK = os.environ.get("U_GITHUB_LINK") or None
GITHUB_LINK = os.environ.get(
    "O_GITHUB_LINK") or "https://github.com/jokerhacker22/"

GITHUB_REPO = os.environ.get("GITHUB_REPO") or "https://github.com/MrRobot22/"
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")

TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TEMP_DOWNLOAD_DIRECTORY") or "./downloads"

PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN")) or False
DB_URI = os.environ.get("DATABASE_URL") or None

DEFAULT_BIO = os.environ.get("DEFAULT_BIO")

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
HEROKU_MEMEZ = os.environ.get("HEROKU_MEMEZ")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")

if STRING_SESSION:
    bot = TelegramClient(StringSession(str(STRING_SESSION)), API_KEY, API_HASH)
else:
    bot = TelegramClient("userbot", API_KEY, API_HASH)

#global variables
CMD_HELP = {}
ISAFK = False
AFKREASON = None
