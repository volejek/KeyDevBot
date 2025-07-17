import asyncio
import pytz
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config import BOT_TOKEN, SEND_HOUR, SEND_MINUTE, SEND_MINUTE0, SEND_HOUR0
from handlers import handle_time_reply
from scheduler import send_morning_message, send_evening_message

LOCAL_TZ = pytz.timezone("Asia/Bishkek")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.message.register(handle_time_reply)
async def on_startup():
    scheduler = AsyncIOScheduler(timezone=LOCAL_TZ)
    # Запланировать отправку утреннего сообщения
    scheduler.add_job(send_morning_message, CronTrigger(hour=SEND_HOUR, minute=SEND_MINUTE, timezone=LOCAL_TZ), kwargs={"bot": bot})
    
    print(f"Утреннее сообщение будет отправлено в {SEND_HOUR}:{SEND_MINUTE:02d} по {LOCAL_TZ}")
    print("Бот запущен и планировщик активен.")
    scheduler.add_job(send_evening_message, CronTrigger(hour=SEND_HOUR0, minute=SEND_MINUTE0, timezone=LOCAL_TZ), kwargs={"bot": bot})
    print(f"Вечернее сообщение будет отправлено в {SEND_HOUR0}:{SEND_MINUTE0:02d} по {LOCAL_TZ}")
    scheduler.start()
    scheduler.print_jobs()
async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
