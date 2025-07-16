import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
POST_URL = os.getenv("POST_URL")
SEND_HOUR = int(os.getenv("MORNING_SEND_HOUR"))
SEND_MINUTE = int(os.getenv("MORNING_SEND_MINUTE"))
print(BOT_TOKEN)
print(CHAT_ID)
print(POST_URL)
print(os.getenv("MORNING_SEND_HOUR"))
print(os.getenv("MORNING_SEND_MINUTE"))