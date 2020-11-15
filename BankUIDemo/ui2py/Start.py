# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Start.ui'
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


class Ui_StartUI(object):
    def setupUi(self, StartUI):
        if not StartUI.objectName():
            StartUI.setObjectName(u"StartUI")
        StartUI.resize(406, 249)
        self.centralwidget = QWidget(StartUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UITitle = QLabel(self.centralwidget)
        self.UITitle.setObjectName(u"UITitle")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UITitle.sizePolicy().hasHeightForWidth())
        self.UITitle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Adobe Arabic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.UITitle.setFont(font)
        self.UITitle.setMouseTracking(False)
        self.UITitle.setLayoutDirection(Qt.LeftToRight)
        self.UITitle.setAutoFillBackground(False)
        self.UITitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.UITitle)

        self.LayHAccout = QHBoxLayout()
        self.LayHAccout.setObjectName(u"LayHAccout")
        self.Account = QLabel(self.centralwidget)
        self.Account.setObjectName(u"Account")
        font1 = QFont()
        font1.setFamily(u"Adobe Arabic")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.Account.setFont(font1)

        self.LayHAccout.addWidget(self.Account)

        self.InAccount = QLineEdit(self.centralwidget)
        self.InAccount.setObjectName(u"InAccount")
        self.InAccount.setClearButtonEnabled(False)

        self.LayHAccout.addWidget(self.InAccount)

        self.btcheckAccount = QPushButton(self.centralwidget)
        self.btcheckAccount.setObjectName(u"btcheckAccount")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btcheckAccount.setFont(font2)

        self.LayHAccout.addWidget(self.btcheckAccount)


        self.verticalLayout.addLayout(self.LayHAccout)

        self.LayHPwd = QHBoxLayout()
        self.LayHPwd.setObjectName(u"LayHPwd")
        self.LayHPwd.setContentsMargins(-1, 0, -1, -1)
        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setFont(font1)

        self.LayHPwd.addWidget(self.Password)

        self.InPassword = QLineEdit(self.centralwidget)
        self.InPassword.setObjectName(u"InPassword")

        self.LayHPwd.addWidget(self.InPassword)

        self.horizontalSpacer = QSpacerItem(82, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.LayHPwd.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.LayHPwd)

        self.LayGridBt = QGridLayout()
        self.LayGridBt.setObjectName(u"LayGridBt")
        self.btForgetPw = QPushButton(self.centralwidget)
        self.btForgetPw.setObjectName(u"btForgetPw")
        sizePolicy.setHeightForWidth(self.btForgetPw.sizePolicy().hasHeightForWidth())
        self.btForgetPw.setSizePolicy(sizePolicy)
        self.btForgetPw.setFont(font2)

        self.LayGridBt.addWidget(self.btForgetPw, 5, 1, 1, 1)

        self.btUnLock = QPushButton(self.centralwidget)
        self.btUnLock.setObjectName(u"btUnLock")
        sizePolicy.setHeightForWidth(self.btUnLock.sizePolicy().hasHeightForWidth())
        self.btUnLock.setSizePolicy(sizePolicy)
        self.btUnLock.setFont(font2)

        self.LayGridBt.addWidget(self.btUnLock, 4, 1, 1, 1)

        self.btRegister = QPushButton(self.centralwidget)
        self.btRegister.setObjectName(u"btRegister")
        sizePolicy.setHeightForWidth(self.btRegister.sizePolicy().hasHeightForWidth())
        self.btRegister.setSizePolicy(sizePolicy)
        self.btRegister.setFont(font2)

        self.LayGridBt.addWidget(self.btRegister, 5, 0, 1, 1)

        self.btLogin = QPushButton(self.centralwidget)
        self.btLogin.setObjectName(u"btLogin")
        sizePolicy.setHeightForWidth(self.btLogin.sizePolicy().hasHeightForWidth())
        self.btLogin.setSizePolicy(sizePolicy)
        self.btLogin.setFont(font2)

        self.LayGridBt.addWidget(self.btLogin, 4, 0, 1, 1)

        self.verticalLayout.addLayout(self.LayGridBt)

        StartUI.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.InAccount, self.InPassword)
        QWidget.setTabOrder(self.InPassword, self.btcheckAccount)

        self.retranslateUi(StartUI)

        QMetaObject.connectSlotsByName(StartUI)
    # setupUi

    def retranslateUi(self, StartUI):
        StartUI.setWindowTitle(QCoreApplication.translate("StartUI", u"登陆", None))
        self.UITitle.setText(QCoreApplication.translate("StartUI", u"More Money Bank", None))
        self.Account.setText(QCoreApplication.translate("StartUI", u"\u8d26\u6237", None))
        self.btcheckAccount.setText(QCoreApplication.translate("StartUI", u"\u68c0\u6d4b\u8d26\u6237", None))
        self.Password.setText(QCoreApplication.translate("StartUI", u"\u5bc6\u7801", None))
        self.btForgetPw.setText(QCoreApplication.translate("StartUI", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.btUnLock.setText(QCoreApplication.translate("StartUI", u"\u89e3\u51bb\u8d26\u6237", None))
        self.btRegister.setText(QCoreApplication.translate("StartUI", u"\u6ce8\u518c", None))
        self.btLogin.setText(QCoreApplication.translate("StartUI", u"\u767b\u5f55", None))
    # retranslateUi

