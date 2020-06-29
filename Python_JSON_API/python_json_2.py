import requests
import urllib.request
import http.client
import json

url ='https://www.baidu.com/'
r = requests.get(url)
#json格式
json_response = r.content.decode()

#json 转字典
dict_json = json.loads(json_response)
print(dict_json)
print('---------------------------')
# 将字典转换成json字符串
str_json =json.dumps(dict_json)
print(str_json)