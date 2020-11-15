# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 17:07

from __init__ import *
from ui2py.Merchant import Ui_Merchant

from ui2py.Tran import Ui_Tran

import close_flag


input_Value_flag = False
input_value = []
manageacc_flag = False

# 交易界面
class MerchantUI(QMainWindow):

    def __init__(self,CardID):

        # python3 继承,使用super()可以调用父类的初始化方法__init__
        super().__init__()  # 因为继承关系，要对父类初始化

        # python2继承
        # super(MerchantUI,self).__init__()  # 因为继承关系，要对父类初始化

        self.CardID = CardID

        # 这里使用动态加载的方式
        # self.ui = QUiLoader().load('../UI/Merchant_2.ui')

        # 使用Pyuic生成界面代码的方式,若要继承关闭事件，必须使用此方法
        self.ui = Ui_Merchant()
        self.ui.setupUi(self)

        self.DB = Op_DB()
        self.Userinfo = self.DB.retUserInfo(self.CardID)
        self.CardID = self.Userinfo[1]

        self.status = QMainWindow.statusBar(self)
        self.status.font()
        self.status.showMessage(f'当前账户：{self.CardID}')

        self.setFixedSize(self.width(), self.height()) #仅可用在动态加载UI的方式中

        self.ui.btSaveMoney.clicked.connect(self.SaveMoney)
        self.ui.btGetMoney.clicked.connect(self.GetMoney)
        self.ui.btTransMoney.clicked.connect(self.TransMoney)
        self.ui.btAccountManage.clicked.connect(self.ManageAccount)

        # 注销登陆
        self.ui.btLogOut.clicked.connect(self.Exit)

        # 直接退出界面
        # self.ui.btLogOut.clicked.connect(QApplication.instance().quit)

        self.ui.btShowLog.clicked.connect(self.ShowLog)
        self.show()

    def closeEvent(self, event):  # 函数名固定不可变

        if close_flag.ManageUI_To_MerchantUI_Flag:
            event.accept()
        else:
            reply = QMessageBox.question(self, u'警告', u'确认退出?', QMessageBox.Yes, QMessageBox.No)
            # QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
            if reply == QMessageBox.Yes:
                if manageacc_flag:
                    self.manageui.close()
                event.accept()  # 关闭窗口
            else:
                event.ignore()  # 忽视点击X事件
                return 0

    def OP_Money(self):
        self.Userinfo = self.DB.retUserInfo(self.CardID)
        global input_value
        while 1:
            input_value = list(QInputDialog().getText(self, "请输入金额", "Money:", QLineEdit.Normal, ""))
            if input_value[1]:
                try:
                    s = re.compile(r"^0$|0.0$|[1-9]+(.[0-9]{2})?$").fullmatch(input_value[0])
                    if re.compile(r"^[1-9]+(.[0-9]{2})?$").fullmatch(input_value[0]): # 可以匹配小数
                        input_value[0] = float(input_value[0])
                        global input_Value_flag
                        input_Value_flag = True
                        break
                    else:
                        QMessageBox.information(self, '金额有误', "请重新输入金额，金额必须为大于0的有效数字")
                        continue

                except ValueError:
                        QMessageBox.information(self, '金额有误', "请重新输入金额，金额必须为大于0的有效数字")
                        continue
            else:
                QMessageBox.information(self, '交易失败', "已取消交易")
                break
    # 存钱
    def SaveMoney(self):
        # 获取账户实时信息
        # ModifData['卡号','用户名','修改字段','修改的字段值','操作日志']
        # 修改字段=[loginPassword,phone,cash,email]
        self.OP_Money()
        global input_value, input_Value_flag

        if input_Value_flag:
            reply_cash = QMessageBox.question(self,u'确认金额',f"您存入的金额是{input_value[0]}元",QMessageBox.Yes, QMessageBox.No)
            Save_value = (self.Userinfo[8]) + float(input_value[0])
            if reply_cash == QMessageBox.Yes:
                Save_flag = self.DB.ModeifyInfo((self.Userinfo[1],self.Userinfo[2],'cash',Save_value,f'Save moeny {Save_value}'))
                if Save_flag != -1 :
                    QMessageBox.information(self, '操作成功', "{0}已存入{1}元，当前账户余额{2}".format(self.CardID, input_value,Save_value))
                    self.DB.ConFirm_DB(1,2)
                else:
                    QMessageBox.information(self, '操作失败', "存钱失败，请拿好您的现金,人工台办理业务")
                    self.DB.ConFirm_DB(0)

            else:
                QMessageBox.information(self, '交易失败', "已取消交易")


    # 取钱
    def GetMoney(self):
        while 1:
            self.OP_Money()
            global input_value, input_Value_flag
            if input_Value_flag:
                if (self.Userinfo[8] - float(input_value[0])) < 0.0:
                    QMessageBox.information(self, '交易失败', f"余额不足，当前可用余额{self.Userinfo[8]}元，请重新输入")
                    continue
                else:
                    break
            else:
                break

        if input_Value_flag:
            reply_cash = QMessageBox.question(self,u'确认金额',f"您的取现的金额是{input_value[0]}元",QMessageBox.Yes, QMessageBox.No)

            Save_value = (self.Userinfo[8]) - input_value[0]
            if reply_cash == QMessageBox.Yes:
                Save_flag = self.DB.ModeifyInfo((self.Userinfo[1],self.Userinfo[2],'cash',Save_value,f'Get moeny {input_value[0]}'))
                if Save_flag != -1 :
                    QMessageBox.information(self, '操作成功', "{0}已取出{1}元，当前账户余额{2}".format(self.CardID, input_value[0],Save_value))
                    self.DB.ConFirm_DB(1, 2)
                else:
                    QMessageBox.information(self, '操作失败', "取现失败，请到人工台办理业务")
                    self.DB.ConFirm_DB(0)

            else:
                QMessageBox.information(self, '交易失败', "已取消交易")

    # 转账
    def TransMoney(self):
        self.tran = TranUI(self.Userinfo[1])

    def ManageAccount(self):
        global manageacc_flag
        manageacc_flag = True
        self.manageui = ManageUI(self.Userinfo,self)


    # 显示当前账户操作日志
    def ShowLog(self):
        Log = self.DB.getDatafromLog(self.CardID)

        # 从数据库中读取操作记录
        # Log = '7.16 取出1000元' # 数据库查询当前账户的记录
        str = ''
        for info in Log:
            str += "Data:{0} Event：{1}\n".format(info[3],info[2])
        # 设置显示的内容
        self.ui.ShowLog.append(str)
        # self.ui.ShowLog.setPlainText(str)

        # 控制滚动条游标，始终可见
        self.ui.ShowLog.ensureCursorVisible()
        # 设置内容是否可编辑
        self.ui.ShowLog.setEnabled(True)

    # 打印当前账户操作日志到指定文件
    def PrintLog(self):
        Log = self.DB.getDatafromLog(self.CardID)

        # 从数据库中读取操作记录
        # Log = '7.16 取出1000元' # 数据库查询当前账户的记录
        str = ''
        for info in Log:
            str += "Data:{0} Event：{1}\n".format(info[3],info[2])
        # 设置显示的内容
        self.ui.ShowLog.append(str)
        # self.ui.ShowLog.setPlainText(str)

        # 控制滚动条游标，始终可见
        self.ui.ShowLog.ensureCursorVisible()
        # 设置内容是否可编辑
        self.ui.ShowLog.setEnabled(True)

    # 退出交易
    def Exit(self):
        if self.close():
            self.StaUI = StartUI()
            self.StaUI.ui.show()


