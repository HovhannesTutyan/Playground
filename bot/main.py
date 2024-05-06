import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6680209213:AAEYJh23Ld3b-Jq7XRkLbUExf6Uvt_opmyU')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}{message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u> Information</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')
    
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Visit site', url='https://google.com'))
    # markup.add(types.InlineKeyboardButton('Delete Photo', callback_data='delete'))
    # markup.add(types.InlineKeyboardButton('Change Text', callback_data='edit'))
    btn1 = types.InlineKeyboardButton('Visit site', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit Text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a nice photo', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Visit site':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'Photo is deleted')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit Text', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)