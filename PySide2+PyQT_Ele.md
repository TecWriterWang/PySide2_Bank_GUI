

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





# 线程、进程

不要在子线程中直接操作主线程的内容，一般通过子线程发信号的方式给主线程，然后修改。



# 信号操作

导入Signal类，然后新建一个信号对象，根据使用的方式确定信号的参数



# 打包

pyinstaller 打包含有多进程的代码后，执行exe无法跳转到多进程的界面内。

解决办法：徐在代码添加一段内容，具体代码见程序内部