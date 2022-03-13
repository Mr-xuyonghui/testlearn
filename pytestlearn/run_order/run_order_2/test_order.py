import pytest

class Test_01():
    @pytest.mark.L1
    def test3(self):
        print("这是第03个测试用例")

    @pytest.mark.run(order=1)
    def test01(self):
        print("这是第01个测试用例")

    #@pytest.mark.run(order=2)
    @pytest.mark.L2
    def testz(self):
        print("这是第z个测试用例")


if __name__ == "__main__":
    pytest.main(['-s','-m L1 or L2'])
