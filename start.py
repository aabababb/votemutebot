# coding=UTF-8
def start(bot, update):
    chat_id = update.message.chat_id
    text = '欢迎使用，玩的开心\n'
    text += '回复想要被投票的成员发送的消息，回复内容为 /fuck d 禁言一天 \n 其他参数有 \n h 一小时（默认）投票人数 1/100 \n d 一天  投票人数 1/50 \n m 一个月 投票人数 1/10 \n f 永久 投票人数 1/2 \n'
    text += '此机器人附带删除入群退群通知 ，不要忘记给权限哦\n'
    bot.send_message(chat_id, text,
                     parse_mode='HTML',
                     disable_web_page_preview=True)
