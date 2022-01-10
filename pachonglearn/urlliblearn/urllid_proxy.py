#! /usr/bin/env python3
import urllib.request

proxies = {
    'socks5': 'localhost:1080',
    'http': 'https://58.240.60.10:81',
    'https': 'https://127.0.0.1:3128'
}

proxy_handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('https://www.baidu.com')
print(response.read())
