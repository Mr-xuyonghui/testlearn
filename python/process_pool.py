from multiprocessing import Pool
import os, time
"""
使用multiprocessing实现多进程池
"""

def work(n):
    print('%s run' % os.getpid())
    time.sleep(2)
    return n ** 2


def after_work(n):
    print("回调函数：", n)


if __name__ == '__main__':
    p = Pool(3)
    res_l = []
    """同步调用"""
    # for i in range(5):
    #     res = p.apply(work,args=(i,))
    #     res_l.append(res)
    # print(res_l)
    """异步调用"""
    for i in range(5):
        res = p.apply_async(work, args=(i,), callback=after_work)
        res_l.append(res)
    p.close()
    p.join()
    print(res_l)
    print([res.get() for res in res_l])
