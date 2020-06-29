#1）字典序列化：
import json
dic={"name":"mcw","age":18}
xu=json.dumps(dic)
print(xu,type(xu),type(dic))

print('------------1---------------')

#2）列表序列化与反序列化：
import json
li=[1,2]
xu=json.dumps(li)
print(xu,type(xu),type(li))
fx=json.loads(xu)
print(fx,type(fx))
print('-------------2--------------')

#3）字符串序列化与反序列化:
import json
mcwstr="xiaoma"
xu=json.dumps(mcwstr)
print(xu,type(xu),type(mcwstr))
fx=json.loads(xu)
print(fx,type(fx))
print('------------3---------------')

#4）整型序列化与反序列化
import json
mcwint=2
xu=json.dumps(mcwint)
print(xu,type(xu),type(mcwint))
fx=json.loads(xu)
print(fx,type(fx))

print('------------4---------------')
#5）浮点型序列化与反序列化
import json
mcwfloat=2.03
xu=json.dumps(mcwfloat)
print(xu,type(xu),type(mcwfloat))
fx=json.loads(xu)
print(fx,type(fx))
print('--------------5-------------')

#6）布尔型序列化与反序列化：
import json
mcwbool=True
xu=json.dumps(mcwbool)
print(xu,type(xu),type(mcwbool))
fx=json.loads(xu)
print(fx,type(fx))

print('--------------6-------------')

#7）None序列化与反序列化
import json
mcwnone=None
xu=json.dumps(mcwnone)
print(xu,type(xu),type(mcwnone))
fx=json.loads(xu)
print(fx,type(fx))