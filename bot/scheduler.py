from aiogram import Bot
from aiogram.types import Message
from config import CHAT_ID

last_morning_message_id = None  # глобально запоминаем ID
last_evening_message_id = None 

async def send_morning_message(bot: Bot):
    global last_morning_message_id
    msg: Message = await bot.send_message(
        CHAT_ID,
        "Доброе утро! Пожалуйста, отметь во сколько ты сегодня приступаешь к работе, ответив комментарием на это сообщение."
    )
    last_morning_message_id = msg.message_id
    print(last_morning_message_id)

async def send_evening_message(bot: Bot):
    global last_evening_message_id
    msg: Message = await bot.send_message(
        CHAT_ID,
        "Добрый вечер! Пожалуйста, отметь во сколько ты сегодня уходишь с работы, ответив комментарием на это сообщение."
    )
    last_evening_message_id = msg.message_id
    print(last_evening_message_id)

def get_parent_message_id():
    return last_morning_message_id

def get_parent_evening_message_id():
    return last_evening_message_id