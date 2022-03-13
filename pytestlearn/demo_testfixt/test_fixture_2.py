import pytest


@pytest.fixture(params=[1, 2, 3],ids=['test1','test2','test3'])
def myfix(request):
    return request.param


def test_fix_2(myfix):
    print("直接调用fixture函数")
print(myfix)


# 通过 pytest.marrk.usefixtures调用带参数fixture
@pytest.mark.usefixtures('myfix')
def test_fix_1():
    print("类方法直接调用fixture")


if __name__ == '__main__':
    pytest.main(['-s','-k', 'fixture_2','-q'])
