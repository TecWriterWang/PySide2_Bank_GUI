# # -*- coding: utf-8 -*-
# # @Time    : 2020/7/14 23:01
#

# http://www.python3.vip/tut/py/gui/web-0100/

"""Test1"""
# from pyqtgraph.Qt import QtGui, QtCore
# import pyqtgraph as pg
#
# # 创建 PlotWidget 对象
# pw = pg.plot()
#
# # 设置图表标题、颜色、字体大小
# pw.setTitle("气温趋势",color='008080',size='12pt')
#
# # 背景色改为白色
# pw.setBackground('w')
#
# # 显示表格线
# pw.showGrid(x=True, y=True)
#
# # 设置上下左右的label
# # 第一个参数 只能是 'left', 'bottom', 'right', or 'top'
# pw.setLabel("left", "气温(摄氏度)")
# pw.setLabel("bottom", "时间")
#
# # 设置Y轴 刻度 范围
# pw.setYRange(min=-10,  # 最小值
#              max=50)  # 最大值
#
# # 创建 PlotDataItem ，缺省是曲线图
# curve = pw.plot( pen=pg.mkPen('b')) # 线条颜色
#
# hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
#
# curve.setData(hour, # x坐标
#               temperature  # y坐标
#               )
#
# QtGui.QApplication.instance().exec_()


"""Test2"""
# from PySide2 import QtWidgets
# import pyqtgraph as pg
#
# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('pyqtgraph作图示例')
#
#         # 创建 PlotWidget 对象
#         self.pw = pg.PlotWidget()
#
#         # 设置图表标题
#         self.pw.setTitle("气温趋势",
#                          color='008080',
#                          size='12pt')
#
#         # 设置上下左右的label
#         self.pw.setLabel("left","气温(摄氏度)")
#         self.pw.setLabel("bottom","时间")
#
#         # 设置Y轴 刻度 范围
#         self.pw.setYRange(min=-10, # 最小值
#                           max=50)  # 最大值
#
#
#         # 显示表格线
#         self.pw.showGrid(x=True, y=True)
#
#         # 背景色改为白色
#         self.pw.setBackground('w')
#
#         # 居中显示 PlotWidget
#         self.setCentralWidget(self.pw)
#
#         hour = [1,2,3,4,5,6,7,8,9,10]
#         temperature = [30,32,34,32,33,31,29,32,35,45]
#
#         # hour 和 temperature 分别是 : x, y 轴上的值
#         self.pw.plot(hour,
#                      temperature,
#                      pen=pg.mkPen('b') # 线条颜色
#                     )
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication()
#     main = MainWindow()
#     main.show()
#     app.exec_()


"""Test3"""
#
# from PySide2 import QtWidgets
# from pyqtgraph.Qt import  QtCore
# import pyqtgraph as pg
# import sys
# from random import randint
#
# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('pyqtgraph作图')
#
#         # 创建 PlotWidget 对象
#         self.pw = pg.PlotWidget()
#
#         # 设置图表标题
#         self.pw.setTitle("气温趋势",
#                          color='008080',
#                          size='12pt')
#
#         # 设置上下左右的label
#         self.pw.setLabel("left","气温(摄氏度)")
#         self.pw.setLabel("bottom","时间")
#
#         # 设置Y轴 刻度 范围
#         self.pw.setYRange(min=-10, # 最小值
#                           max=50)  # 最大值
#
#         # 显示表格线
#         self.pw.showGrid(x=True, y=True)
#
#         # 背景色改为白色
#         self.pw.setBackground('w')
#
#         # 设置Y轴 刻度 范围
#         self.pw.setYRange(min=-10, # 最小值
#                           max=50)  # 最大值
#
#         # 居中显示 PlotWidget
#         self.setCentralWidget(self.pw)
#
#         # 实时显示应该获取 plotItem， 调用setData，
#         # 这样只重新plot该曲线，性能更高
#         self.curve = self.pw.getPlotItem().plot(
#             pen=pg.mkPen('r', width=1)
#         )
#
#         self.i = 0
#         self.x = [] # x轴的值
#         self.y = [] # y轴的值
#
#         # 启动定时器，每隔1秒通知刷新一次数据
#         self.timer = QtCore.QTimer()
#         self.timer.timeout.connect(self.updateData)
#         self.timer.start(1000)
#
#     def updateData(self):
#         self.i += 1
#         self.x.append(self.i)
#         # 创建随机温度值
#         self.y.append(randint(10,30))
#
#         # plot data: x, y values
#         self.curve.setData(self.x,self.y)
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication()
#     main = MainWindow()
#     main.show()
#     app.exec_()

"""Test4"""


from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg

class Stock:

    def __init__(self):

        loader = QUiLoader()

        # pyside2 一定要 使用registerCustomWidget
        # 来注册 ui文件中的第三方控件，这样加载的时候
        # loader才知道第三方控件对应的类，才能实例化对象
        loader.registerCustomWidget(pg.PlotWidget)
        self.ui = loader.load("main.ui")

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # 通过控件名称 historyPlot，找到Qt designer设计的 控件
        self.ui.historyPlot.plot(hour,temperature)

app = QApplication([])
stock = Stock()
stock.ui.show()
app.exec_()