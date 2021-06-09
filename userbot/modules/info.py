"""
Code created by Joker Hacker for Stray Dogs UB, 
Son please take care of your mom if you try to steal or copy the code
thanks to @tgscanrobot from telegram for such a wonderful bot
"""


import asyncio
import re, os
from typing import Pattern
from userbot import bot, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register
from telethon.errors import YouBlockedUserError
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

##dinfo(detailed user info) module starts from here
conver = "@tgscanrobot"
unknown = "This human is not in my database."
slow = "Whoa! Slow down,"
@register(outgoing=True, pattern="^.dinfo ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    username = event.pattern_match.group(1)
    if username is None:
        await event.edit(
            "`Oh man c'mon gimme id/username/tag`"
        )
        return
    await event.edit("`Accessing NASA Database.....`")
    async with bot.conversation(conver) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(username)
            response = await conv.get_response()
            if unknown in response.text:
                ##If the user is not in tgscanrobot database, then inform the user
                await event.edit("`Oops sorry I can not parse this user now`")
            elif slow in response.text:
                #If the bot says to wait and try again.
                await event.edit("`Uh man just be slow and try again...`")
            else:
                ##Using re to replace some words in response.txt
                response1 = re.sub(r"Human found!","**Hey I found your leaked info!**", response.text, count=1)
                response2 = re.sub(r"Telegram ID","**ID**", response1, count=1)
                response3 = re.sub(r"Name","**Skid Name**", response2, count=1)
                response3 += "\n\n\t `This info was gathered using Stray Dogs UB.`"
                await event.edit(response3)
        except YouBlockedUserError:
            await event.edit("**Error**\n It seems you have block the bot(TgScanRobot),\n Man unblock it already.")

##uinfo(user info) module starts from here
@register(outgoing=True, pattern="^.uinfo ?(.*)")
async def who(event):
    """ For .info command, get info about a user. """
    if event.fwd_from:
        return

    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user(event)
    caption = await fetch_info(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id
    replied_user_profile_photos = await bot(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )

    if not message_id_to_reply:
        message_id_to_reply = None

    await bot.send_message(
        event.chat_id,
        caption,
        reply_to=message_id_to_reply,
        parse_mode="markdown",
        file=replied_user.profile_photo,
        force_document=False,
        silent=True,
    )
    await event.delete()


async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit("**ERROR**\n" + str(err))
            return None
        replied_user_profile_photos = await bot(
            GetUserPhotosRequest(
                user_id=replied_user.user.id, offset=42, max_id=0, limit=80
            )
        )

    return replied_user


async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    is_restricted = replied_user.user.restricted
    is_verified = replied_user.user.verified
    first_name = first_name.replace("\u2060", "") if first_name else (" ")
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    user_profile_photos_count = "None"
    try:
        user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    username = "@{}".format(username) if username else ("This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio

    if user_id != (await event.client.get_me()).id:
        common_chat = replied_user.common_chats_count
    else:
        common_chat = "This user has no common chat with you."

    caption = f"""
            \t **User info Panel** \
            \n\n **Common info.** \
            \n\n User ID : `{user_id}` \
            \n FIrst Name : `{first_name}` \
            \n Last Name : `{last_name}` \
            \n Username : `{username}` \
            \n User Bio : `{user_bio}` \
            \n\n **Advanced info.**
            \n Is Bot? : `{is_bot}` \
            \n Is Restricted : `{is_restricted}` \
            \n Is Verified by Telegram? : `{is_verified}` \
            \n\n **Extras.**
            \n No. of Profile Pictures : `{user_profile_photos_count}` \
            \n Common Groups : `{common_chat}` \
            \n\n Permanent link : [{first_name}](tg://user?id={user_id}">{first_name})
            """

    return caption



CMD_HELP.update({
    "info":
    ".uinfo <username>"
    "\nUsage: A basic detail about a user."
    "\n\n.dinfo <username>"
    "\nUsage: You wanna see someone who is in which group? fun right give a try."
})