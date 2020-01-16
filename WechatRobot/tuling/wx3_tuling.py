#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
import wxpy 

# 实例化，并登录微信
bot = Bot(cache_path=True)

# 查找到要使用机器人来聊天的好友
my_friend = ensure_one(bot.search(u'好友名字'))

# 调用图灵机器人API
tuling = Tuling(api_key='9d1d9486f8ca4663bc508afc9799f05e')

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

embed()
