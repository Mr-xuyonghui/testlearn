import pytest
class Test_01():
    def test(self):
        print("这是run_oeder同级目录下的文件")

if __name__ == "__main__":
    pytest.main(['-s'])