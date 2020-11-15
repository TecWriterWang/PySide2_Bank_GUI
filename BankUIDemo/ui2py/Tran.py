# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tran.ui'
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


class Ui_Tran(object):
    def setupUi(self, Tran):
        if not Tran.objectName():
            Tran.setObjectName(u"Tran")
        Tran.resize(226, 162)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tran.sizePolicy().hasHeightForWidth())
        Tran.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Tran)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.UITitle = QLabel(Tran)
        self.UITitle.setObjectName(u"UITitle")
        self.UITitle.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UITitle.sizePolicy().hasHeightForWidth())
        self.UITitle.setSizePolicy(sizePolicy1)
        self.UITitle.setMinimumSize(QSize(131, 24))
        self.UITitle.setMaximumSize(QSize(16777215, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UITitle.setFont(font)
        self.UITitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.UITitle)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HCard = QHBoxLayout()
        self.HCard.setObjectName(u"HCard")
        self.CardID = QLabel(Tran)
        self.CardID.setObjectName(u"CardID")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CardID.sizePolicy().hasHeightForWidth())
        self.CardID.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.CardID.setFont(font1)
        self.CardID.setLayoutDirection(Qt.LeftToRight)
        self.CardID.setScaledContents(False)
        self.CardID.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CardID.setMargin(0)
        self.CardID.setIndent(0)

        self.HCard.addWidget(self.CardID)

        self.InCardID = QLineEdit(Tran)
        self.InCardID.setObjectName(u"InCardID")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.InCardID.sizePolicy().hasHeightForWidth())
        self.InCardID.setSizePolicy(sizePolicy3)
        self.InCardID.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HCard.addWidget(self.InCardID)


        self.verticalLayout.addLayout(self.HCard)

        self.HName = QHBoxLayout()
        self.HName.setObjectName(u"HName")
        self.Name = QLabel(Tran)
        self.Name.setObjectName(u"Name")
        sizePolicy2.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy2)
        self.Name.setFont(font1)
        self.Name.setToolTipDuration(-1)
        self.Name.setLayoutDirection(Qt.LeftToRight)
        self.Name.setLineWidth(1)
        self.Name.setScaledContents(False)
        self.Name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Name.setMargin(0)
        self.Name.setIndent(0)

        self.HName.addWidget(self.Name)

        self.InName = QLineEdit(Tran)
        self.InName.setObjectName(u"InName")
        sizePolicy3.setHeightForWidth(self.InName.sizePolicy().hasHeightForWidth())
        self.InName.setSizePolicy(sizePolicy3)
        self.InName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HName.addWidget(self.InName)


        self.verticalLayout.addLayout(self.HName)

        self.HCash = QHBoxLayout()
        self.HCash.setObjectName(u"HCash")
        self.Cash = QLabel(Tran)
        self.Cash.setObjectName(u"Cash")
        sizePolicy2.setHeightForWidth(self.Cash.sizePolicy().hasHeightForWidth())
        self.Cash.setSizePolicy(sizePolicy2)
        self.Cash.setFont(font1)
        self.Cash.setLayoutDirection(Qt.LeftToRight)
        self.Cash.setScaledContents(False)
        self.Cash.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Cash.setMargin(0)
        self.Cash.setIndent(0)

        self.HCash.addWidget(self.Cash)

        self.InCash = QLineEdit(Tran)
        self.InCash.setObjectName(u"InCash")
        sizePolicy3.setHeightForWidth(self.InCash.sizePolicy().hasHeightForWidth())
        self.InCash.setSizePolicy(sizePolicy3)
        self.InCash.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HCash.addWidget(self.InCash)


        self.verticalLayout.addLayout(self.HCash)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btTran = QPushButton(Tran)
        self.btTran.setObjectName(u"btTran")
        sizePolicy3.setHeightForWidth(self.btTran.sizePolicy().hasHeightForWidth())
        self.btTran.setSizePolicy(sizePolicy3)
        self.btTran.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btTran.setFont(font2)
        self.btTran.setLayoutDirection(Qt.LeftToRight)
        self.btTran.setAutoFillBackground(False)
        self.btTran.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.btTran, 0, Qt.AlignRight|Qt.AlignBottom)


        self.retranslateUi(Tran)

        QMetaObject.connectSlotsByName(Tran)
    # setupUi

    def retranslateUi(self, Tran):
        Tran.setWindowTitle(QCoreApplication.translate("Tran", u"转账中", None))
        self.UITitle.setText(QCoreApplication.translate("Tran", u"\u8f6c\u8d26", None))
        self.CardID.setText(QCoreApplication.translate("Tran", u"\u6536\u6b3e\u5361\u53f7", None))
        self.Name.setText(QCoreApplication.translate("Tran", u"\u6536\u6b3e\u8d26\u6237\u540d", None))
        self.Cash.setText(QCoreApplication.translate("Tran", u"\u91d1\u989d", None))
        self.btTran.setText(QCoreApplication.translate("Tran", u"\u786e\u8ba4\u8f6c\u8d26", None))
    # retranslateUi

