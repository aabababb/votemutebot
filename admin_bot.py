# coding=UTF-8
import logging
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler

from vote import fuck, vote
from clear import clear_message
from filters import status_update
from start import start
from functools import partial

class AdminBot():
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dp = self.updater.dispatcher

    def error(self, bot, update,error):
        try:
            bot.deleteWebhook()
            raise error
        except Exception as e:
            logging.error(e)

    def run(self,mutetime1):
        self.dp.add_handler(CommandHandler('start', start))
        #fuck1 = partial(fuck,mutetime1)
        self.dp.add_handler(CommandHandler('fuck', fuck,pass_args=True))
        self.dp.add_handler(CallbackQueryHandler(vote))
        self.dp.add_handler(MessageHandler(status_update, clear_message))
        self.dp.add_error_handler(self.error)
        self.updater.start_polling()
        self.updater.idle()
