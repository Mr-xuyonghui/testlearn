import pytest

class Test_01():
    def test9(self):
        print("这是run_order_01 09个测试用例")
    def test08(self):
        print("这是run_order_01 第08个测试用例")

    def testb(self):
        print("这是run_order_01 第b个测试用例")

if __name__ == "__main__":
    pytest.main()