# -*- coding: utf-8 -*- 
'''
不加daemon属性，主进程结果，子进程不结束
'''
import multiprocessing
import time

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print p.daemon
    print "end!"