import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('6680209213:AAEYJh23Ld3b-Jq7XRkLbUExf6Uvt_opmyU')
name = None

@bot.message_handler(commands=['intro'])
def start(message):
    conn = sqlite3.connect('players.db')
    cur = conn.cursor()

    # cur.execute('CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))')
    # conn.commit()
    # cur.close()
    # conn.close()

    bot.send_message(message.chat.id, 'Hello, we will register you now. Enter your name!')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name 
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter the password')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('players.db')
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, pass) VALUES ('%s','%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Users list', callback_data = 'users'))
    bot.send_message(message.chat.id, 'User is registered', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('players.db')
    cur = conn.cursor()

    cur.execute(
        'SELECT * FROM users')
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Name:{el[1]}, Password: {el[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
