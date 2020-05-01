import re
import logging
import time
import datetime
from telegram import ChatPermissions

def cao(bot, update):
	
    cao_message = update.message.reply_to_message
    print("cao_message=%s" % cao_message)

    if update.message.chat.type == 'private':
        text = '此命令在私聊中不可用'
        bot.send_message(update.message.chat_id, text)
        return

    if not cao_message:
        bot.delete_message(update.message.chat_id, update.message.message_id)
        return
    try: 
        chat_member = bot.get_chat_member(update.message.chat_id, cao_message.from_user.id)
        print("chat_member=%s" % chat_member)
        until_date1 = chat_member.until_date
        print("until_date1=%s" % until_date1)

        if  until_date1 != None :
            now_stamp = time.time()
            local_time = datetime.datetime.fromtimestamp(now_stamp)
            utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
            offset = local_time - utc_time
            print("offset=%s" % offset)
            until_date2 = until_date1 + offset
            
            a = until_date2.timetuple()           
            until_date3 = time.mktime(a)
            print("until_date2=%s" % until_date2)
            if until_date3 == -28800.0 or until_date3 == 0:
                print("1 until_date3=%s" % until_date3)
                text = '【{}】 再被【{}】禁言1分钟！'.format(cao_message.from_user.name,update.effective_user.name)
                bot.send_message(update.message.chat_id, text)

                bot.restrict_chat_member(
                update.message.chat_id,
                cao_message.from_user.id,
                until_date=int(time.time()+60),
                permissions=ChatPermissions(
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_polls=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False))
            else:
                print("3 until_date3=%s" % until_date3)
                b=int(until_date3+60)
                print("b=%s" % b)
                text = '【{}】 再被【{}】禁言1分钟！'.format(cao_message.from_user.name,update.effective_user.name)
                bot.send_message(update.message.chat_id, text)

                bot.restrict_chat_member(
                update.message.chat_id,
                cao_message.from_user.id,
                until_date=b,
                permissions=ChatPermissions(
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_polls=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False))
                
        else:

            text = '【{}】被 【{}】禁言1分钟！'.format(cao_message.from_user.name,update.effective_user.name)
            bot.send_message(update.message.chat_id, text)

            bot.restrict_chat_member(
            update.message.chat_id,
            cao_message.from_user.id,
            until_date=int(time.time()+60),
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False))

    except Exception as e:
        logging.error(e)
