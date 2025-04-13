from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from dotenv import load_dotenv
import aiohttp

import os

if os.getenv("RENDER") is None:
    load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_API')
URL_TOKEN = os.getenv("RENDER_RASA_PATH")

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    payload = {
        "sender": str(message.chat.id),
        "message": message.text
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(URL_TOKEN, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                if isinstance(data, list) and data:
                    reply_text = data[0].get("text", "🤖 Пустой ответ.")
                else:
                    reply_text = "🤖 Пустой ответ."
            else:
                reply_text = "❌ Ошибка связи с Rasa."

    await message.answer(reply_text)