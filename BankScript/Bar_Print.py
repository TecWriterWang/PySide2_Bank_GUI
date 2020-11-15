# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 13:01

# https://mp.weixin.qq.com/s?__biz=MzI0OTc0MzAwNA==&mid=2247489771&idx=2&sn=ca8071edd84ab418e168770a9d6b957b&chksm=e98d8b18defa020ed004f27ed1d13d4c34f09605a04d77823e3efb627cf0e303726d4e84d942&scene=126&sessionid=1601096439&key=bf5b07d1268a5d20d5d2c300479cf27b4003c614b28ffd468740b9731423c70e0017c102356715e4e7246179b122ff90aa880c8546156dbf436e63b8ebe155f8bceceffcd9e3422a1fb59f772403285703b43b21491cf894c17e7236a132d9ff6643b7dab01d19e3f941677e7ee6bd08c344914c083498879a22cc4bad51c099&ascene=1&uin=NjA3ODIyNDI1&devicetype=Windows+10+x64&version=62090529&lang=zh_CN&exportkey=A9gUJLkQq8mUlT%2BMd%2BF8eK0%3D&pass_ticket=8eJ%2BdTFLRk%2FR3AFv6KRPJdd%2BWjXrtgsjOmHt52nNdkrv50PPBZhpJLRClczoh7GF&wx_header=0
import sys
import time
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)

def progress_bar_A():
    scale = 50
    print("\n")
    print("执行开始，祈祷不报错".center(scale // 2, "-"))
    start = time.perf_counter()
    for i in range(scale + 1):
        a = "*" * i
        b = "." * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
        time.sleep(0.1)
    print("\n" + "执行结束，万幸".center(scale // 2, "-"))


progress_bar()
progress_bar_A()