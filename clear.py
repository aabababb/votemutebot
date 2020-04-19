import re

def clear_message(bot, update):
    try:
        bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)
                           
        fname = update.message.from_user.first_name
        uname = update.message.from_user.username
        fnum = re.match("\d{8}",fname)
        unum = re.match("\d{8}",uname)
        
        if len(fname) > 30 or  fnum != None or unum != None:
                
            bot.kick_chat_member(update.message.chat_id, update.message.from_user.id,until_date=60)
            text = '{} 名字有广告，被踢出！'.format(fname)
            bot.send_message(update.message.chat_id, text)
    except Exception as e:
        logging.error(e)
