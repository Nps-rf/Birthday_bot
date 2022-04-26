from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from config import TOKEN
from Database import Database
# from Maintainer import *

db = Database()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


class States(StatesGroup):
    Start_state = State()


@dp.message_handler(commands=['start'], state="*")
async def send_message(message: types.Message):
    await message.answer(text='*Добро пожаловать!*', parse_mode='markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
