import logging
import sqlite3
from settings.config import TG_TOKEN, WEB_APP_URL, AUTH_URL
import requests
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = TG_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def on_start(message: types.Message):
    user_id = message.from_user.id
    r = requests.get(f'{AUTH_URL}')
    r.status_code

    if r.status_code == 200:
        await message.answer(f"Привет, {user_id[1]}! Добро пожаловать!")
    else:
        await message.answer("Привет! Ты не зарегистрирован. Пожалуйста, зарегистрируйся.")


# Приветственное сообщение
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, пидор! Я могу помочь тебе с покупками в твоем обоссаном вагоне, если ты мне скажешь свой логин и пароль, а если у тебя его нет, так загистрируйся нахуй, а не морочь не мозги.")

# Обработка всех остальных сообщений
@dp.message_handler()
async def echo_message(message: types.Message):
    global Vremenniy_cringe
    Vremenniy_cringe = message.text
    print(Vremenniy_cringe)
    #await message.answer(message.text)


@dp.message_handler(commands=['showWebApp'])
async def show_web_app(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть меню', web_app=WebAppInfo(url=WEB_APP_URL)))
    await message.answer("ado", reply_markup=markup)


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
