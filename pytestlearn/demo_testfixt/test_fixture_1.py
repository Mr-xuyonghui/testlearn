import pytest
from selenium import webdriver


@pytest.fixture
def myfixture():
    # return "my first testfixture"
    driver = webdriver.Chrome()
    driver.get("https://www.zhihu.com/signin?next=%2F")


# 直接调用test fixture
def test_fix(myfixture):
    print("函数直接调用fixture")


# 类调用fixture函数
@pytest.mark.usefixtures('myfixture')
class Test_fixture():
    def test_01(self):
        print("类调用")

    # 通过 pytest.marrk.usefixtures调用
    @pytest.mark.usefixtures('myfixture')
    def test_fix_1(self):
        print("类方法直接调用fixture")


if __name__ == '__main__':
    pytest.main(['-s'])
