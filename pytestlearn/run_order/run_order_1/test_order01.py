import pytest

class Test_01():
    def test4(self):
        print("这是run_order_1 第04个测试用例")
    def test5(self):
        print("这是 run_order_1 第05个测试用例")

    def testa(self):
        print("这是 run_order_1 第a个测试用例")

if __name__ == "__main__":
    pytest.main()