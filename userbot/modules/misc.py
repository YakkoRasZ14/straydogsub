# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
""" Userbot module for other small commands. """

from random import randint
from time import sleep
from os import execl
import sys
import io
import sys
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.utils import time_formatter


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" +
                     itemo[index] + "`")


@register(outgoing=True, pattern="^.sleep ([0-9]+)$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    counter = int(time.pattern_match.group(1))
    await time.edit("`Going to Sleep, For a Moment`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    await event.edit("`Shutting Down`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "Bot shut down")
    await bot.disconnect()


@register(outgoing=True, pattern="^.restart$")
async def killdabot(event):
    await event.edit("`Restarting, Wait for a Moment`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n"
                                        "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@register(outgoing=True, pattern="^.community$")
async def bot_community(community):
    await community.edit(
        "\nJoin the Stray [Dogs Community](https://t.me/straydogsub) to learn and resolve your problems")


@register(outgoing=True, pattern="^.support$")
async def bot_support(wannahelp):
    """ For .support command, just returns the group link. """
    await wannahelp.edit(
        "\nJoin our Support Group to fix your problems and discuss"
        "\n[Support Group](https://t.me/straydogsub)"
    )


@register(outgoing=True, pattern="^.creator$")
async def creator(ereee):
    """ See who create this userbot. """
    await ereee.edit(
        "Creator of this userbot:"
        "\n??? ??? [Joker Hacker](https://github.com/jokerhacker22) ???")


@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    await e.edit(
        "Here's something for you to read:\n"
        "\n[User Bot's README.md](https://github.com/jokerhacker22/straydogsub/blob/6d3115fb43a427081a3ed9d2112e61583a91fd7b/README.md)")


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "[Click here](https://github.com/jokerhacker22/straydogsub) to open User Bot GitHub page."
    )


@register(outgoing=True, pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`")


CMD_HELP.update({"powermenu": ".sleep <seconds> :- Userbots get tired too. Let yours snooze for a few seconds.\n\n"
                 "shutdown :-Usage: Sometimes you need to shut down your bot. Sometimes you just hope to hear Windows XP shutdown sound... but you don't.\n\n"
                 "restart:-Usage: Restarts the bot !!"})

CMD_HELP.update({"userbot": ".support :-Usage: If you need help, use this command.\n\n"
                 "community :-Join the awesome Stray Dogs userbot community !!\n\n"
                 "repo:- If you are curious what makes the userbot work, this is what you need.\n\n"
                 "readme:- Provide links to setup the userbot and it's modules.\n\n"
                 "creator:- Know who created this awesome userbot !!\n"})

CMD_HELP.update({"tools": ".random <item1> <item2> ... <itemN>:-Get a random item from the list of items.\n\n"
                 "repeat <no.> <text> :-Usage: Repeats the text for a number of times. Don't confuse this with spam though.\n\n"
                 "raw:- Get detailed JSON-like formatted data about replied message.\n"})
