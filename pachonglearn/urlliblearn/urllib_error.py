import urllib.request
from urllib import error
import ssl
# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

"""访问不存在的url，测试urlerror"""
try:
    urllib.request.urlopen('http://www.i.com')
except error.URLError as e:
    print(e.reason)

"""捕获httperror"""
try:
    urllib.request.urlopen('http://www.i.htm')
except error.HTTPError as e:
    print(e.reason)
except error.URLError as e:
    print(e.reason)
else:
    print("successfully")