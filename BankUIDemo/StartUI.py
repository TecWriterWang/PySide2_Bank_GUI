# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 17:10

# 开始界面

from PySide2.QtCore import QThread,Signal,Slot
import multiprocessing_win
import multiprocessing


class StartUI(QThread):

    signal_startui_to_Merchantui = Signal()

    def __init__(self):
        super().__init__()

        self.ui = QUiLoader().load('../UI/Start.ui')
        self.ui.setWindowTitle('登录')
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.DB = Op_DB()


        # 起始界面跳转交易界面flag
        self.Start_to_MerchantUI_Falg = False
        self.signal_startui_to_Merchantui.connect(self.startui_to_Merchantui)

        self.account = None
        self.password = None


        # 状态栏
        self.status = QMainWindow.statusBar(self.ui)
        self.status.font()
        self.status.showMessage('欢迎使用MoreMoney账户管理系统')#,5000)

        # 设置密码输入框显示圆点
        self.ui.InPassword.setEchoMode(QLineEdit.Password)

        # 输入框提示文字 setText
        # self.ui.InAccount.setText('请输入账户名')
        # self.ui.InPassword.setText('请输入密码')

        # 设置控件的提示信息
        self.ui.btcheckAccount.setToolTip('检查当前用户是否可用')
        self.ui.InAccount.setToolTip("请输入银行卡号/手机号")
        self.ui.InPassword.setToolTip("请输入6位数字密码")
        # 文本框内容修改的Slot
        # self.ui.InAccount.textChanged.connect(self.checkAccount)

        # 按钮被点击的Slot
        self.ui.btcheckAccount.clicked.connect(self.checkAccount)
        self.ui.btLogin.clicked.connect(self.login)
        self.ui.btRegister.clicked.connect(self.register)
        self.ui.btUnLock.clicked.connect(self.Unlock)
        self.ui.btForgetPw.clicked.connect(self.ForgetPwd)

    def get_acc_pwd(self):
        # global account, password
        self.account = self.ui.InAccount.text()
        self.password = self.ui.InPassword.text()
        if(self.account and self.password):
            # print("请登录")
            # print("账户名:{0}\t\t密码:{1}".format(self.account,self.password))
            return True

        else:
            # print("账户名密码无效")
            QMessageBox.warning(self.ui,'操作失败','请输入有效账户和密码')
            return False


    def checkAccount(self):
        # sender = self.sender()
        # print(sender.text() + "按钮被按下")

        # 检测检查按钮被按下
        self.bt_check = 1
        self.account = self.ui.InAccount.text()
        if (len(self.account) == 0):
            QMessageBox.warning(self.ui, '操作失败', '当前账户输入为空，请输入有效账户')
        else:
            flag_check = self.DB.Login_queue(self.account, self.bt_check)

            # 从数据库中查询到当前账户名
            if flag_check[0]:
                QMessageBox.information(self.ui,'操作成功','当前账户可用')

            else:
                QMessageBox.warning(self.ui,'操作失败','当前账户不存在，请重新检查账户')

    @Slot()
    def startui_to_Merchantui(self):
        # print("process1.kill()1\n")

        # 使用队列存取线程中函数的返回值
        q1 = mp.Queue(10)
        # bar = Bar(q1)
        # bar.AnimalBar()

        # 重新开启进程，运行进度条界面
        global bar_process
        bar_process = mp.Process(target=BarInstance,args=(q1,))
        bar_process.daemon = True
        # print("{0}process1 Creat ok()\n".format(process1))
        bar_process.start()
        bar_process.join()
        # print("process1.kill()3\n")

        if q1.get():
            self.Start_to_MerchantUI_Falg = True
            # process1.kill()
            # print("process1.kill()\n")
        else:
            self.ui.show()


    # 多线程操作启用进度条窗口
    """注意使用继承QThread的方式无法在子线程中发射信号给主线程"""
    def run(self):
        self.signal_startui_to_Merchantui.emit()
        # self.LogToBar()
        # 账户密码正确后，先进入进度条，进度条跑完后关闭登录界面，进入交易界面
        # threadlogin = Thread(target=self.LogToBar())
        # threadlogin.start()

    def login(self):

        if self.get_acc_pwd():

            # self.account = self.ui.InAccount.text()
            # self.password = self.ui.InPassword.text()
            # if (self.account and self.password):#查找当前账户名对应的密码，这里密码使用hash加密
            #     QMessageBox.information(self.ui,'操作成功',"登录成功")
            #     self.Merchant()

            flag_login = self.DB.Login_queue(int(self.account),0,int(self.password))
            # 检查账户是否被冻结
            if flag_login == 'Lock':
                QMessageBox.warning(self.ui, '操作失败', "账户已被冻结，请先解冻")

            else:
                if len(flag_login)== 2:

                    if flag_login[0] is True and flag_login[1] is True:# 从数据库中查询当前账户名和密码，若查询到账户和密码，进入交易界面


                        self.ui.hide()
                        # self.start()
                        # 账户密码正确后，先进入进度条，进度条跑完后关闭登录界面，进入交易界面
                        threadlogin = Thread(target=self.LogToBar())
                        threadlogin.start()

                        while 1:
                            if self.Start_to_MerchantUI_Falg:
                                # 进度条走完进入后续界面
                                # print("Start_to_MerchantUI_Falg")
                                # bar_process.kill()
                                self.Merchant = MerchantUI(self.account)
                                self.Merchant.show()
                                self.ui.close()
                                break

                    else:
                        QMessageBox.warning(self.ui, '操作失败', "账户密码有误，请确认后登录")
                elif len(flag_login) == 1:
                    QMessageBox.about(self.ui, '操作失败', "账户不存在，请重新输入账户")


    # 跳转到注册界面
    def register(self):
        self.ui.close()
        self.DB.connection.close()
        self.RegUI = RegisterUI()
        self.RegUI.show()

    # 解冻账户
    def Unlock(self):
        Unlock_flag = False
        reply = QMessageBox.question(self.ui, u'警告', u'你要解冻账户吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            while 1:
                CardID, okPressed  = QInputDialog.getText(self.ui, "请输入你的卡号/手机号","CardID:",QLineEdit.Normal, "")
                if okPressed:
                    if re.compile(r"[0-9]*").fullmatch(CardID): # 检测卡号是否为纯数字
                        Name, okPressed = QInputDialog.getText(self.ui, "请输入你的用户名", "Name:", QLineEdit.Normal, "")
                        if okPressed:
                            if self.DB.queue_data(CardID, Name):
                                QMessageBox.information(self.ui, "Information",
                                                        "Your CardID is: <b>" + CardID + "</b>\nYour Name is：<b>" + Name + "</b>")
                                Unlock_flag = True
                                break # 卡号输入正确跳出循环
                            else:
                                QMessageBox.critical(self.ui, '信息有误', "请重新输入您的卡号和用户名")
                                continue
                        else:
                            break # 退出用户名对话输入框

                    else:
                        QMessageBox.critical(self.ui, '卡号有误', "卡号为11位数字")
                        continue

                else:
                    break # 退出CardID对话输入框
        else:
            pass # 忽略冻结账户对话框

        # 执行解冻操作
        if Unlock_flag:
            Status = self.DB.Freeze((CardID, Name, '', '解冻账户'), 1)
            if Status == -100:
                QMessageBox.information(self.ui, '操作失败', "您的账户未被解冻,无须解冻")
            elif Status[0] == 1 and Status[1] == 1:
                QMessageBox.information(self.ui, '操作成功', "账户已解冻,请登录...")

            else:
                QMessageBox.information(self.ui, '操作失败', "账户解冻失败")

    def ForgetPwd(self):
        ForgetPwd_flag = False
        reply = QMessageBox.question(self.ui, u'警告', u'你要修改密码吗?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            while 1:
                CardID, okPressed = QInputDialog.getText(self.ui, "请输入你的卡号/手机号", "CardID:", QLineEdit.Normal, "")
                if okPressed:
                    if re.compile(r"[0-9]*").fullmatch(CardID):  # 检测卡号是否为纯数字
                        Name, okPressed = QInputDialog.getText(self.ui, "请输入你的用户名", "Name:", QLineEdit.Normal, "")
                        if okPressed:
                            # 补充邮件验证密码方式
                            if self.DB.queue_data(CardID, Name):
                                QMessageBox.information(self.ui, "Information",
                                                        "Your CardID is: <b>" + CardID + "</b>\nYour Name is：<b>" + Name + "</b>")

                                ForgetPwd_flag = True
                                break  # 卡号输入正确跳出循环
                            else:
                                QMessageBox.critical(self.ui, '信息有误', "请重新输入您的卡号和用户名")
                                continue
                        else:
                            break  # 退出用户名对话输入框

                    else:
                        QMessageBox.critical(self.ui, '卡号有误', "卡号为11位数字")
                        continue
                else:
                    break  # 退出CardID对话输入框
        else:
            pass  # 忽略冻结账户对话框

        if ForgetPwd_flag:
            while 1:
                Pwd1, okPressed1 = QInputDialog.getText(self.ui, "请输入你的密码", "Password:", QLineEdit.Password, "")
                if okPressed1:
                    Pwd2_Confirm, okPressed2 = QInputDialog.getText(self.ui, "请再次输入你密码", "Password:", QLineEdit.Password, "")
                    if okPressed2:
                        if Pwd1==Pwd2_Confirm:
                            Status = self.DB.ModeifyInfo([CardID, Name, 'loginPassword',Pwd2_Confirm, '修改密码'])
                            if Status[0] == 1 and Status[1] == 1:
                                QMessageBox.information(self.ui, '操作成功', "密码已修改,请使用新密码登陆登录...")
                                self.DB.ConFirm_DB(1, 0)
                                break

                            else:
                                QMessageBox.information(self.ui, '操作失败', "密码修改失败")
                                self.DB.ConFirm_DB(0)
                                break
                        else:
                            QMessageBox.information(self.ui, '操作失败', "两次密码不一致，请重新输入")
                            continue

                    else:
                        QMessageBox.information(self.ui, '操作失败', "密码修改失败")
                        pass
                else:
                    QMessageBox.information(self.ui, '操作失败', "密码修改失败")
                    break

    # 跳转到交易界面，先进入进度条，然后进入界面
    # 不要在子线程中修改主线程的内容，通过在子线程中发射信号，主线程接收后再去修改
    def LogToBar(self):
        # self.ui.hide()
        self.signal_startui_to_Merchantui.emit()



# 导入放在最后，因为交叉引用会出问题

from MerchantUI import MerchantUI

from RegisterUI import RegisterUI

from ProgressBar import *


if __name__ == '__main__':

    # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support
    # https://github.com/pyinstaller/pyinstaller/issues/182
    # https: // blog.csdn.net / wm9028 / article / details / 101208869
    multiprocessing.freeze_support() # 解决使用pyinstaller打包无法进入子进程的界面

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    panel = StartUI()
    panel.ui.show()
    sys.exit(app.exec_())

# pyinstaller -F -c --paths ../venv/Lib/site-packages/shiboken2  --hidden-import PySide2.QtXml StartUI.py

# pyinstaller -F -c -w -D  --hidden-import PySide2.QtXml StartUI.py -i ../UI/Bank.ico