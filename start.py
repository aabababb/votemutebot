# coding=UTF-8
def start(bot, update):
    chat_id = update.message.chat_id
    text = '欢迎使用，玩的开心\n'
    text += '回复想要被投票的成员发送的消息，回复内容为 [/fuck d] 禁言一天\n 其他参数有 \n h 一小时（默认）投票人数 1/100 \n d 一天  投票人数 1/50 \n w 一周  投票人数 1/30 \n m 一个月 投票人数 1/10 \n f 永久 投票人数 1/2 \n'
    text += '直接[/fuck d ID]命令，可以通过ID号来发起禁言投票！\n'
    text += '回复消息[/cao]命令，发起禁言每次1分钟，可累加！\n'
    text += '此机器人附带删除入群退群通知,\n检测用户名长度和数字，当广告踢出 ，\n长文本消息刷屏禁言1小时，联系方式广告禁言8小时 \n'
    text += '命令[/findid number] 通过ID找用户名字\n'
    text += '不要忘记给权限哦！\n'
    bot.send_message(chat_id, text,
                     parse_mode='HTML',
                     disable_web_page_preview=True)
