import  requests
class Requestunitl():
    def __init__(self,url):
        self.url = url
        self.headers={"Content-Type":"application/json;charset=utf-8"}
    def _get(self,param,**kwargs):
        res = requests.get(self.url,param=param)
        return res

    def _post(self,data,json=None,**kwargs):
        res = requests.post(self.url,data=data,json=json)
        return res

if __name__ == '__main__':
    request =Requestunitl('https://api.s.suv666.com/iyourcar_news_suv/suv/news/related_jxwd/list')
    result =request._post(data={"artilce_online_id":"871611"})
    print(result.json())
