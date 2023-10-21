import logging
import sqlite3
from settings.config import TG_TOKEN, WEB_APP_URL, AUTH_URL, REG_URL
import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = TG_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    user_id = message.from_user.id
    r = requests.get(f'{AUTH_URL}')

    markup = types.InlineKeyboardMarkup()

    if r.status_code == 200:
        markup.add(types.InlineKeyboardButton('Открыть меню', web_app=WebAppInfo(url='/index.html')))
        await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=markup)
    else:
        markup.add(types.InlineKeyboardButton('Открыть меню', web_app=WebAppInfo(url=REG_URL)))
        await message.answer(f"Привет! Ты не зарегистрирован. Пожалуйста, зарегистрируйся., {message.from_user.full_name}", reply_markup=markup)


@dp.message_handler(commands=['showWebApp'])
async def show_web_app(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть меню', web_app=WebAppInfo(url=WEB_APP_URL)))
    await message.answer("ado", reply_markup=markup)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
