from aiogram import types
from config import POST_URL
from scheduler import get_parent_message_id, get_parent_evening_message_id
import aiohttp

async def handle_time_reply(message: types.Message):
    # 1) убеждаемся, что это ответ на сообщение бота
    if not message.reply_to_message:
        return

    parent_id = message.reply_to_message.message_id
    morning_id = get_parent_message_id()
    evening_id = get_parent_evening_message_id()

    # 2) выясняем тип отметки
    if parent_id == morning_id:
        time_type = "arrival"
    elif parent_id == evening_id:
        time_type = "departure"
    else:
        return  # не наш запрос

    data = {
        "username": message.from_user.full_name or message.from_user.username,
        "text": message.text,
        "date": message.date.date().isoformat(),
        "comment_date": message.date.isoformat(),
        "message_id": message.message_id,
        "parent_message_id": parent_id,
        "chat_id": message.chat.id,
        "type": time_type,
    }

    print(f"Отправка данных ({time_type}): {data}")
    async with aiohttp.ClientSession() as session:
        async with session.post(POST_URL, json=data) as resp:
            print(f"Ответ сервера: {await resp.text()}")