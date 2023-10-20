import logging
import sqlite3
from aiogram import Bot, Dispatcher, types

API_TOKEN = '5883070708:AAHIcmhvLJ2IAeFohKWIloXskBWspdnduqw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Подключение к базе данных "Death_Note"
conn = sqlite3.connect('Death_Note.db')
cursor = conn.cursor()


# Создание таблицы для хранения пользователей (если она еще не создана)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        telegram_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT
    )
''')
conn.commit()

async def on_start(message: types.Message):
    user_id = message.from_user.id
    if user_id:
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

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
