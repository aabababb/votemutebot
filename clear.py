import re
import logging
import time
from telegram import ChatPermissions,ChatMember
def clear_tmessage(bot, update):
    try:        
        ltext=len(update.message.text)
        print("fupdate=%s" % update)
        #print("ChatMember=%s" % update.ChatMember)
        print("ltext=%s" % ltext)
        tnum1 = re.search("\d{8}",update.message.text)
        
        qtext = re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+',update.message.text,re.S)   #只要字符串中的中文，字母，数字
        qtext = "".join(qtext)
        print("qtext=%s" % qtext)
        tnum2 = re.search("\d{9}",qtext)
        
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
            text = '【{},{}】 名字有广告，被踢出！'.format(fname,lname)
            #bot.send_message(update.message.chat_id, text)
            query = bot.send_message(update.message.chat_id, text)
            message_id1=query.message_id
            print("send_message1=%s" % query)
            time.sleep(3)
            bot.delete_message(update.message.chat_id,message_id1)            
        if ltext > 666  or ltext == 1 :
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
            text = '【{}】 刷屏，禁言1小时'.format(update.message.from_user.name)
            bot.send_message(update.message.chat_id, text)
        if tnum1 != None:
            bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)
            bot.restrict_chat_member(
            update.message.chat_id,
            update.message.from_user.id,
            until_date=int(time.time()+3600*8),
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False))
            text = '【{}】 乱发广告，禁言8小时'.format(update.message.from_user.name)
            bot.send_message(update.message.chat_id, text)
        if tnum2 != None:
            bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)
            bot.restrict_chat_member(
                update.message.chat_id,
                update.message.from_user.id,
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


def clear_jlmessage(bot, update):
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
            bot.kick_chat_member(update.message.chat_id, update.message.from_user.id,until_date=int(time.time()+60))
            text = '【{},{}】 名字有广告，被踢出！'.format(fname,lname)
            #bot.send_message(update.message.chat_id, text)
            query = bot.send_message(update.message.chat_id, text)
            message_id1=query.message_id
            print("send_message2=%s" % query)
            time.sleep(3)
            bot.delete_message(update.message.chat_id,message_id1)
    except Exception as e:
        logging.error(e)
