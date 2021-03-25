# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 18:03

from __init__ import *
import sys,time
from PySide2.QtCore import Signal,QObject


class MySignal(QObject):

   progress_update = Signal(int)

class Bar:

    def __init__(self,q):
        # 使用Signal信号在新线程中修改主线程中的内容
        self.updataBar = MySignal()
        self.updataBar.progress_update.connect(self.setProgress)
        # 用于后续登陆
        self.flag_login = 0
        # 将登陆成功标识，存入队列，供后续使用
        self.q = q

        self.ui = QUiLoader().load('../UI/Progress.ui')
        self.ui.setWindowTitle('正在登录')
        # self.bankLock = Lock()

        self.ui.show()


    def ChangeValue(self):
        # self.bankLock.acquire()
        for i in range(0, 101, 10):
            # 这里创建发射信号，等待信号处理函数执行完需要花费时间，需要等待才会看到修改后进度条的值
            self.updataBar.progress_update.emit(i)
            time.sleep(0.1)
        # self.bankLock.release()

    def AnimalBar(self):
        thread1 = Thread(target=self.ChangeValue)
        thread1.start()

    # 处理进度的slot函数
    def setProgress(self,value):
        self.ui.LoginProgress.setValue(value)
        if self.ui.LoginProgress.value() == 100:
            self.flag_login = 1
            self.q.put(self.flag_login)
            # print("Login Successful")
            # QMessageBox.information(self.ui, '登录成功', "正在准备界面，请稍等...")
            self.ui.close()


def BarInstance(q):
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    bar = Bar(q)
    bar.AnimalBar()
    sys.exit(app.exec_())



if __name__ == '__main__':

    q1 = mp.Queue(10)

    # 重新开启进程，运行进度条界面
    process1 = mp.Process(target=BarInstance, args=(q1,))
    process1.start()
    process1.join()
    print(q1.get())



