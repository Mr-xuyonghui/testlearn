import requests
r= requests.get('http://www.baidu.com')
print(r)
#文本形式打印响应信息
print("文本形式响应信息",r.text)
#二进制形式打印响应信息
print("二进制响应信息：",r.content)
#获取响应头
print("响应头：",r.headers)
#获取响应cookies
print("响应头cookies:",r.cookies)
for key,value in r.cookies.items():
    print(key,value)
print("响应状态码：",r.status_code)
#获取请求头部信息
print("请求头所有信息：",r.request.headers)
#获取请求头部信息的Accept
print("请求头信息Accept：",r.request.headers["Accept"])
#获取请求头部cookies
print("请求头cookies：",r.request._cookies)