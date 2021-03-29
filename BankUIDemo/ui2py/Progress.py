# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Progress.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        if not ProgressBar.objectName():
            ProgressBar.setObjectName(u"ProgressBar")
        ProgressBar.resize(348, 93)
        self.verticalLayout = QVBoxLayout(ProgressBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LoginWait = QLabel(ProgressBar)
        self.LoginWait.setObjectName(u"LoginWait")
        self.LoginWait.setLayoutDirection(Qt.LeftToRight)
        self.LoginWait.setStyleSheet(u"font: 75 9pt \"Adobe Arabic\" bold;")
        self.LoginWait.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LoginWait)

        self.LoginProgress = QProgressBar(ProgressBar)
        self.LoginProgress.setObjectName(u"LoginProgress")
        self.LoginProgress.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.LoginProgress.setValue(50)

        self.verticalLayout.addWidget(self.LoginProgress)


        self.retranslateUi(ProgressBar)

        QMetaObject.connectSlotsByName(ProgressBar)
    # setupUi

    def retranslateUi(self, ProgressBar):
        ProgressBar.setWindowTitle(QCoreApplication.translate("ProgressBar", u"\u767b\u9646\u4e2d", None))
        self.LoginWait.setText(QCoreApplication.translate("ProgressBar", u"<html><head/><body><p><span style=\"\n"
"       font-weight:600;\">\u6b63\u5728\u767b\u9646\uff0c\u8bf7\u7a0d\u7b49...</span></p></body></html>", None))
    # retranslateUi

