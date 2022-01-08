import urllib.request,urllib.parse
import ssl
from urllib.error import URLError,HTTPError
import re,json
# 全局取消证书验证
#https://www.maoyan.com/board/1?timeStamp=1641618052198&channelId=40011&index=4&signKey=bdbfb6a9451718880373fe5992489151&sVersion=1&webdriver=false
import requests

ssl._create_default_https_context = ssl._create_unverified_context
url = "http://www.santostang.com/"
header={
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
request = urllib.request.Request(url,headers=header)
try:
    #通过urllib抓取网页内容
    r =urllib.request.urlopen(request)
    #通过requests抓取网页内容
    #r =requests.get(url,headers=header)
    print(type(r))
except URLError as e:
    print(e)
except HTTPError as e:
    print(e)
else:
    print("Sucessfully")
    #print(str(r.read(),'utf-8'))

title_pattern = "<h4 .*>(.*?)<\/h4>"
regex = re.compile(r'<h4 .*>(.*?)</h4>')
#将urllib返回的 HTTPResponse对象转为字符串
re_str =str(r.read(),'utf-8')
#re_str = r.read().decode('utf-8')
#将requests返回的response转为文本
#re_str = r.text
title = regex.search(re_str)
#设置正则的匹配模式
title = re.search(title_pattern,re_str,flags=2)
title_1= re.findall(r"<p>(.*?)</p>",re_str)
print(title.group(1))
print(title_1)