# -*- coding: utf-8 -*- 
'''
子进程结束后，主进程继续
'''
import multiprocessing
import time

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
#     p.daemon = True//只要join了，这个参数有没有都一样
    p.start()
    p.join()
    print "end!"