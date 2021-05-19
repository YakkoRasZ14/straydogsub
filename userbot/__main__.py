from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\n The Mobile Number you entered is invalid' \
             '\n Go check that shit again'


try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit()

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("You are currently running StrayDogs_UB")

LOGS.info("Congo, your UB is running successfully, run .on/.alive to verify it")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
