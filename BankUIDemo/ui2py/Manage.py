# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Manage.ui'
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


class Ui_Manage(object):
    def setupUi(self, Manage):
        if not Manage.objectName():
            Manage.setObjectName(u"Manage")
        Manage.resize(362, 118)
        self.verticalLayout = QVBoxLayout(Manage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btUnTransaction = QPushButton(Manage)
        self.btUnTransaction.setObjectName(u"btUnTransaction")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btUnTransaction.setFont(font)

        self.gridLayout.addWidget(self.btUnTransaction, 0, 1, 1, 1)

        self.btLostFreez = QPushButton(Manage)
        self.btLostFreez.setObjectName(u"btLostFreez")
        self.btLostFreez.setFont(font)

        self.gridLayout.addWidget(self.btLostFreez, 0, 0, 1, 1)

        self.btModifyPwd = QPushButton(Manage)
        self.btModifyPwd.setObjectName(u"btModifyPwd")
        self.btModifyPwd.setFont(font)

        self.gridLayout.addWidget(self.btModifyPwd, 1, 0, 1, 1)

        self.btUnSubscribe = QPushButton(Manage)
        self.btUnSubscribe.setObjectName(u"btUnSubscribe")
        self.btUnSubscribe.setFont(font)

        self.gridLayout.addWidget(self.btUnSubscribe, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Manage)

        QMetaObject.connectSlotsByName(Manage)
    # setupUi

    def retranslateUi(self, Manage):
        Manage.setWindowTitle(QCoreApplication.translate("Manage", u"安全中心", None))
        self.btUnTransaction.setText(QCoreApplication.translate("Manage", u"\u5f02\u5e38\u4ea4\u6613\u5904\u7406", None))
        self.btLostFreez.setText(QCoreApplication.translate("Manage", u"\u6302\u5931\u51bb\u7ed3", None))
        self.btModifyPwd.setText(QCoreApplication.translate("Manage", u"\u4fee\u6539\u5bc6\u7801", None))
        self.btUnSubscribe.setText(QCoreApplication.translate("Manage", u"\u6ce8\u9500\u8d26\u6237", None))
    # retranslateUi

