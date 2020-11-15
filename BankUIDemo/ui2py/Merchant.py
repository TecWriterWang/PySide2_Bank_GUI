# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Merchant_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Merchant(object):
    def setupUi(self, Merchant):
        if not Merchant.objectName():
            Merchant.setObjectName(u"Merchant")
        Merchant.resize(616, 439)
        self.centralwidget = QWidget(Merchant)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.HAll = QHBoxLayout()
        self.HAll.setObjectName(u"HAll")
        self.Vbt = QVBoxLayout()
        self.Vbt.setObjectName(u"Vbt")
        self.btSaveMoney = QPushButton(self.centralwidget)
        self.btSaveMoney.setObjectName(u"btSaveMoney")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btSaveMoney.setFont(font)

        self.Vbt.addWidget(self.btSaveMoney)

        self.btGetMoney = QPushButton(self.centralwidget)
        self.btGetMoney.setObjectName(u"btGetMoney")
        self.btGetMoney.setFont(font)

        self.Vbt.addWidget(self.btGetMoney)

        self.btTransMoney = QPushButton(self.centralwidget)
        self.btTransMoney.setObjectName(u"btTransMoney")
        self.btTransMoney.setFont(font)

        self.Vbt.addWidget(self.btTransMoney)

        self.btAccountManage = QPushButton(self.centralwidget)
        self.btAccountManage.setObjectName(u"btAccountManage")
        self.btAccountManage.setFont(font)

        self.Vbt.addWidget(self.btAccountManage)

        self.btLogOut = QPushButton(self.centralwidget)
        self.btLogOut.setObjectName(u"btLogOut")
        self.btLogOut.setFont(font)

        self.Vbt.addWidget(self.btLogOut)


        self.HAll.addLayout(self.Vbt)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ShowLog = QTextBrowser(self.groupBox)
        self.ShowLog.setObjectName(u"ShowLog")

        self.verticalLayout_2.addWidget(self.ShowLog)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btShowLog = QPushButton(self.groupBox)
        self.btShowLog.setObjectName(u"btShowLog")
        self.btShowLog.setFont(font)

        self.horizontalLayout.addWidget(self.btShowLog)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.HAll.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.HAll)

        Merchant.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Merchant)
        self.statusbar.setObjectName(u"statusbar")
        Merchant.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btSaveMoney, self.btGetMoney)
        QWidget.setTabOrder(self.btGetMoney, self.btTransMoney)
        QWidget.setTabOrder(self.btTransMoney, self.btAccountManage)
        QWidget.setTabOrder(self.btAccountManage, self.btLogOut)
        QWidget.setTabOrder(self.btLogOut, self.btShowLog)
        QWidget.setTabOrder(self.btShowLog, self.ShowLog)

        self.retranslateUi(Merchant)

        QMetaObject.connectSlotsByName(Merchant)
    # setupUi

    def retranslateUi(self, Merchant):
        Merchant.setWindowTitle(QCoreApplication.translate("Merchant", u"账户交易", None))
        self.btSaveMoney.setText(QCoreApplication.translate("Merchant", u"\u5b58\u94b1", None))
        self.btGetMoney.setText(QCoreApplication.translate("Merchant", u"\u53d6\u94b1", None))
        self.btTransMoney.setText(QCoreApplication.translate("Merchant", u"\u8f6c\u8d26", None))
        self.btAccountManage.setText(QCoreApplication.translate("Merchant", u"安全中心", None))
        self.btLogOut.setText(QCoreApplication.translate("Merchant", u"\u9000\u51fa\u767b\u5f55", None))
        self.groupBox.setTitle(QCoreApplication.translate("Merchant", u"OperateLog", None))
        self.btShowLog.setText(QCoreApplication.translate("Merchant", u"\u67e5\u8be2\u65e5\u5fd7", None))
    # retranslateUi

