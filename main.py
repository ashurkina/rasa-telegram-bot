from typing import Union
from fastapi import FastAPI
from telegram_bot import start_bot
from threading import Thread

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q" : q}

# Start Telegram bot in a separate thread when app launches
@app.on_event("startup")
def startup_event():
    Thread(target=start_bot, daemon=True).start()


# import os
# import telebot
# import requests
#
# API_TOKEN = os.getenv("TELEGRAM_API")
# URL_TOKEN = os.getenv("RENDER_RASA_PATH")
# bot = telebot.TeleBot(API_TOKEN)
#
# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """
# Привет, я помощник OPEN AI. Какой вопрос?
# """)
#
# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(content_types=['text'])
# def message(message):
#     params = {
#       "sender": str(message.chat.id), #check
#       "message": message.text
#     }
#     response = requests.post(URL_TOKEN, json=params)
#     data = response.json()
#     bot.reply_to(message, data[0]['text'])
#
# bot.infinity_polling()