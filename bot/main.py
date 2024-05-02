import telebot

bot = telebot.TeleBot('6680209213:AAEYJh23Ld3b-Jq7XRkLbUExf6Uvt_opmyU')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling(non_stop=True)