
from __init__ import *

# 注册窗口
class RegisterUI(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_RegisterUI()
        self.ui.setupUi(self)
        self.db = Op_DB()

        # 动态加载UI
        # self.ui = QUiLoader().load('../UI/RegisterUI.ui')

        # 窗口大小固定
        self.setFixedSize(self.width(), self.height())

        # 设置密码输入框显示圆点
        self.ui.InPassword.setEchoMode(QLineEdit.Password)
        self.ui.ReInPassword.setEchoMode(QLineEdit.Password)
        self.ui.btRegister.clicked.connect(self.register)


    def closeEvent(self, event):  # 函数名固定不可变
        self.ReOpenStaUI()

    def getText(self):
        self.Name = self.ui.InName.text()
        self.AuthiorID = self.ui.InCardID.text()
        self.Gender = self.ui.InGender.currentText()
        self.Email = self.ui.InEmail.text()
        self.Phone = self.ui.InPhone.text()
        self.PassWord = self.ui.InPassword.text()
        self.RePassWord = self.ui.ReInPassword.text()

    def checkNone(self):
        self.getText()
        if self.Name is '':
            return '姓名'

        # 身份证号
        elif self.AuthiorID is '':
            return '身份证'

        elif self.PassWord is '':
            return '密码'

        elif self.RePassWord is '':
            return '确认密码'

        elif self.PassWord != self.RePassWord:
            return '两次密码不一致'

        elif self.Gender is '':
            return '性别'

        elif self.Email is '':
            return '邮箱地址'

        elif self.Phone is '':
            return '手机号'

    def creat_userinfo(self):
        # 创建卡号
        self.CardID = '622'
        for i in range(8):
            number = random.randint(0, 9)
            self.CardID += str(number)
        # 创建手机号
        # 随机生成手机号
        # phoneNumber = '1'
        # for i in range(10):
        #     number = random.randint(0, 9)
        #     phoneNumber += str(number)

        # 手动输入手机号
        # phoneNumber = input("请输入您的手机号：")

        # 创建身份证号
        self.uidNumber = str(random.randint(1, 8))

        while True:
            number = random.randint(0, 9)
            self.uidNumber += str(number)

            if len(self.uidNumber) == 18:
                break
        # return phoneNumber, uidNumber, cardNumber
        return self.CardID,self.uidNumber

    def register(self):

        if self.checkNone() == '两次密码不一致':
            QMessageBox.warning(self,'操作失败',f"注册失败，两次密码不一致，请重新输入")

        elif (self.Name and self.AuthiorID and self.Gender and self.Email and self.Phone and self.PassWord==self.RePassWord):
            self.creat_userinfo()
            self.db.SaveData([self.CardID,self.Name, self.PassWord,self.AuthiorID, self.Gender, self.Phone,self.Email,"CreateAccount",0,0])
            reply = QMessageBox.question(self, '注册成功', f"请牢记你的银行卡号<b><font size=4 color=red>'{self.CardID}'</font></b>", QMessageBox.Yes, QMessageBox.No)
            # QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
            if reply == QMessageBox.Yes:
                pass
            else:
                pass

            QMessageBox.information(self,'注册成功',f"你的银行卡号是<b><font size=4 color=red>'{self.CardID}'</font></b>，可以使用您的卡号或手机号登录")
            self.deleteLater()
            self.ReOpenStaUI()

        else:
            QMessageBox.warning(self,'注册失败',f"请输入<b><font size=4 color=red>'{self.checkNone()}'</font></b>后，重新注册")
            self.ui.InName.clear()
            self.ui.InCardID.clear()
            self.ui.InEmail.clear()
            self.ui.InPhone.clear()
            self.ui.InPassword.clear()
            self.ui.ReInPassword.clear()

    def ReOpenStaUI(self):
        # self.StaUI = StartUI() # 类初始化时就直接创建两个窗口会造成栈内存溢出，在使用时初始化即可
        self.StaUI = StartUI()
        self.StaUI.ui.show()

# 导入放在最后，因为交叉引用会出问题

from StartUI import StartUI
from ui2py.Register import *


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../UI/Bank.ico'))
    panel = RegisterUI()
    panel.show()
    sys.exit(app.exec_())