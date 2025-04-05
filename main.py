# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#comment

import os
import telebot
import requests

API_TOKEN = os.getenv("TELEGRAM_API")

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет, я помощник OPEN AI. Какой вопрос?
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(content_types=['text'])
def message(message):
    params = {
      "sender": "user1",
      "message": message.text
    }
    response = requests.post("https://ai-agent-vsnj.onrender.com/webhooks/rest/webhook", json=params)
    data = response.json()
    bot.reply_to(message, data[0]['text'])

bot.infinity_polling()

#result = openai.Model.list()
#print(result)

# create a chat completion
#chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
#print(chat_completion.choices[0].message.content)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    token = os.environ.get('OPENAI_KEY', 'N/a')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/