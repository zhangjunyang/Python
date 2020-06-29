import requests
# url ='http://api.map.baidu.com/telematics/v3/weather?location=shanghai&output=json&ak=3p49MVra6urFRGOT9s8UWr2'
url ='https://www.baidu.com/'
r = requests.get(url)
#json格式
json_response = r.content.decode()
print(json_response)


