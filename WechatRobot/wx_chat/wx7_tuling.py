from wxpy import *
bot = Bot(cache_path=True)
my_friend = bot.friends().search('好友昵称')[10] #定位好友
my_friend.send('Hello！') #发送“Hello！”测试一下对接是否成功。
group = bot.groups().search('群名')[10] #定位群

#接入图灵api：需要去下述网址申请：
tuling = Tuling(api_key='9d1d9486f8ca4663bc508afc9799f05e')

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
