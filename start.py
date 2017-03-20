# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler

from settings import TOKEN

from bot import (start, roll)

if __name__ == "__main__":
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('roll', roll))
    updater.start_polling()