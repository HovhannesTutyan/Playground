import telebot
import requests
import json

bot = telebot.TeleBot('7095392986:AAErTMkTFedOdxeMErpW_6xYXE-YiwZWYA8')
API = '62b4024ececf8274fe8e6daa37886601'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, enter the country name')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.send_message(message.chat.id, f'Now the weather in {city.upper()} is {temp} * Celsius')

        image = 'sun.jpg' if temp > 5.0 else "cold.png"
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'The country is not correct')

bot.polling(non_stop=True)