import json
from telegram import Update
from fastapi import FastAPI, Request

from telegram_bot import dispatcher, updater

app = FastAPI()


@app.get("/debug")
async def debug():
    return {"message": "it works!"}


@app.post("/webhook/")
async def webhook(request: Request):
    update = Update.de_json(await request.json(), updater.bot)
    dispatcher.process_update(update)
    return {"ok": "POST request processed"}

