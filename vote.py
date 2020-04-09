# coding=UTF-8
import logging
import time
#from pyrogram import ChatPermissions

from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ChatPermissions

class KickUser(object):
    def __init__(self, message):
        self.message_id = message.message_id
        self.chat_id = message.chat_id
        self.user_id = message.from_user.id
        self.fullname = message.from_user.full_name
        self.username = message.from_user.username
        self.name = message.from_user.name
        self.agree = []
        self.disagree = []
        self.mutetime2 = 0
        self.chatmembers = 0
        self.karg = ''
        self.ktext = ''
        
    def add_agree(self, user):
        if user.id in self.vote_user():
            return False
        self.agree.append(user.id)
        return True

    def add_disagree(self, user):
        if user.id in self.vote_user():
            return False
        self.disagree.append(user.id)
        return True

    def agree_counter(self):
        return len(self.agree)

    def disagree_counter(self):
        return len(self.disagree)
    
    def get_karg(self,arg):
        self.karg = arg
        print("self.karg=%s" % self.karg)
        return (self.karg)
    
    def get_ktext(self,text):
        self.ktext = text
        print("self.ktext=%s" % self.ktext)
        return (self.ktext)        
    
    def get_mutetime2(self,time):
        print("time=%s" % time)
        self.mutetime2 = time
        return (self.mutetime2)

    def get_chatmembers(self,members):
        print("members=%s" % members)
        self.chatmembers = members
        return (self.chatmembers)

    def vote_counter(self):
        return self.agree_counter()+self.disagree_counter()

    def vote_user(self):
        return self.agree + self.disagree
    

    def log(self):
        return "{},{},{},{}".format(self.user_id, self.name, self.agree_counter(), self.disagree_counter())


class KickUsers():
    def __init__(self):
        self.kickusers = {}

    def get_kickuser(self, key):
        return self.kickusers.get(key)

    def save_kickuser(self, key, kickuser):
        self.kickusers[key] = kickuser

    def remove_kickuser(self, key):
        if self.kickusers.get(key):
            self.kickusers.pop(key)
    def votetime(self, vtime):
        for i in range(61):
            time.sleep(1)
            vtime=i
            print('time=%s' % vtime)
            return vtime
    

    def log(self):
        ret = ''
        for key in self.kickusers:
            ret += '{},{}\n'.format(key, self.kickusers.get(key).log())
        return ret[:-1]


kickusers = KickUsers()


def menu_keyboard(key, agree, disagree):
    menu = [[InlineKeyboardButton('支持 - {}'.format(agree), callback_data='agree {}'.format(key))],
            [InlineKeyboardButton('反对 - {}'.format(disagree), callback_data='disagree {}'.format(key))]]
    return InlineKeyboardMarkup(menu)


def delete_keyboard(key):
    delete = [[InlineKeyboardButton(
        '删除', callback_data='delete {}'.format(key))]]
    return InlineKeyboardMarkup(delete)


def fuck(bot, update,args):    
    print("bot=%s" % bot)
    #print("update=%s" % update)

    mutetime1=60*8
    #mutetime1=args[0]
    kick_message = update.message.reply_to_message
    if update.message.chat.type == 'private':
        text = '此命令在私聊中不可用'
        bot.send_message(update.message.chat_id, text)
        return

    if not kick_message:
        bot.delete_message(update.message.chat_id, update.message.message_id)
        return

    kick_user = KickUser(kick_message)
    if len(args) == 0:
        arg = 'h'
        kick_user.get_karg(arg)
    else:
    	print("args0=%s" % args[0])
    	arg = args[0]
    	kick_user.get_karg(arg)

    print("kick_user.karg=%s" % kick_user.karg)
    if kick_user.karg == 'd':
        mutetime2 = 86400
        chatmembers = 50
        text = "一天"
        kick_user.get_ktext(text) 
        kick_user.get_mutetime2(mutetime2)        
        kick_user.get_chatmembers(chatmembers)
    elif kick_user.karg == 'm':
        mutetime2 = 2592000
        chatmembers = 10
        text = "一月"
        kick_user.get_ktext(text) 
        kick_user.get_mutetime2(mutetime2)        
        kick_user.get_chatmembers(chatmembers)
    elif  kick_user.karg == 'f':
        mutetime2 = 6
        chatmembers = 2
        text = "永久"
        kick_user.get_ktext(text) 
        kick_user.get_mutetime2(mutetime2)        
        kick_user.get_chatmembers(chatmembers)
    else:
        mutetime2=3600
        chatmembers = 100
        text = "一小时"
        kick_user.get_ktext(text) 
        kick_user.get_mutetime2(mutetime2)        
        kick_user.get_chatmembers(chatmembers)
    print("mutetime2=%s" % mutetime2)
    
    if kick_user.user_id == bot.get_me().id:
    	text = '【{} {}】总有刁民想害朕!'.format(update.effective_user.name,kick_user.name)
    	bot.send_message(kick_user.chat_id,text)
    	bot.delete_message(kick_user.chat_id, update.message.message_id)
    	return

    key = str(kick_user.chat_id) + '-' + str(kick_user.user_id)
    print(key)
    try:
        bot.restrict_chat_member(
            kick_user.chat_id,
            kick_user.user_id,
            until_date=int(time.time()+mutetime1),
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False)     
        )
    except BaseException as e:
        logging.error(e)
        text = '【{} {}】刚才发生了什么？'.format(bot.effective_user.name,kick_user.name)
        bot.send_message(kick_user.chat_id, text)
        bot.delete_message(kick_user.chat_id, update.message.message_id)
        return
    try:
