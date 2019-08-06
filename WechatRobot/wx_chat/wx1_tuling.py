#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = '9d1d9486f8ca4663bc508afc9799f05e'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['小阳']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply


itchat.auto_login(hotReload=True)
# itchat.auto_login()
# itchat.auto_login(enableCmdQR=True)
itchat.run()

# 微信自动回复机器人
