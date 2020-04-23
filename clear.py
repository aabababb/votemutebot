import re
import logging
import time
from telegram import ChatPermissions
def clear_message(bot, update):
    try:        
        ltext=len(update.message.text)
        print("ftext=%s" % update.message)
        print("ftext=%s" % ltext)     
        fname = update.message.from_user.first_name
        fnum = re.search("\d{8}",fname)
        strname = 0
        lnum = None
        unum = None
        try:
            lname = update.message.from_user.last_name
            print("lname=%s" % lname)
            lnum = re.search("\d{8}",lname)
            print("lnum=%s" % lnum)
            strname=len(lname)
        except Exception as e:
            logging.error(e)
        try:
            uname = update.message.from_user.username
            print("uname=%s" % uname)
            unum = re.search("\d{8}",uname)
            print("unum=%s" % unum)
        except Exception as e:
            logging.error(e)
                
        if len(fname) > 30 or strname > 20 or fnum != None or lnum != None or unum != None:
            bot.kick_chat_member(update.message.chat_id, update.message.from_user.id,until_date=int(time.time()+60))
            text = '【{}】 名字有广告，被踢出！'.format(fname)
            bot.send_message(update.message.chat_id, text)
        if ltext > 666:
            bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)
            bot.restrict_chat_member(
                update.message.chat_id,
                update.message.from_user.id,
                until_date=int(time.time()+3600),
                permissions=ChatPermissions(
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_polls=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False))
            text = '【{}】 刷屏，禁言1小时'.format(fname)
            bot.send_message(update.message.chat_id, text)

    except Exception as e:
        logging.error(e)
