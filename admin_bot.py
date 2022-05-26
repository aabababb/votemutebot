# coding=UTF-8
import logging
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler
from telegram import Update
from vote import fuck, vote,get_mutetime1
from clear import clear_jlmessage,clear_tmessage
from filters import status_update,ftext
from start import start
from findid import findid
from cao import cao


class AdminBot():
    def __init__(self, token1):
        self.updater = Updater(token=token1,use_context=True)
        print(self.updater)
        self.dp = self.updater.dispatcher
        print(self.dp)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    def error(self, update,context,error):
        try:
            context.bot.deleteWebhook()
            raise error
        except Exception as e:
            logging.error(e)

    def run(self,mutetime1):
        self.dp.add_handler(CommandHandler('start', start))
        self.dp.add_handler(CommandHandler('cao', cao))
        get_mutetime1(mutetime1)
        self.dp.add_handler(CommandHandler('fuck', fuck,pass_args=True))
        self.dp.add_handler(CommandHandler('findid', findid,pass_args=True))
        self.dp.add_handler(CallbackQueryHandler(vote))
        self.dp.add_handler(MessageHandler(status_update, clear_jlmessage))
        self.dp.add_handler(MessageHandler(ftext, clear_tmessage))
        self.dp.add_error_handler(self.error)
        self.updater.start_polling()
        self.updater.idle()
