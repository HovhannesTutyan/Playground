import telebot
import requests
import json
from telebot import types
from currency_converter import CurrencyConverter

sumAmount = 0

bot = telebot.TeleBot('6734298829:AAElu9ykhFFxQ9GCxUCp1QsnffHLNBlg-44')

currency = CurrencyConverter()
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, enter the amount')
    bot.register_next_step_handler(message, amount)

def amount(message):
    sumAmount = message.text.strip()

bot.polling(non_stop=True)