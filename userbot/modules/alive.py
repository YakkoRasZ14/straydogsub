# import necessary modules to work
from userbot import ALIVE_LOGO, O_GITHUB_LINK, U_GITHUB_LINK, bot, CMD_HELP, ALIVE_NAME, Up_Time, bot_version, GITHUB_REPO
from userbot.events import register
from platform import python_version
from telethon import version
import time

# Thanks to Thunderuserbot for this code,
# https://github/Thundergang/Thunderuserbot.
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@register(outgoing=True, pattern=r"^.(alive|on)$")
async def amireallyalive(alive):
    # This is to make sure .alive command works perfectly
    UpTime = get_readable_time((time.time() - Up_Time))
    output = (
        f"**✨ Hey there I'm `{ALIVE_NAME}` ✨**\n"
        "`No system is Safe!`\n"
        "\n===============================\n"
        f"**Python 🐍**: v`{python_version()}`\n"
        f"**Telethon**: v`{version.__version__}`\n"
        f"**Bot Version 🤖**: v`{bot_version}`\n"
        "=================================\n\n"
        f"**Bot Uptime**: `{UpTime}`\n"

    )

    if U_GITHUB_LINK:
        output += f"[Repo]({GITHUB_REPO}) | [My Github]({U_GITHUB_LINK}) | [Creator]({O_GITHUB_LINK}) \n"
    else:
        output += f"[Repo]({GITHUB_REPO}) | [My Github]({O_GITHUB_LINK}) "

    if ALIVE_LOGO:
        logo = ALIVE_LOGO
        await bot.send_file(alive.chat_id, logo, caption=output)
        await alive.delete()
    else:
        await alive.edit(output)


CMD_HELP.update({
    "alive":
    ".alive|.on"
    "\n Usage: Come on, type .alive/on in any chat to check this Userbot is online or not"
})
