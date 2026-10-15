import os
from dotenv import load_dotenv, find_dotenv
from telethon import TelegramClient, events

# Force load .env file
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path, override=True)

# Fetch values from environment
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

# Hardcode fallback values if .env continues to fail reading
if not API_ID or not API_HASH:
    
    API_ID = 31936108
    API_HASH = '687a69eaf4a3f795078e44e0883e150c'

client = TelegramClient('nami_telegram_session', int(API_ID), API_HASH)

AUTO_REPLY_TEXT = (
    "Hello! I'm Nami, Dipjoy's AI Assistant.\n"
    "Master is currently offline. When he comes online, "
    "he will reply to your message."
)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_reply_handler(event):
    sender = await event.get_sender()
    sender_name = sender.first_name if sender and sender.first_name else "Friend"
    
    print(f"📩 New Message from {sender_name}: {event.text}")
    await event.reply(AUTO_REPLY_TEXT)
    print(f"🤖 Auto-reply successfully sent to {sender_name}!")

print("🚀 Nami Telegram Auto-Responder active in background...")

client.start()
client.run_until_disconnected()