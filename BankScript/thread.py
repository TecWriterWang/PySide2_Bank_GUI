# -*- coding: utf-8 -*-
# @Time    : 2020/6/26 13:18

# 从 threading 库中导入Thread类
from threading import Thread,Lock
import time

if __name__ == '__main__':

    print('主线程执行代码')
    start = time.time()

    # 线程锁，当前线程执行时，会添加锁，在加锁期间其他线程必须等当前线程执行完在才能开始
    # 函数中使用sleep时使用锁会导致程序运行时间增加，线程不加锁时同时运行，加锁后是串行运行，也就是阻塞运行
    thLock = Lock()

    # 定义一个函数，作为新线程执行的入口函数
    def threadFunc(index,arg1,arg2):
        # 申请线程锁
        thLock.acquire()
        print('子线程{0} 开始,线程函数参数是：{1}\t{2}'.format(index,arg1, arg2))
        time.sleep(0.1)
        print('子线程{0} 结束'.format(index))
        # 释放线程锁
        thLock.release()


    # 创建 Thread 类的实例对象， 并且指定新线程的入口函数
    thread1 = Thread(target=threadFunc,daemon=True,
                    args=(1,100, 101)
                    )
    thread2 = Thread(target=threadFunc,
                    args=(2,200, 201)
                    )
    thread3 = Thread(target=threadFunc,
                    args=(3,300, 301)
                    )
    thread4 = Thread(target=threadFunc,
                    args=(4,400, 401)
                    )

    # 执行start 方法，就会创建新线程，
    # 并且新线程会去执行入口函数里面的代码。
    # 这时候 这个进程 有两个线程了。
    thread1.start()
    # thread1.join()
    thread2.start()
    # thread2.join()
    thread3.start()
    # thread3.join()
    thread4.start()
    # thread4.join()

    # 主线程的代码执行 子线程对象的join方法，就会等待当前子线程结束，才继续执行下面的代码

    # 不使用join方法就会主线程先结束，然后子线程在结束，
    # 最后整个进程结束(可以使用deamon=true的方式让主线程结束，程序就结束)

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    end = time.time()
    print(f'主线程结束,一共耗时{end-start}s')
