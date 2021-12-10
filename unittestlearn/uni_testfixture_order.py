import unittest


def setUpModule():
    print("setUpModule 每个模块执行前执行一次")


def tearDownMoudle():
    print("tearDownMoudle 每个模块执行后执行一次")


class Test_fixture(unittest.TestCase):

    def setUp(self) -> None:
        print("setup 每个用例执行前执一次")

    def tearDown(self) -> None:
        print("teardown 每个用例执行完成之后执行一次")

    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass 测试类例执行前执一次，只执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass 测试类例执行完成之后执一次，只执行一次")

    def test_01(self):
        print("这是第一个测试用例")

    def test_02(self):
        print("这是第二个测试用例")


if __name__ == '__main__':
    unittest.main()
