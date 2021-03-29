# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 18:03

from __init__ import *
import sys,time
from PySide2.QtCore import Signal,QObject,Slot

from ui2py.Progress import *


class Bar(QObject):

    progress_update = Signal(int)

    def __init__(self,q):
        super().__init__()
        # print("process1.kill()2\n")
        # 使用Signal信号在新线程中修改主线程中的内容
        self.progress_update.connect(self.setProgress)

        # 用于后续登陆
        self.flag_login = 0
        # 将登陆成功标识，存入队列，供后续使用
        self.q = q

        self.ui = QUiLoader().load('../UI/Progress.ui')
        self.ui.setWindowTitle('正在登录')
        self.ui.show()
        self.AnimalBar()

        # self.ui = Ui_ProgressBar()
        # self.ui.setupUi(self)
        # self.show()
        # self.ChangeValue()

    def ChangeValue(self):
        # self.bankLock.acquire()
        for i in range(0, 101, 10):
            # 这里创建发射信号，等待信号处理函数执行完需要花费时间，需要等待才会看到修改后进度条的值
            self.progress_update.emit(i)
            time.sleep(0.5)
        # self.bankLock.release()

    def AnimalBar(self):
        thread1 = Thread(target=self.ChangeValue)
        thread1.start()

    # 处理进度的slot函数
    @Slot(int)
    def setProgress(self,value):
        self.ui.LoginProgress.setValue(value)
        if self.ui.LoginProgress.value() == 100:
            self.flag_login = 1
            self.q.put(self.flag_login)
            # print("Login Successful")
            # QMessageBox.information(self.ui, '登录成功', "正在准备界面，请稍等...")
            # self.deleteLater()
            self.ui.close()


def BarInstance(q):
    # print("{0}BarInstance Creat ok()\n".format(q))
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    bar = Bar(q)
    bar.AnimalBar()
    sys.exit(app.exec_())


if __name__ == '__main__':

    q1 = mp.Queue(10)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    bar = Bar(q1)
    sys.exit(app.exec_())

    # 重新开启进程，运行进度条界面
    # process1 = mp.Process(target=BarInstance, args=(q1,))
    # process1.start()
    # process1.join()
    # print(q1.get())



