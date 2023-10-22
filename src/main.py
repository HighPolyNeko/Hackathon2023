import io
import logging
from tkinter import Image
import pytesseract

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

    r.status_code = 4
    if r.status_code == 200:
        await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=markup)
        await show_web_app(message)
    else:
        markup.add(types.KeyboardButton('Зарегистрироваться', web_app=WebAppInfo(url=AUTH_URL)))
        await message.answer(
            f"Привет! Ты не зарегистрирован. Пожалуйста, зарегистрируйся., {message.from_user.full_name}",
            reply_markup=markup)


async def show_web_app(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть меню', web_app=WebAppInfo(url=WEB_APP_URL)))
    await message.answer(text="Меню", reply_markup=markup)

# Define a message handler to process images and extract the number after "билета"
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_image(message: types.Message):
    # Get the photo with the highest resolution
    photo = message.photo[-1]

    # Download the photo
    file_id = photo.file_id
    file_info = await bot.get_file(file_id)
    photo_url = file_info.file_path

    # Download the photo using aiohttp
    async with bot.session.get(f'https://api.telegram.org/file/bot{API_TOKEN}/{photo_url}') as response:
        if response.status == 200:
            photo_data = await response.read()
            with Image.open(io.BytesIO(photo_data)) as img:
                # Perform OCR using Tesseract to extract text
                text = pytesseract.image_to_string(img, lang='eng+rus', config='--oem 3 --psm 6')

                # Find the number following "билета"
                number = find_number_after_word(text, "билета")

                if number:
                    await message.reply(f"The number of ticket is: {number}")
                else:
                    await message.reply("No number found")
        else:
            await message.reply("Failed to download the image.")

def find_number_after_word(text, keyword):
    # Split the text by spaces and punctuation marks
    words = text.split()

    for i, word in enumerate(words):
        if word == keyword and i + 1 < len(words):
            number = words[i + 1]
            # Remove any non-numeric characters
            number = ''.join(filter(str.isdigit, number))
            return number

@dp.message_handler(content_types=["web_app_data"])
async def web_app(message: types.Message):
    requests.post(f'{AUTH_URL}data={message.web_app_data.data}')

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)

