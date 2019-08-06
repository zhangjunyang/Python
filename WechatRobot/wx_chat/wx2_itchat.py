#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
import itchat

itchat.auto_login(hotReload=True)
# 注意实验楼环境的中文输入切换
itchat.send(u'测试消息发送', 'filehelper')