class TranUI(QWidget):

    def __init__(self,CardID):
        super().__init__()

        self.ui = Ui_Tran()
        self.ui.setupUi(self)
        self.show()

        self.CardID = CardID
        self.DB = Op_DB()

        self.ui.InName.setToolTip("请输入收款人姓名")
        self.ui.InCardID.setToolTip("请输入收款人卡号")
        self.ui.InCash.setToolTip("请输入转账金额")

        self.ui.btTran.clicked.connect(self.Confirm_Tran)

    def Confirm_Tran(self):
        global input_Value_flag
        self.TranUserinfo = self.DB.retUserInfo(self.CardID)
        while 1:
            Rec_CardID = self.ui.InCardID.text()
            Rec_Name = self.ui.InName.text()
            Tran_Cash = self.ui.InCash.text()
            try:
                if (len(Rec_CardID) and len(Rec_Name) and len(Tran_Cash)):

                    s = re.compile(r"[^-][0-9]*.?[0-9]*").fullmatch(Tran_Cash)
                    if re.compile(r"[^-][0-9]*.?[0-9]*").fullmatch(Tran_Cash):  # 可以匹配小数
                        Tran_Cash = float(Tran_Cash)
                        input_Value_flag = True

                    else:
                        self.ui.InCash.setStyleSheet("background-color:red")
                        input_Value_flag = False
                        self.ui.InCash.setStyleSheet("background-color:white")
                        QMessageBox.information(self, '金额有误', "请重新输入金额，金额必须为大于0的有效数字")
                        break
                else:
                    if (len(Rec_CardID) == 0):
                        QMessageBox.warning(self, '输入有误', f'请输入收款人卡号')
                    elif (len(Rec_CardID) == 0):
                        QMessageBox.warning(self, '输入有误', f'请输入收款人姓名')
                    elif (len(Rec_CardID) == 0):
                        QMessageBox.warning(self, '输入有误', f'请输入您的转账金额')
                    break


            except ValueError:
                # QMessageBox.information(self, '金额有误', "请重新输入金额，金额必须为大于0的有效数字")
                break

            if input_Value_flag:

                if self.DB.queue_data(Rec_CardID, Rec_Name):
                    if self.TranUserinfo[8] >= Tran_Cash:
                        virtua_balance = self.TranUserinfo[8] - Tran_Cash
                        while 1:
                            pwd_input = QInputDialog.getText(self, "请输入密码", "Password", QLineEdit.Password,"")
                            if len(pwd_input[0]) == 0:
                                QMessageBox.warning(self, '密码输入有误', f'请输入您的密码')
                                continue
                            else:
                                break
                        if pwd_input[1]:
                            if self.DB.encrypePW(pwd_input[0]) == self.TranUserinfo[3]:
                                reply_cash = QMessageBox.question(self, u'确认金额', f"您的转出金额是{Tran_Cash}元", QMessageBox.Yes, QMessageBox.No)
                                if reply_cash == QMessageBox.Yes:
                                    try:
                                        Tran_Flag = self.DB.ModeifyInfo((self.TranUserinfo[1], self.TranUserinfo[2], 'cash', virtua_balance, f"TranOut To {Rec_CardID} {Tran_Cash}元"))
                                        if Tran_Flag[0] != -1:
                                            Tran_Userinfo_Now = self.DB.retUserInfo(self.CardID) # 转账后实际余额-Tran
                                            Rec_Userinfo_Origin = self.DB.retUserInfo(Rec_CardID) # 收款前实际余额-Rec
                                            Rec_Flag = self.DB.ModeifyInfo((Rec_CardID, Rec_Name, 'cash', Rec_Userinfo_Origin[8]+Tran_Cash, f"Recieve {Tran_Cash}元 From {self.CardID}"))
                                            Rec_Userinfo_Now = self.DB.retUserInfo(Rec_CardID) # 收款后实际余额-Rec
                                            Real_Rec_Cash = Rec_Userinfo_Now[8] - Rec_Userinfo_Origin[8] # 实际收款-Rec
                                            A_flag = abs(Tran_Cash - Real_Rec_Cash) > 1e-014
                                            if Rec_Flag[0] != -1 and A_flag  and Tran_Userinfo_Now[8] == virtua_balance:
                                                QMessageBox.information(self, '交易成功', f"您的账户{self.TranUserinfo[1]}已转出{Tran_Cash}元")
                                                self.DB.ConFirm_DB(1,2)
                                                self.close()
                                                break
                                            else:
                                                QMessageBox.information(self, '交易失败', "请到人工台处理")
                                                self.DB.ConFirm_DB(0)
                                                self.close()
                                                break
                                        else:
                                            QMessageBox.information(self, '交易失败', "交易密码错误")
                                            self.DB.ConFirm_DB(0)
                                            self.close()
                                            break
                                    except Exception:
                                        self.DB.ConFirm_DB(0)

                                else:
                                    QMessageBox.information(self, '交易取消', "交易已取消")
                                    self.close()
                                    break
                            else:
                                QMessageBox.information(self, '交易失败', "交易密码错误")
                                self.close()
                                break
                        else:
                            QMessageBox.information(self, '交易取消', "交易已取消")
                            self.close()
                            break

                    else:
                        QMessageBox.information(self, '交易失败', f"您的账户余额不足，当前可用余额{self.TranUserinfo[8]}元")
                        self.close()
                        break
                # QMessageBox.information(self, '操作成功', "{0}存入1000元".format(self.CardID))
                else:
                    QMessageBox.information(self, '账户错误', "收款卡号和姓名不匹配，请确认后重新输入")
                    self.close()
                    break


    # self.tran.ui.btTran.clicked.connect(Confirm_Tran)


# 导入放在最后，因为交叉引用会出问题
from StartUI import StartUI
from ManageUI import ManageUI

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    panel = MerchantUI(62201206121)
    sys.exit(app.exec_())