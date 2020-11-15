# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 17:50

from __init__ import *
import close_flag

from ui2py.Manage import Ui_Manage

class ManageUI(QWidget):

    def __init__(self,Userinfo,selfMerchant=0):
        super().__init__()
        self.ui = Ui_Manage()
        self.ui.setupUi(self)
        self.closeMerchant = selfMerchant

        self.info = Userinfo
        self.DB = Op_DB()

        self.ui.btLostFreez.clicked.connect(self.LostFreeze)
        self.ui.btUnSubscribe.clicked.connect(self.UnSubscrib)
        self.ui.btModifyPwd.clicked.connect(self.ModifyPW)

        self.show()



    def closeActive(self):

        if self.close():
            close_flag.ManageUI_To_MerchantUI_Flag = True
            self.closeMerchant.close()
            self.StaUI = StartUI()
            self.StaUI.ui.show()


    def LostFreeze(self):
        Status = self.DB.Freeze((self.info[1],self.info[2],'','冻结账户'))
        if Status[0] and Status[1]:
            QMessageBox.information(self, '操作成功', "账户已被冻结,即将退出...")
            self.closeActive()
        else:
            QMessageBox.information(self, '操作失败', "账户冻结失败")


    # 注销账户
    def UnSubscrib(self):
        Status = self.DB.delData(self.info)
        if len(Status) == 2:
            if Status[0] == 'Cash Not Zero':
                QMessageBox.information(self, '操作失败', f"你的账户有<b><font color=red>{Status[1]}</font></b>元未取出，请取出或转账后再操作")
        else:
            if Status[0]:
                QMessageBox.information(self, '操作成功', "账户已注销")
                self.DB.connection.commit()
                self.closeActive()
            else:
                QMessageBox.information(self, '操作失败', "账户注销失败")
                self.DB.connection.rollback()



    # 修改密码
    def ModifyPW(self):
        def ForgetPwd():
            ForgetPwd_flag = False
            while 1:
                CardID, okPressed = QInputDialog.getText(self, "请输入你的卡号/手机号", "CardID:", QLineEdit.Normal, "")
                if okPressed:
                    if re.compile(r"[0-9]*").fullmatch(CardID):  # 检测卡号是否为纯数字
                        Name, okPressed = QInputDialog.getText(self, "请输入你的用户名", "Name:", QLineEdit.Normal, "")
                        if okPressed:
                            # 补充邮件验证密码方式
                            if self.DB.queue_data(CardID, Name):
                                QMessageBox.information(self, "Information",
                                                        "Your CardID is: <b>" + CardID + "</b>\nYour Name is：<b>" + Name + "</b>")

                                ForgetPwd_flag = True
                                break  # 卡号输入正确跳出循环
                            else:
                                QMessageBox.critical(self, '信息有误', "请重新输入您的卡号和用户名")
                                continue
                        else:
                            break  # 退出用户名对话输入框

                    else:
                        QMessageBox.critical(self, '卡号有误', "卡号为11位数字")
                        continue
                else:
                    break  # 退出CardID对话输入框

            if ForgetPwd_flag:
                while 1:
                    Pwd1, okPressed1 = QInputDialog.getText(self, "请输入你的密码", "Password:", QLineEdit.Password, "")
                    if okPressed1:
                        Pwd2_Confirm, okPressed2 = QInputDialog.getText(self, "请再次输入你密码", "Password:", QLineEdit.Password, "")
                        if okPressed2:
                            if Pwd1 == Pwd2_Confirm:
                                Status = self.DB.ModeifyInfo([CardID, Name, 'loginPassword', Pwd2_Confirm, '修改密码']) #修改密码时需要修改传入的数据值
                                if Status[0] == 1 and Status[1] == 1:
                                    QMessageBox.information(self, '操作成功', "密码已修改,请使用新密码登陆登录...")
                                    self.DB.ConFirm_DB(1, 0)
                                    self.closeActive()
                                    break
                                else:
                                    QMessageBox.information(self, '操作失败', "密码修改失败")
                                    self.DB.ConFirm_DB(0)
                            else:
                                QMessageBox.information(self, '操作失败', "两次密码不一致，请重新输入")
                                continue

                        else:
                            QMessageBox.information(self, '操作失败', "密码修改失败")
                            break
                    else:
                        QMessageBox.information(self, '操作失败', "密码修改失败")
                        break

        reply = QMessageBox.question(self, u'警告', u'你确定要修改密码?', QMessageBox.Yes, QMessageBox.No)
        # QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply == QMessageBox.Yes:
            ForgetPwd()
        else:
            return 0


from StartUI import StartUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    panel = ManageUI((0,62201206121,'www','','freeze'))
    sys.exit(app.exec_())