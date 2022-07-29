import requests,re


def get_one_page(offest):
    base_url = "https://www.maoyan.com/board/6?timeStamp=1656684681874&channelId=40011&index=2&signKey=9524d8521ebaa61b4716dfd84f14f21b&sVersion=1&webdriver=false"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

    param = {
        "offest":offest,
    }
    try:
        res =requests.get(url=base_url,headers=headers,params=param)
        if res.status_code == 200:
            return res.text
    except Exception as e:
        print(e)

def main(offest):
    html=get_one_page(offest)
    print(html)

if __name__ =="__main__":
    main(0)