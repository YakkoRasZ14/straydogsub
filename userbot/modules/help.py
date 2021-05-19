# Import all the ncessary pakcages needed
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please provide a valid module name")
    else:
        string = "**⚙️ Hello there, Welcome to Help option ⚙️** \n\n"
        for i in CMD_HELP:
            string += "`✨" + str(i)
            string += "`\n"
        await event.edit(f"{string}"
                         "\n\nPlease specify which module you want help for"
                         "\n Usage:.help <Module> \n\n Like `.help alive`"
                         )
