import telebot
from handlers import start_handler, message_handler_func, callback_query_handler
from config import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    start_handler(message, bot)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    message_handler_func(message, bot)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    callback_query_handler(call, bot)

bot.infinity_polling()
