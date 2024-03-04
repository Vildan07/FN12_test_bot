# Aiogram
# pyTelegramBotApi

# -----------------------------------------------------------------------

from telebot import TeleBot
from telebot.types import Message
bot = TeleBot(token='6948819597:AAEn1SRyai2hNC4gOyHpYMEp-fbmg9jOulI')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu Alaykum {full_name}")


bot.polling()