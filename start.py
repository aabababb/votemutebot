# coding=UTF-8
def start(bot, update):
    chat_id = update.message.chat_id
    text = '欢迎使用，玩的开心\n'
    text += '回复想要被投票的成员发送的消息，回复内容为 /fuck \n'
    text += '此机器人附带删除入群退群通知 ，不要忘记给权限哦\n'
    bot.send_message(chat_id, text,
                     parse_mode='HTML',
                     disable_web_page_preview=True)
