from telegram import Update
from telegram.ext import Updater, Dispatcher, MessageHandler, Filters, CallbackContext

import settings


def perform_message(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        text="Hello!"
    )


def _setup_dispatcher(_dispatcher: Dispatcher):
    _dispatcher.add_handler(MessageHandler(Filters.text, perform_message))
    return _dispatcher


updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = _setup_dispatcher(updater.dispatcher)
