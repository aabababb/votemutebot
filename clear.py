import re
import logging
import time
from telegram import ChatPermissions,ChatMember,Update
from telegram.ext import CallbackContext

def clear_tmessage(update: Update, context: CallbackContext):
    try:        
        print("fupdate=%s" % update)
        if update.message != None:
            update.messages = update.message
        else:
            update.messages = update.edited_message
        ltext=len(update.messages.text)
        #print("ChatMember=%s" % update.ChatMember)
        print("ltext=%s" % ltext)
        tnum1 = re.search("\d{8}",update.messages.text)
        print("tnum1=%s" % tnum1)
        qtext = re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+',update.messages.text,re.S)   #只要字符串中的中文，字母，数字
        qtext = "".join(qtext)
        print("qtext=%s" % qtext)
        tnum2 = re.search("\d{9}",qtext)
        print("tnum2=%s" % tnum2)
        fname = update.messages.from_user.first_name
        fnum = re.search("\d{8}",fname)
        strname = 0
        try:
            lname = update.messages.from_user.last_name
            print("lname=%s" % lname)
            if lname != None:
                lnum = re.search("\d{8}",lname)
                print("lnum=%s" % lnum)
                strname=len(lname)
            else:
                lnum = None
                strname = 0
        except Exception as e:
            logging.error(e)
        try:
            uname = update.messages.from_user.username
            print("uname=%s" % uname)
            if  uname != None:
                unum = re.search("\d{8}",uname)
                print("unum=%s" % unum)
            else:
                unum = None
            
        except Exception as e:
            logging.error(e)
                
        if len(fname) > 30 or strname > 20 or fnum != None or lnum != None or unum != None:
            print("if-fname=%s" % fname)
            context.bot.kick_chat_member(update.messages.chat_id, update.messages.from_user.id,until_date=int(time.time()+60))
            text = '【{},{}】 名字有广告，被踢出！'.format(fname,lname)
            #bot.send_message(update.messages.chat_id, text)
            query = context.bot.send_message(update.messages.chat_id, text)
            message_id1=query.message_id
            print("send_message1=%s" % query)
            time.sleep(3)
            context.bot.delete_message(update.messages.chat_id,message_id1)            
        elif ltext > 666 or ltext == 1:
            print("if-ltext=%s" % ltext)
            context.bot.delete_message(chat_id=update.messages.chat_id,message_id=update.messages.message_id)
            context.bot.restrict_chat_member(
                update.messages.chat_id,
                update.messages.from_user.id,
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
            text = '【{}】 刷屏，禁言1小时'.format(update.messages.from_user.name)
            context.bot.send_message(update.messages.chat_id, text)
        elif tnum1 != None or tnum2 != None:
            print("if-tnum1=%s" % tnum1)
            context.bot.delete_message(chat_id=update.messages.chat_id,message_id=update.messages.message_id)
            context.bot.restrict_chat_member(
            update.messages.chat_id,
            update.messages.from_user.id,
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
            text = '【{}】 乱发广告，禁言8小时'.format(update.messages.from_user.name)
            context.bot.send_message(update.messages.chat_id, text)
    except Exception as e:
        logging.error(e)


def clear_jlmessage(update: Update, context: CallbackContext):
    try: 
        context.bot.delete_message(chat_id=update.messages.chat_id,message_id=update.messages.message_id)
        if update.message != None:
            update.messages = update.message
        else:
            update.messages = update.edited_message       
        fname = update.messages.from_user.first_name
        fnum = re.search("\d{8}",fname)
        strname = 0
        try:
            lname = update.messages.from_user.last_name
            print("lname=%s" % lname)
            if lname != None:
                lnum = re.search("\d{8}",lname)
                print("lnum=%s" % lnum)
                strname=len(lname)
            else:
                lnum = None
                strname = 0
        except Exception as e:
            
            logging.error(e)
        try:
            uname = update.messages.from_user.username
            print("uname=%s" % uname)
            if  uname != None:
                unum = re.search("\d{8}",uname)
                print("unum=%s" % unum)
            else:
                unum = None
        except Exception as e:
            logging.error(e)
                
        if len(fname) > 30 or strname > 20 or fnum != None or lnum != None or unum != None:
            print("if-fname2=%s" % fname)
            context.bot.kick_chat_member(update.messages.chat_id, update.messages.from_user.id,until_date=int(time.time()+60))
            text = '【{},{}】 名字有广告，被踢出！'.format(fname,lname)
            #bot.send_message(update.messages.chat_id, text)
            query = context.bot.send_message(update.messages.chat_id, text)
            message_id1=query.message_id
            print("send_message2=%s" % query)
            time.sleep(3)
            context.bot.delete_message(update.messages.chat_id,message_id1)
    except Exception as e:
        logging.error(e)
