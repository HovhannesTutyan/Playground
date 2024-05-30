from aiogram import Bot, executor, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('7067365722:AAFLTbWwdXTJ3eyn0AMUKJDju4N6S9gorZs')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open the Web page', web_app=WebAppInfo(url='https://hovhannestutyan.github.io/TelegramApp/')))
    await message.answer('Hello', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')

executor.start_polling(dp)