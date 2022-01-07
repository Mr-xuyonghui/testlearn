import urllib.request
import ssl
# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

response = urllib.request.urlopen('http://www.baidu.com')
#获取所有响应信息
#print(response.read())
# #获取第一行响应信息
# print(response.readline())
# #获取指定行数响应信息，不传默认全部
# print(response.readlines(3))
#获取检索的url，判断是否重定向
print(response.geturl())
#获取网页的信息，http.client.HTTPMessage对象
print(type(response.info()))
print(response.status)
#获取所有头部信息，列表形式
print(response.getheaders())
#获取指定头部信息
print(response.getheader('Server'))