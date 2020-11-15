# -*- coding: utf-8 -*-

# pyside2-uic H:\PythonWorkSpace\PyQtStudio\Bases.ui -o Base.py


import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox,\
    QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QWidget


"""
薛蟠     4560 25
薛蝌     4460 25
薛宝钗   35776 23
薛宝琴   14346 18
王夫人   43360 45
王熙凤   24460 25
王子腾   55660 45
王仁     15034 65
尤二姐   5324 24
贾芹     5663 25
贾兰     13443 35
贾芸     4522 25
尤三姐   5905 22
贾珍     54603 35
"""

class QtTest():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 310)
        self.window.setWindowTitle('薪资统计')


        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10,25)
        self.textEdit.resize(300,350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380,80)

        self.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        print('统计按钮被点击了')
        # 获取文本输入框的所有信息
        info = self.textEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        # splitlines 把字符串按照换行符分割
        for line in info.splitlines():
            stp = line.strip()
            if not stp:
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                            \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )



app = QApplication([])
myqt = QtTest()
myqt.window.show()
app.exec_()

"""
# 点击界面上的按钮操作叫做发送signal
# 处理signal的函数叫做Slot
def handleCalc():
    print('统计按钮被点击了')
    # 获取文本输入框的所有信息
    info = textEdit.toPlainText()

    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    # splitlines 把字符串按照换行符分割
    for line in info.splitlines():
        stp = line.strip()
        if not stp:
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                      )


if __name__ == '__main__':

    app = QApplication([])

    window = QMainWindow()
    window.resize(500, 400)
    window.move(300, 310)
    window.setWindowTitle('薪资统计')

    textEdit = QPlainTextEdit(window)
    textEdit.setPlaceholderText("请输入薪资表")
    textEdit.move(10,25)
    textEdit.resize(300,350)

    button = QPushButton('统计', window)
    button.move(380,80)

    button.clicked.connect(handleCalc)

    window.show()
    # app.exec_()
    sys.exit(app.exec_())
"""
