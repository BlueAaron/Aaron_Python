# -*- coding: utf-8 -*- 
'''
Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。设置当前同时可以多少进程共存
'''
import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + "acquire");
    print i
    time.sleep(i)
    print(multiprocessing.current_process().name + "release\n");
    s.release()

if __name__ == "__main__":
    s = multiprocessing.Semaphore(1)
    for i in range(5):
        p = multiprocessing.Process(target = worker, args=(s, i*2))
        p.start()