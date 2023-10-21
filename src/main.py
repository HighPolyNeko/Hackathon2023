import logging
from settings.config import TG_TOKEN, WEB_APP_URL, AUTH_URL, REG_URL
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = TG_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    user_id = message.from_user.id
    r = requests.get(f'{AUTH_URL}')

    markup = types.ReplyKeyboardMarkup()

    if r.status_code == 200:
        await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=markup)
        await show_web_app(message)
    else:
        markup.add(types.KeyboardButton('Зарегистрироваться', web_app=WebAppInfo(url=REG_URL)))
        await message.answer(
            f"Привет! Ты не зарегистрирован. Пожалуйста, зарегистрируйся., {message.from_user.full_name}",
            reply_markup=markup)


async def show_web_app(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть меню', web_app=WebAppInfo(url=WEB_APP_URL)))
    await message.answer(text="Меню", reply_markup=markup)


@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.Message):
    requests.post(f'{AUTH_URL}data={message.web_app_data.data}')

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
