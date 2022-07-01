import urllib.request, urllib.parse, urllib.error
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# response = urllib.request.urlopen('http://www.baidu.com')
# 获取所有响应信息
# print(response.read())
# #获取第一行响应信息
# print(response.readline())
# #获取指定行数响应信息，不传默认全部
# print(response.readlines(3))
# #获取检索的url，判断是否重定向
# print(response.geturl())
# #获取网页的信息，http.client.HTTPMessage对象
# print(type(response.info()))
# print(response.status)
# #获取所有头部信息，列表形式
# print(response.getheaders())
# #获取指定头部信息
# print(response.getheader('Server'))

# 通过urlopen请求post方法的url
base_url = "https://weibo.com/ajax/statuses/mymblog?"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "cookie": "SUB=_2AkMW4hFff8NxqwJRmP8dy2rhaoV2ygrEieKgvuCEJRMxHRl-yT8XqlwatRB6PWI_sKu9uX4tY_bpSewU7uWd9MIE-mTM; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5o02B860_NVZ71C92I4uXW; SINAGLOBAL=1741345181483.1338.1639882345287; ULV=1639882345289:1:1:1:1741345181483.1338.1639882345287:; XSRF-TOKEN=oRnT2mviGP3E-8N4WO3uYsi_; WBPSESS=5fStQf4aE0d6e7rh9d-P6p_DO6wXn7m4TQKA0c9m5w7jaDFdS2ybwO4kJW8k4EvIOY0kBnkwJ1fOVWUNh9zp-Zsz21Gqhrfr_DoQiVBIjg_WFYVkPNMkKnmxzJGvBcim3J9W1WVARgs3Kz4jgnJn_RtCA0o12shYgFfC_SmQwH8=",
    "referer": "https://weibo.com/u/2118872917"
}
param = {
    "uid": 2118872917,
    "page": 2,
    "feature": 0
}
'''urllib的get请求参数需要用urlenconde之后，拼接到url上'''
url = base_url+urllib.parse.urlencode(param)
print(url)
# """将param转为字节流，先通过urlencode转为字符串，再通过bytes转为字节；"""
# data = bytes(urllib.parse.urlencode(param), encoding='utf8')
"""需要用到heaeder的话，需要通过request对象构建，再传入urlopen"""
req = urllib.request.Request(url=url,headers=header)

try:
    res = urllib.request.urlopen(req)
    '''获取请求的url'''
    # print(res.geturl())
    '''获取所有请求头'''
    # print(res.getheaders())
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("sucesssful")
    print(res.read().decode('utf8'))
