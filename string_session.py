from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("Get your API_KEY an API_HASH from my.telegram.org")

API_KEY = int(input("Enter API_KEY here: "))
API_HASH = input("Enter API_HASH here: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Check your Telegram Saved Messages to copy the STRING_SESSION value")
    session_string = client.session.save()
    saved_messages_template = (
        "Hey there here is your String Session\n\n"
        "Generated from Fsociety's Code\n"
        f"<b>String_Session</b> : <code>{session_string}</code>"
        "Join SUpport group for more info @"

    )
    client.send_message("me", saved_messages_template, parse_mode="html")
