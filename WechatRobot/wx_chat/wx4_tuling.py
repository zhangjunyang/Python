#!/usr/bin/enw python3
# -*- coding=utf-8 -*-
import itchat
import requests

def get_response(_info):
    print(_info)                                    
    api_url = 'http://www.tuling123.com/openapi/api'   
    data = {
        'key': '9d1d9486f8ca4663bc508afc9799f05e',     
        'info': _info,                               
        'userid': 'wechat-robot',                      
    }
    r = requests.post(api_url, data=data).json()       
    print(r.get('text'))                              
    return r

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return get_response(msg["Text"])["text"]

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)                  
    itchat.run()

