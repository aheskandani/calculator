from unittest import result
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from instaloader import Instaloader, Profile
import math
import numpy as np

bot_token = '1310337464:AAFZeDEfYF1S-1MZ4p1ht_jW8Jq0zoeqlLo'
updater = Updater(bot_token, use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text('Hello friend to instagram profile save bot 🌹\nPlease enter the username or url and wait to download 🙏🏻')

def calculate(update: Update, context: CallbackContext):
    result = str(math.factorial(int(update.message.text)))
    update.message.reply_text(result)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('id', id))
updater.dispatcher.add_handler(MessageHandler(Filters.text, calculate))
updater.dispatcher.add_handler(MessageHandler(Filters.command, calculate))

updater.start_polling()