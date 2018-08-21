# -*- coding:utf-8 -*-
import itchat 
@itchat.msg_register(itchat.content.TEXT) 
def text_reply(msg): print msg.text xte=u"你是谁" 
retmsg=u“我TMD是机器人！别烦我！” 
if msg==xte: return retmsg
itchat.auto_login() 
itchat.run() 
