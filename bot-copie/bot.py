from telethon import TelegramClient, events

API_ID = 34075359
API_HASH = "f3278a98e215c293901e43db00c74801"
SOURCE_GROUP = "https://t.me/+Gwq9c6nE-XIwODI0"
TARGET_GROUP = "https://t.me/+ddhEXjO1jvxjMDY8"

client = TelegramClient("session_bot", API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_GROUP))
async def handler(event):
    await client.send_message(TARGET_GROUP, event.message)

print("Bot démarré ! En attente de messages...")
client.start()
client.run_until_disconnected()