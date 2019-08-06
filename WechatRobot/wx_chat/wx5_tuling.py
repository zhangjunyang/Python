#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
from wxpy import *

# 实例化，并登录微信
bot = Bot(cache_path=True)

# 调用图灵机器人API
tuling = Tuling(api_key='9d1d9486f8ca4663bc508afc9799f05e')

@bot.register()

def auto_reply(msg):

    tuling.do_reply(msg)

embed()

# 让机器人与所有好友聊天
