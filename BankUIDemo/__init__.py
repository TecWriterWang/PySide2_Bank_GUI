# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 19:56

import sys,threading,time,random,re

import multiprocessing as mp

from threading import Thread,Lock

from PySide2.QtWidgets import QApplication,QLineEdit,QMainWindow,QPushButton,QPlainTextEdit,QWidget,QMessageBox,QAction,QInputDialog,QLabel

from PySide2.QtGui import QIcon # 设置窗口图标

from PySide2.QtUiTools import QUiLoader

from Op_DataBase import *


from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *






# QMessageBox
# https://developer.aliyun.com/article/712798