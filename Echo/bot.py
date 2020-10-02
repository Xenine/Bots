"""
This is a echo bot.
It echoes any incoming text messages.
"""

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import API_TOKEN


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.answer("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_start_command(msg: types.Message):
    await msg.answer("Все, что ты будешь мне писать, я буду отправлять тебе обратно!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await msg.answer(msg.text)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)