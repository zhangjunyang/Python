#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
import itchat
from itchat.content import*
import re
 
@itchat.msg_register([TEXT])
def text_reply(msg):
    print('msg:%s'%msg['Text'])
    match = re.search('',msg['Text']).span()
    print("~~~~~")
    if match:
        itchat.send('[自动回复]你好，微信测试中!',msg['FromUserName'])
 
#二维码
itchat.auto_login(hotReload=True)
itchat.run()

