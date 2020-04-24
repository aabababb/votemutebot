# coding=UTF-8
import logging
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler

from vote import fuck, vote,get_mutetime1
from clear import clear_jlmessage,clear_tmessage
from filters import status_update,ftext
from start import start


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
        get_mutetime1(mutetime1)
        self.dp.add_handler(CommandHandler('fuck', fuck,pass_args=True))
        self.dp.add_handler(CallbackQueryHandler(vote))
        self.dp.add_handler(MessageHandler(status_update, clear_jlmessage))
        self.dp.add_handler(MessageHandler(ftext, clear_tmessage))
        self.dp.add_error_handler(self.error)
        self.updater.start_polling()
        self.updater.idle()
