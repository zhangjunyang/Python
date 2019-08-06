#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
import itchat
import wxpy 

 bot = Bot()
 # api可直接用
 tuling = Tuling(api_key='9d1d9486f8ca4663bc508afc9799f05e')
 @bot.register(msg_types=TEXT)
 def auto_reply_all(msg):
  tuling.do_reply(msg)
 bot.join()

# 微信自动回复机器人
