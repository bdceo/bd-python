import requests

res = requests.get('https://www.baidu.com/')
print(res)
print(res.text)
print(res.encoding)
res.encoding = 'UTF-8'
print(res.text)
print(res.status_code)

print(res.headers)

