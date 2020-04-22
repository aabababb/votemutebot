import re
import logging
def clear_message(bot, update):
    try:
        bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)
               
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
            bot.kick_chat_member(update.message.chat_id, update.message.from_user.id,until_date=int(60))
            text = '【{}】 名字有广告，被踢出！'.format(fname)
            bot.send_message(update.message.chat_id, text)
    except Exception as e:
        logging.error(e)
