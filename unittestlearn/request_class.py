import  requests
class Requestunitl():
    def __init__(self):
        #self.url = url
        #self.headers={"Content-Type":"application/json;charset=utf-8"}
        pass
    def _get(self,url,param,**kwargs):
        res = requests.get(url,params=param,**kwargs)
        return res
        #   {
        #     "responseheader" : res.headers,
        #     "responsebody" : res.json()
        # }

    def _post(self,url,data,json=None,**kwargs):
        res = requests.post(url,data=data,json=json,**kwargs)
        return res
        #     {
        #     "responseheader" : res.headers,
        #     "responsebody" : res.json()
        # }

if __name__ == '__main__':
    request =Requestunitl()
    result =request._post('https://api.s.suv666.com/iyourcar_news_suv/suv/news/related_jxwd/list',data={"artilce_online_id":"871611"})
    print(result)
    #获取响应状态码
    print("响应状态码:",result.status_code)
    #获取请求头部
    print("request-header：",result.request.headers)
    #获取请求头的cookies
    print("request-cookies：", result.request._cookies)
    #字符串化处理,二进制，json格式response
    print(result.text)
    print(result.content)
    print(result.json())
    #获取响应体头部
    print(result.headers)
    #获取响应体cookies
    print(result.cookies)
    Log=Log().logger()
    Log.info("rizhi")