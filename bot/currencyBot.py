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
    global sumAmount
    try: 
        sumAmount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'The amount must be integer')
        bot.register_next_step_handler(message, amount)
        return
    if sumAmount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('EUR/GBP', callback_data='eur/gbp')
        btn4 = types.InlineKeyboardButton('other', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Enter currency for exchange', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'The amount must be more than 0')
        bot.register_next_step_handler(message, amount)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(sumAmount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'You receive: {round(res, 2)}. You can try another amount.')
        bot.register_next_step_handler(call.message, amount)
    else:
        bot.send_message(call.message.chat.id, 'Enter the currency to be converted')
        bot.register_next_step_handler(call.message, myCurrency)

def myCurrency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(sumAmount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'You receive: {round(res, 2)}. You can try another amount.')
        bot.register_next_step_handler(message, amount)
    except:
        bot.send_message(message.chat.id, 'Something went wrong. Try again.')
        bot.register_next_step_handler(message, amount)
bot.polling(non_stop=True)