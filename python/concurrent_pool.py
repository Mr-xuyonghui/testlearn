import random
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
def func(name):
    s = random.randint(1, 5)
    print(f'current thread is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f'thread {name} is over')


def func_01(name):
    s = random.randint(1, 5)
    print(f'current process is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f'process  {name} is over')

def mythread():
     t = ThreadPoolExecutor(max_workers=2)
     for i in range(1, 3):
         t.submit(func, i)

if __name__ == '__main__':
    """单独使用线程池"""
    # with ThreadPoolExecutor(max_workers=2) as t:
    #     for i in range(1, 3):
    #         t.submit(func, i)
    """单独使用进程池"""
    # with ProcessPoolExecutor(max_workers=2) as p:
    #     for i in range(1,4):
    #         p.submit(func_01,i)
    """
    进程池和线程同时使用
    开三个进程，同时每个进行里面开多个线程
    """

    with ProcessPoolExecutor(max_workers=2) as p:
        for i in range(1,3):
            p.submit(mythread)
