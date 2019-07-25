__Author__ = "noduez"
'''使用threading模块'''
'''创建Thread的实例，传给他一个函数'''

import threading
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('Starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,
                             args=(i, loops[i]))
        threads.append(t)

    for i in nloops:        # start threads
        threads[i].start()

    for i in nloops:        # wait for all
        threads[i].join()   # threads to finish

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
