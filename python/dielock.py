import time
from threading import Thread, Lock, RLock


def eat1(noodle_lock, fork_lock, name):
    noodle_lock.acquire()
    print(name, '拿到了面')
    fork_lock.acquire()
    print(name, '拿到了叉子')
    time.sleep(1)
    print(name, '吃到了面')
    fork_lock.release()
    noodle_lock.release()
    print(name, '放下了面')
    print(name, '放下了叉子')


def eat2(noodle_lock, fork_lock, name):
    fork_lock.acquire()
    print(name, '拿到了叉子')
    noodle_lock.acquire()
    print(name, '拿到了面')
    print(name, '吃到了面')
    noodle_lock.release()
    print(name, '放下了面')
    fork_lock.release()
    print(name, '放下了叉子')


name_list1 = ['特斯拉', '牛顿']
name_list2 = ['法拉第', '爱迪生']
"""
互斥锁造成死锁
"""
# noodle_lock = Lock()
# fork_lock = Lock()
"""
递归锁解决死锁问题
"""
noodle_lock=fork_lock  = RLock()

for i in name_list1:
    t = Thread(target=eat1, args=(noodle_lock, fork_lock, i))
    t.start()
for i in name_list2:
    t = Thread(target=eat2, args=(noodle_lock, fork_lock, i))
    t.start()
