# coding=UTF-8
import logging

def findid(bot, update,args):
    chat_id = update.message.chat_id
    rmessage=update.message.reply_to_message
    if len(args) == 0:
        try:
            if rmessage:
                text = '【{}】,查到【{}】的ID号码为【{}】'.format(update.effective_user.name,rmessage.from_user.name,rmessage.from_user.id)
                bot.send_message(chat_id, text,parse_mode='HTML',disable_web_page_preview=True)
            else:
                text = '【{}】你的ID号码为【{}】'.format(update.message.from_user.name,update.message.from_user.id)
                bot.send_message(chat_id, text,parse_mode='HTML',disable_web_page_preview=True)
        except Exception as e:
            logging.error(e)
    else:
        print("args0=%s" % args[0])
        arg = args[0]
        try:
            member = bot.get_chat_member(chat_id, arg, timeout=60)
            print(member.user)
            text = 'ID为【{}】的用户名字是【{}】'.format(arg,member.user.name)
            bot.send_message(chat_id, text,parse_mode='HTML',disable_web_page_preview=True)
        except Exception as e:
            text = e            
            bot.send_message(chat_id,str(text))

