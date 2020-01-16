# -*- coding:utf-8 -*-
import itchat 
@itchat.msg_register(itchat.content.TEXT) 
def text_reply(msg): 
	print msg.text xte=u"你是谁" 
retmsg=u“我是机器人！” 
if msg==xte: 
	return retmsg
itchat.auto_login() 
itchat.run() 
