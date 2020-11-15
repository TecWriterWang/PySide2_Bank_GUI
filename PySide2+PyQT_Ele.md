

# Pyside2/PyQt5控件总结

参考：https://www.jianshu.com/nb/46707335

## QMessage 文本提示框

http://www.python3.vip/tut/py/gui/qt_05_4/

## QLineEdit 文本输入框

- Settext() 设置输入框内容
- text() 获取输入框内容
- textChanged.connect(func) 文本改变触发的槽函数
- **QLineEdit.Normal** 使用普通模式显示输入框，**QLineEdit.Password** 使用密文模式显示输入框





# 多文件交叉引用

python中多文件交叉引用，会导致出现不能导入文件，这个时候将导入的跑放在代码最后一行，可暂时解决问题，根本上还是需要考虑代码结构的问题