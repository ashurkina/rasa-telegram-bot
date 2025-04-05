import os
import telebot
import requests
from dotenv import load_dotenv
from threading import Thread

if os.getenv("RENDER") is None:
    load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_API")
URL_TOKEN = os.getenv("RENDER_RASA_PATH")

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Hi! How may I help you?
""")

# Handle text messages
@bot.message_handler(content_types=['text'])
def handle_message(message):
    params = {
        "sender": str(message.chat.id),
        "message": message.text
    }
    response = requests.post(URL_TOKEN, json=params)
    data = response.json()
    if isinstance(data, list) and data:
        bot.reply_to(message, data[0].get('text', '🤖 Пустой ответ.'))

def start_bot():
    bot.infinity_polling()
