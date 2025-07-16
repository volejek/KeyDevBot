from aiogram import types
from config import POST_URL
from scheduler import get_parent_message_id
import aiohttp

async def handle_reply(message: types.Message):
    parent_id = get_parent_message_id()
    if not parent_id or message.reply_to_message.message_id != parent_id:
        return  # не тот ответ

    data = {
        "username": message.from_user.full_name or message.from_user.username,
        "text": message.text,
        "date": message.date.date().isoformat(),
        "comment_date": message.date.isoformat(),
        "message_id": message.message_id,
        "parent_message_id": parent_id,
        "chat_id": message.chat.id,
    }
    print(f"Отправка данных: {data}")
    async with aiohttp.ClientSession() as session:
        async with session.post(POST_URL, json=data) as resp:
            print(await resp.text())
