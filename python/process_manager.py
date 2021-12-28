from multiprocessing import Process, Lock, Manager


def manadata(data, lock):
    with lock:
        data['count'] -= 1


if __name__ == '__main__':
    data = {'count': 100}
    lock = Lock()
    with Manager() as m:
        """设置需要共享的数据"""
        dic = m.dict({'count': 100})
        print("原始数据",dic)
        p_l = []
        for i in range(100):
            p = Process(target=manadata, args=(dic, lock))
            p_l.append(p)
            p.start()
            """将每个子进程设置为等待进程"""
        for p in p_l:
            p.join()
        print("共享处理之后的数据",dic)