##        if 'job' in context.chat_data:
##            old_job = context.chat_data['job']
##            old_job.schedule_removal()
##        new_job = context.job_queue.run_once(alarm, due, context=chat_id)
##        context.chat_data['job'] = new_job     

        base_text = '正在投票禁言群成员【{} {} 】  {}.\n产生投票结果前，该用户被禁言8分钟，请尽快投票！\n'.format(kick_user.name,kick_user.user_id,kick_user.ktext)

        kickusers.save_kickuser(key, kick_user)

        bot.delete_message(update.message.chat_id, update.message.message_id)

        logging.info(kick_user.log())


        bot.send_message(
            chat_id=kick_user.chat_id,
            text=base_text,
            #timeout=60,
            reply_markup=menu_keyboard(key, kick_user.agree_counter(), kick_user.disagree_counter())
        )
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /fuck <seconds>')

    
   
def vote(bot, update):
        query = update.callback_query
        print("query=%s" % query)
        msg = query.message
        cmd = query.data.split(' ')[0]
        key = query.data.split(' ')[1]

        kick_user = kickusers.get_kickuser(key)
        print("vmutetime2=%s" % kick_user.mutetime2)
        print("vchatmembers=%s" % kick_user.chatmembers)
       
        allmembers = bot.get_chat_members_count(kick_user.chat_id)
        try:
            max_vote = int(allmembers/kick_user.chatmembers)
            if max_vote <= 2:
                max_vote = 3
            else:
                max_vote = int(allmembers/kick_user.chatmembers)
                
        except Exception as e:
            logging.error(e)
            
        print('allmembers=%s' % allmembers)
        print('max_vote=%s' % max_vote)


        if not kick_user:
            try:
                bot.delete_message(msg.chat_id, msg.message_id)
                bot.answer_callback_query(query.id, "此投票已过期，清理成功")
            except:
                bot.answer_callback_query(query.id, "超出Bot控制范围，请联系非Bot管理员")
            return

        if cmd == 'delete':
            try:
                bot.delete_message(msg.chat_id, msg.message_id)
            except:
                bot.answer_callback_query(query.id, "超出Bot控制范围，请联系非Bot管理员")

            if kick_user and kick_user.agree_counter() > max_vote//2:
                try:
                    bot.delete_message(kick_user.chat_id, kick_user.message_id)
                except:
                    bot.answer_callback_query(query.id, "被举报消息已被删除或超出Bot控制范围")
            if key:
                kickusers.remove_kickuser(key)
            return

        if kick_user.vote_counter() >= max_vote:
            return

        base_text = '正在投票禁言群成员【{} {} 】  {}.\n产生投票结果前，该用户被禁言8分钟，请尽快投票！\n'.format(kick_user.name,kick_user.user_id,kick_user.ktext)

        if  kick_user.vote_counter() < max_vote:
        
            #i = 1
            ret_agree = True
            ret_disagree = True
            if cmd == 'agree':
                ret_agree = kick_user.add_agree(query.from_user)
            else:
                ret_disagree = kick_user.add_disagree(query.from_user)

            if not (ret_agree and ret_disagree):
                bot.answer_callback_query(query.id, "请勿重复投票")
                return
            else:
                bot.answer_callback_query(query.id, "投票成功")
                bot.delete_message(chat_id=msg.chat.id,message_id=msg.message_id)
                bot.send_message(
                    chat_id=msg.chat_id,
                    text=base_text,
                    #timeout=60,
                    reply_markup=menu_keyboard(key, kick_user.agree_counter(), kick_user.disagree_counter()))

                 
            
            logging.info(kick_user.log())
##            print('ktime=%s' % kickusers.votetime(vtime))
##                      
##            if kickusers.votetime(vtime) == 60:
##                bot.delete_message(chat_id=msg.chat.id,message_id=msg.message_id)
##                bot.send_message(
##                    chat_id=msg.chat_id,
##                    text='投票禁言群成员【{}】.\n时间到，人数不够，投票失效！\n'.format(kick_user.name),
##                    reply_markup=delete_keyboard(key))
                    

            if kick_user.vote_counter() == max_vote:
                if kick_user.agree_counter() > kick_user.disagree_counter():
                    text = '经投票,同意禁言【{} {} 】 {}'.format(kick_user.name,kick_user.user_id,kick_user.ktext)
                    #bot.kick_chat_member(kick_user.chat_id, kick_user.user_id)
                    bot.restrict_chat_member(
                        kick_user.chat_id,
                        kick_user.user_id,
                        permissions=ChatPermissions(
                            can_send_messages=False,
                            can_send_media_messages=False,
                            can_send_polls=False,
                            can_send_other_messages=False,
                            can_add_web_page_previews=False,
                            can_change_info=False,
                            can_invite_users=False,
                            can_pin_messages=False),
                        until_date=int(time.time()+kick_user.mutetime2)
                        )
                else:
                    text = '经投票,不同意禁言【{} {}】,已恢复该用户所有权限'.format(kick_user.name,kick_user.user_id)
                    bot.restrict_chat_member(
                        kick_user.chat_id,
                        kick_user.user_id,
                        permissions=ChatPermissions(can_send_messages=True,can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True,can_send_polls=True)
                    )

    ##            bot.edit_message_text(
    ##                message_id=msg.message_id,
    ##                chat_id=msg.chat.id,
    ##                text=text,
    ##                reply_markup=delete_keyboard(key))
                

                bot.send_message(
                    chat_id=msg.chat_id,
                    text=text,
                    #timeout=60,
                    reply_markup=delete_keyboard(key))

                

# 绑定kick,当有人点击kick时,返回投票窗口
# dispatcher.add_handler(CommandHandler('kick', kick))
# dispatcher.add_handler(CallbackQueryHandler(vote))
