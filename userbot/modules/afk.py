""" Uerbot module which contains afk-related commands"""

from datetime import datetime
import time

from random import choice, randint

from telethon.events import StopPropagation

from userbot import (
    ISAFK,  # pylint:disable=E0602
    AFKREASON,
    CMD_HELP,
    BOTLOG,
    BOTLOG_CHATID,
    PM_AUTO_BAN)
from userbot.events import register

AFKSTR = [
    "What the hell you want now?",
    "OMG, I'm busy right now so come back later",
    "Would ya spend your time with someone",
    "My god, i don't know how to respond you right now, so i'll text you later",
    "Don't you have any other work to do?",
    "I should've never done this, so wait for my master",
    "you should talk to yourself while I'm AFK!",
    "How many time's should i tell you to wait until my master come's",
    "Hang in there I'm just went to Mars",
    "You better wait until next week, so i can ignore you again.",
    "Come on man I have to sleep now, dattebayo"]

global USER_AFK
global afk_time
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
afk_start = {}


@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    afk_e.text
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"Going AFK!\
        \nReason: `{string}`")
    else:
        await afk_e.edit("Going AFK!")
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\nYou went AFK!")
    ISAFK = True
    afk_time = datetime.now()  # pylint:disable=E0602
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    COUNT_MSG = 0
    USERS = {}
    AFKREASON = None
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)

    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("I'm no longer AFK.")
        time.sleep(3)
        await msg.delete()
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "You've recieved " + str(COUNT_MSG) + " messages from " +
                str(len(USERS)) + " chats while you were away",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " sent you " + "`" + str(USERS[i]) + " messages`",
                )


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "a while ago"
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "Yesterday"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` ago"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` ago"
            else:
                afk_since = f"`{int(seconds)}s` ago"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"I'm AFK since {afk_since}.\
                        \nReason: `{AFKREASON}`")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(f"I'm still AFK since {afk_since}.\
                            \nReason: `{AFKREASON}`")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "a while ago"
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "Yesterday"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)}h{int(minutes)}m` ago"
            elif minutes > 0:
                afk_since = f"`{int(minutes)}m{int(seconds)}s` ago"
            else:
                afk_since = f"`{int(seconds)}s` ago"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"I'm AFK since {afk_since}.\
                        \nReason: `{AFKREASON}`")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(f"I'm still AFK since {afk_since}.\
                            \nReason: `{AFKREASON}`")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


CMD_HELP.update({
    "afk":
    ".afk [Optional Reason]\
\nUsage: Sets you as afk.\nReplies to anyone who tags/PM's \
you telling them that you are AFK(reason).\n\nSwitches off AFK when you type back anything, anywhere.\
"
})
