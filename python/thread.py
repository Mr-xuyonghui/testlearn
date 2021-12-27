import time
import random
import threading
#直接创建，通过线程挑调用
def func(name):
    meta.acquire()
    s = random.randint(1, 5)
    print(f'current thread is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f'thread {name} is over')
    meta.release()
#继承创建
class Func01(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
#重构实例方法run()，改成我们需要执行的函数
    def run(self):
        s = random.randint(1, 5)
        print(f'current thread is {self.name}, sleeping {s}s.')
        time.sleep(s)
        print(f'thread {self.name} is over')

if __name__ == '__main__':
    meta = threading.Lock()
    for i in range(1, 5):
        t = threading.Thread(target=func, args=(i,))
        #守护线程，程序执行完成之后，强制停止线程
        t.setDaemon(True)
        t.start()
        #等待线程，需要等线程都执行完成，程序才会继续执行
        #t.join()
        # t1=Func01(str(i))
        # t1.start()
    print('Main Thread')