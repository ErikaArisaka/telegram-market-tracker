import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

start_selection = types.ReplyKeyboardMarkup()
start_selection.row('eBay')
start_selection.row('Warframe.market')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome!\nPlease select one of the following markets:", reply_markup=start_selection)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)