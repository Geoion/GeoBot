# -*- coding: utf-8 -*-
import random 

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def roll(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="您的点数为：{} (1-100)".format(random.choice(range(1,101))))