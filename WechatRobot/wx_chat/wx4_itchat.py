import itchat
from itchat.content import TEXT
 
@itchat.msg_register
def simple_reply(msg):
    if msg['Type'] == TEXT:
        return 'I received: %s' % msg['Content']
itchat.auto_login()
itchat.run()

# 回复所有文本信息（包括群聊）
