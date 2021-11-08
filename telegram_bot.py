from telegram import Update
from telegram.ext import Updater, Dispatcher, MessageHandler, Filters, CallbackContext, CommandHandler

import settings
import utils


def command_start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text=(
            "Привет! Чтобы воспользоваться ботом, отправь ему номер группы и дату, по которой ты хочешь "
            "получить расписание (пример: 'АНГ.203.Б-1 2021-05-24'/'ФИС.203.Б 2021-05-25')"
        )
    )


def perform_message(update: Update, context: CallbackContext) -> None:
    t_message: str = update.message.text
    t_message_parse_result, is_valid = utils.parse_message(t_message)

    if not is_valid:
        update.message.reply_text(text=t_message_parse_result[1])
    else:
        update.message.reply_text(
            text=utils.get_t_result(*t_message_parse_result)
        )


def _setup_dispatcher(_dispatcher: Dispatcher):
    _dispatcher.add_handler(CommandHandler("start", command_start))
    _dispatcher.add_handler(MessageHandler(Filters.text, perform_message))

    # TODO: perform image and voice receiving
    # _dispatcher.add_handler(MessageHandler(Filters))

    # TODO: perform sticker receiving
    # _dispatcher.add_handler(MessageHandler(Filters))
    return _dispatcher


updater = Updater(settings.TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = _setup_dispatcher(updater.dispatcher)
