# -*- coding: utf-8 -*-
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler)

from settings import TOKEN

from bot import (start, roll, echo, caps, inline_caps, unknown, help, userinfo)

if __name__ == "__main__":
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('roll', roll))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))
    dispatcher.add_handler(InlineQueryHandler(inline_caps))
    dispatcher.add_handler(CommandHandler('userinfo', userinfo))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # IMPORTANT: must put it in the end!!!!!!!!!
    updater.start_polling()
