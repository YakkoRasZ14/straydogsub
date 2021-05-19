import pyfiglet
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.fg(?: |$)(.*)")
async def figlet(fg):
    if fg.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital"}
    input_str = fg.pattern_match.group(1)
    if "." in input_str:
        text, cmd = input_str.split(".", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await fg.edit("`Please add some text to figlet`")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await fg.edit("`Invalid selected font.`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await fg.respond("‌‌‎`{}`".format(result))
    await fg.delete()

CMD_HELP.update({
    "figlet":
        ".fg"
    "\nUsage: Just nothing but figlet in telegram"
    "\n\nExample: `.figlet <Text Style>`"
})
