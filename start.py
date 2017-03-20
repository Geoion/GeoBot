# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import TOKEN

from bot import (start, roll, echo, caps)

if __name__ == "__main__":
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('roll', roll))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))
    updater.start_polling()
    