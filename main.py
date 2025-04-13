from fastapi import FastAPI, Request
from bot import bot, dp, BOT_TOKEN
from aiogram import types
import asyncio
import os
from fastapi.responses import HTMLResponse


WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{os.getenv("WEBHOOK_BASE")}{WEBHOOK_PATH}'

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = types.Update(**await request.json())
    await dp.feed_update(bot, update)
    return {"ok": True}

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()

@app.get("/")
async def read_root():
    return {"message": "Hello, World"}
