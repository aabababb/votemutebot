import re

def clear_message(bot, update):
    bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)
                       
    name1 = update.message.from_user.name
    num = re.match("\d{8}",name1)
    
    if len(name1) > 20 or  num != None:
            
        bot.kick_chat_member(update.message.chat_id, update.message.from_user.id,until_date=60)
        text = '{} 名字有广告，被踢出！'.format(name1)
        bot.send_message(update.message.chat_id, text)
