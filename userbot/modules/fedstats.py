import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register, bot
from userbot import CMD_HELP

Rose = "@MissRose_bot"


@register(outgoing=True, pattern="^.fstat ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Checking...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
        user = sysarg
    if sysarg == "":
        await ok.edit(
            "`Shit gimme that bastard's id to check.`"
        )
        return
    else:
        async with bot.conversation(Rose) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                audio = await conv.get_response()
                if "The Following" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await bot.send_file(
                        event.chat_id,
                        audio,
                        caption=f"List of feds {user} has been banned in.\n\n Gathered by Stray Dogs UB",
                    )
                else:
                    await bot.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


@register(outgoing=True, pattern="^.finfo ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Extracting information...`")
    sysarg = event.pattern_match.group(1)
    async with bot.conversation(Rose) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + sysarg)
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nFederation Details Gathered by Stray Dogs UB")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @MissRose_Bot `and try again!")


CMD_HELP.update(
    {
        "fedstat": ".fstat <username/userid/reply to user>\nUse - To check fstat of a person.\
        \n\n.finfo <fedid>\nUse - To gather info about the fed."
    }
)
