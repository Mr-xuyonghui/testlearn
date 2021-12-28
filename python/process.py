import time
import random
from multiprocessing import Process, Lock


# 直接创建，通过线程挑调用
def func(name):
    lock.acquire()
    s = random.randint(1, 5)
    print(f'func current process is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f' func process {name} is over')
    lock.release()
# 继承创建
class Func01(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # 重构实例方法run()，改成我们需要执行的函数
    def run(self):
        s = random.randint(1, 5)
        print(f'current process is {self.name}, sleeping {s}s.')
        time.sleep(s)
        print(f'process {self.name} is over')


if __name__ == '__main__':
    """定义互斥锁"""
    lock = Lock()
    for i in range(3):
        p1 = Process(target=func,args=('p'+str(i),))
        #p2 = Func01('p2')
        """将p1进程设置为主进程的守护进程"""
        #p1.daemon = True
        p1.start()
        #p2.start()
        """将p1进程设置为等到进程"""
        #p1.join()
    print('Main process')
