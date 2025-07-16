from aiogram import Bot
from aiogram.types import Message
from config import CHAT_ID

last_morning_message_id = None  # глобально запоминаем ID

async def send_morning_message(bot: Bot):
    global last_morning_message_id
    msg: Message = await bot.send_message(
        CHAT_ID,
        "Доброе утро! Пожалуйста, отметь во сколько ты сегодня приступаешь к работе, ответив комментарием на это сообщение."
    )
    last_morning_message_id = msg.message_id

def get_parent_message_id():
    return last_morning_message_id