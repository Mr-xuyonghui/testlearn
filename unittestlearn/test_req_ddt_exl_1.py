import ast

from unittestlearn.request_class import Requestunitl
import unittest
from unittestlearn.openpyxl_class import ExlHander
from ddt import ddt,data,unpack


def exldata():
    exl = ExlHander(r'f:\useracount.xlsx')
    data_1 = exl.read_dict('Sheet1')
    return data_1


@ddt
class Testlogin(unittest.TestCase):
    def setUp(self) -> None:
        print("测试开始，准备数据")

    def tearDown(self) -> None:
        print("测试结束")

    @data(*exldata())
    def test_login(self,exldata):
        print(exldata)
        print(type(exldata['headers']))
        res =Requestunitl()
        #header必须是字典 eval()-转化为字典，ast.literal_eval()
        resdata=res._post(url=exldata['url'],data=exldata['data'],headers=ast.literal_eval(exldata['headers']))
        print(resdata.json())
        response=resdata.json()
        print(resdata.status_code)
        #断言需要提高，获取请头，响应体，响应头等需要提高
        self.assertEqual(resdata.status_code,exldata['expect'])
        self.assertEqual(response['result']['nickname'], exldata['expect_1'])
if __name__ == '__main__':
    unittest.main()


