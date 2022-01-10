import requests

"""
微博个人主页通过ajax加载数据
"""
cookie = "SUB=_2AkMW4hFff8NxqwJRmP8dy2rhaoV2ygrEieKgvuCEJRMxHRl-yT8XqlwatRB6PWI_sKu9uX4tY_bpSewU7uWd9MIE-mTM; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5o02B860_NVZ71C92I4uXW; SINAGLOBAL=1741345181483.1338.1639882345287; ULV=1639882345289:1:1:1:1741345181483.1338.1639882345287:; XSRF-TOKEN=oRnT2mviGP3E-8N4WO3uYsi_; WBPSESS=5fStQf4aE0d6e7rh9d-P6p_DO6wXn7m4TQKA0c9m5w7jaDFdS2ybwO4kJW8k4EvIOY0kBnkwJ1fOVWUNh9zp-Zsz21Gqhrfr_DoQiVBIjg_WFYVkPNMkKnmxzJGvBcim3J9W1WVARgs3Kz4jgnJn_RtCA0o12shYgFfC_SmQwH8="

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "referer": "https://weibo.com/u/2118872917"
}
url = "https://weibo.com/ajax/statuses/mymblog"
param = {
    "uid": 2118872917,
    "page": 2,
    "feature": 0
}
# 初始化RequestsCookieJar对象
jar = requests.cookies.RequestsCookieJar()
c_l = cookie.split(";")
for c in c_l:
    key, value = c.split("=", 1)
    # 通过RequestsCookieJar对象set()设置cookies
    jar.set(key, value)
re = requests.get(url, params=param, headers=header, cookies=jar)
print(re.status_code)
print(re.json()["data"]["list"])
