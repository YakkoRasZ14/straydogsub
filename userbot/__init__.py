# Import all the necessary packages
from telethon.sessions import StringSession
from telethon import TelegramClient
from requests import get
from dotenv import load_dotenv
from pySmartDL import SmartDL
from pylast import LastFMNetwork, md5
from distutils.util import strtobool as sb
from logging import basicConfig, getLogger, INFO, DEBUG
from sys import version_info
from platform import uname
import os
import time

# load config file if it exists
load_dotenv("config.env")

# Small variables which is used in modules
Up_Time = time.time()
bot_version = "0.1b"

# Get this variable from my.telegram.org
API_KEY = os.environ.get("API_KEY") or None
API_HASH = os.environ.get("API_HASH") or None

# Alive name and logo to be appear in .alive message
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/a7d9ae50487b75a4fd672.jpg"
ALIVE_NAME = os.environ.get("ALIVE_NAME") or uname().node

# Turn this on if you want to kick and get a notification about spam Bots
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT") or "False")
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT") or "False")

# THe botlog chat id of the group where you want logging to work
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID")) or 0
BOTLOG = sb(os.environ.get("BOTLOG") or False)
if BOTLOG:
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER") or False)
else:
    LOGSPAMMER = False

BIO_PREFIX = os.environ.get("BIO_PREFIX") or None

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

# chrome driver location
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or None

# config check or config.env or sample_config.env
CONFIG_CHECK = os.environ.get("__REMOVE__THIS__LINE__" or None)
if CONFIG_CHECK:
    LOGS.info(
        "Please remove the mentioned first line in config.env"
    )
    quit(1)

# postgresql DataBase URL; ex:
# postgres://username:password@ip/localhost:port/dbname
DB_URI = os.environ.get("DATABASE_URL") or None

# Default bio message for .alive module
DEFAULT_BIO = os.environ.get("DEFAULT_BIO") or None

# String_session value generated from strin_session.py
STRING_SESSION = os.environ.get("STRING_SESSION") or None

# User Github Link to be shown in .alive module
U_GITHUB_LINK = os.environ.get("U_GITHUB_LINK") or None

# Leave this as empty if you Don't know
O_GITHUB_LINK = os.environ.get(
    "GITHUB_LINK") or "https://github.com/jokerhacker22/"
GITHUB_REPO = os.environ.get(
    "GITHUB_REPO") or "https://github.com/JokerHacker22/Straydogsub"

# Your github access token
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN") or None

GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME") or None

TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TEMP_DOWNLOAD_DIRECTORY") or "./downloads"

# Turn this on if you want to Auto ban Whoever PM.
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN")) or False

# These values are needed for heroku and .set module, get this from heroku
# dashboard
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY") or None
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ")) or True
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME") or None

GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN") or None

USER_TERM_ALIAS = os.environ.get("USER_TERM_ALIAS") or "root@Fsociety"

ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY") or "./zips"
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME") or "True")


G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA") or None
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID") or None
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET") or None
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA") or None
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID") or None

UPSTREAM_REPO_URL = (os.environ.get("UPSTREAM_REPO_URL")
                     or "https://github.com/jokerhacker22/straydogsub.git")
UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH") or "Devil"


if not os.path.exists("bin"):
    os.mkdir("bin")

# this if-else statement made to make testing and building easy, no need
# to download these always when you run the bot
if not os.path.exists("../bin"):
    binaries = {
        "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown": "bin/megadown",
        "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
    }

    for binary, path in binaries.items():
        downloader = SmartDL(binary, path, progress_bar=False)
        downloader.start()
        os.chmod(path, 0o755)
    else:
        pass

if STRING_SESSION:
    bot = TelegramClient(StringSession(str(STRING_SESSION)), API_KEY, API_HASH)
else:
    bot = TelegramClient("userbot", API_KEY, API_HASH)

# Checking for new python version
if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info(
        "It seems you have python version below than 3.9,"
        "Oh sh*t this thing can't run in older python version."
        "Go and update Python now."
    )
    quit(1)

#global variables
CMD_HELP = {}
ISAFK = False
AFKREASON = None
