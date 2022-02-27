import requests,urllib
from bs4 import BeautifulSoup
import time,random
url = "https://www.shicimingjv.com/bookindex/27.html"
header={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
res = requests.get(url=url,headers=header)
#实例化beautifulsoup对象
print(res.text)
bs = BeautifulSoup(res.text,'lxml')
#通过css查到元素
book_list = bs.select('.book-tags > li > a')
# #通过find_all选取,返回值为字符串
# bl= bs.find_all('ul',class_='book-tags')
# print("find_all的返回值{},值为{}".format(type(bl),bl))
print(book_list)
for i in book_list:
    #获取诗歌名称
    title = i.string
    #获取详情链接
    detail_url= i['href']
    #跳转诗歌详情页
    deres = requests.get(url=detail_url,headers=header).text
    dbs = BeautifulSoup(deres,'lxml')
    #获取诗歌详情
    detail= dbs.find('div',class_="entry-content clearfix").find_all('p')
    detail_text=""
    for d in detail:
        detail_text+=d.get_text()
    print(title)
    print(detail_text)
