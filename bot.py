
import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Tilni tanlang:\n1. O'zbek\n2. Русский")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
