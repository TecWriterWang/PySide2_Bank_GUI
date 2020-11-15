# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterUI.ui'
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


class Ui_RegisterUI(object):
    def setupUi(self, RegisterUI):
        if not RegisterUI.objectName():
            RegisterUI.setObjectName(u"RegisterUI")
        RegisterUI.setEnabled(True)
        RegisterUI.resize(225, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegisterUI.sizePolicy().hasHeightForWidth())
        RegisterUI.setSizePolicy(sizePolicy)
        RegisterUI.setAnimated(True)
        self.centralwidget = QWidget(RegisterUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UITitle = QLabel(self.centralwidget)
        self.UITitle.setObjectName(u"UITitle")
        self.UITitle.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UITitle.sizePolicy().hasHeightForWidth())
        self.UITitle.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.UITitle.setFont(font)
        self.UITitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.UITitle)

        self.HName = QHBoxLayout()
        self.HName.setObjectName(u"HName")
        self.Name = QLabel(self.centralwidget)
        self.Name.setObjectName(u"Name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.Name.setFont(font1)
        self.Name.setToolTipDuration(-1)
        self.Name.setLayoutDirection(Qt.LeftToRight)
        self.Name.setLineWidth(1)
        self.Name.setScaledContents(False)
        self.Name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Name.setMargin(0)
        self.Name.setIndent(0)

        self.HName.addWidget(self.Name)

        self.InName = QLineEdit(self.centralwidget)
        self.InName.setObjectName(u"InName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.InName.sizePolicy().hasHeightForWidth())
        self.InName.setSizePolicy(sizePolicy3)
        self.InName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HName.addWidget(self.InName)


        self.verticalLayout.addLayout(self.HName)

        self.HCard = QHBoxLayout()
        self.HCard.setObjectName(u"HCard")
        self.CardID = QLabel(self.centralwidget)
        self.CardID.setObjectName(u"CardID")
        sizePolicy2.setHeightForWidth(self.CardID.sizePolicy().hasHeightForWidth())
        self.CardID.setSizePolicy(sizePolicy2)
        self.CardID.setFont(font1)
        self.CardID.setLayoutDirection(Qt.LeftToRight)
        self.CardID.setScaledContents(False)
        self.CardID.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.CardID.setMargin(0)
        self.CardID.setIndent(0)

        self.HCard.addWidget(self.CardID)

        self.InCardID = QLineEdit(self.centralwidget)
        self.InCardID.setObjectName(u"InCardID")
        sizePolicy3.setHeightForWidth(self.InCardID.sizePolicy().hasHeightForWidth())
        self.InCardID.setSizePolicy(sizePolicy3)
        self.InCardID.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HCard.addWidget(self.InCardID)


        self.verticalLayout.addLayout(self.HCard)

        self.HPasssword = QHBoxLayout()
        self.HPasssword.setObjectName(u"HPasssword")
        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")
        sizePolicy2.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy2)
        self.Password.setFont(font1)
        self.Password.setLayoutDirection(Qt.LeftToRight)
        self.Password.setScaledContents(False)
        self.Password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Password.setMargin(0)
        self.Password.setIndent(0)

        self.HPasssword.addWidget(self.Password)

        self.InPassword = QLineEdit(self.centralwidget)
        self.InPassword.setObjectName(u"InPassword")
        sizePolicy3.setHeightForWidth(self.InPassword.sizePolicy().hasHeightForWidth())
        self.InPassword.setSizePolicy(sizePolicy3)
        self.InPassword.setInputMethodHints(Qt.ImhNone)
        self.InPassword.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HPasssword.addWidget(self.InPassword)


        self.verticalLayout.addLayout(self.HPasssword)

        self.HRePassword = QHBoxLayout()
        self.HRePassword.setObjectName(u"HRePassword")
        self.RePassword = QLabel(self.centralwidget)
        self.RePassword.setObjectName(u"RePassword")
        sizePolicy2.setHeightForWidth(self.RePassword.sizePolicy().hasHeightForWidth())
        self.RePassword.setSizePolicy(sizePolicy2)
        self.RePassword.setFont(font1)
        self.RePassword.setLayoutDirection(Qt.LeftToRight)
        self.RePassword.setScaledContents(False)
        self.RePassword.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.RePassword.setMargin(0)
        self.RePassword.setIndent(0)

        self.HRePassword.addWidget(self.RePassword)

        self.ReInPassword = QLineEdit(self.centralwidget)
        self.ReInPassword.setObjectName(u"ReInPassword")
        sizePolicy3.setHeightForWidth(self.ReInPassword.sizePolicy().hasHeightForWidth())
        self.ReInPassword.setSizePolicy(sizePolicy3)
        self.ReInPassword.setInputMethodHints(Qt.ImhNone)
        self.ReInPassword.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HRePassword.addWidget(self.ReInPassword)


        self.verticalLayout.addLayout(self.HRePassword)

        self.HPhone = QHBoxLayout()
        self.HPhone.setObjectName(u"HPhone")
        self.Phone = QLabel(self.centralwidget)
        self.Phone.setObjectName(u"Phone")
        sizePolicy2.setHeightForWidth(self.Phone.sizePolicy().hasHeightForWidth())
        self.Phone.setSizePolicy(sizePolicy2)
        self.Phone.setFont(font1)
        self.Phone.setLayoutDirection(Qt.LeftToRight)
        self.Phone.setScaledContents(False)
        self.Phone.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Phone.setMargin(0)
        self.Phone.setIndent(0)

        self.HPhone.addWidget(self.Phone)

        self.InPhone = QLineEdit(self.centralwidget)
        self.InPhone.setObjectName(u"InPhone")
        sizePolicy3.setHeightForWidth(self.InPhone.sizePolicy().hasHeightForWidth())
        self.InPhone.setSizePolicy(sizePolicy3)
        self.InPhone.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HPhone.addWidget(self.InPhone)


        self.verticalLayout.addLayout(self.HPhone)

        self.HGender = QHBoxLayout()
        self.HGender.setObjectName(u"HGender")
        self.Gender = QLabel(self.centralwidget)
        self.Gender.setObjectName(u"Gender")
        sizePolicy2.setHeightForWidth(self.Gender.sizePolicy().hasHeightForWidth())
        self.Gender.setSizePolicy(sizePolicy2)
        self.Gender.setFont(font1)
        self.Gender.setLayoutDirection(Qt.LeftToRight)
        self.Gender.setScaledContents(False)
        self.Gender.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Gender.setMargin(0)
        self.Gender.setIndent(0)

        self.HGender.addWidget(self.Gender)

        self.InGender = QComboBox(self.centralwidget)
        self.InGender.addItem("")
        self.InGender.addItem("")
        self.InGender.setObjectName(u"InGender")
        self.InGender.setEnabled(True)

        self.HGender.addWidget(self.InGender)

        self.HGender.setStretch(0, 1)
        self.HGender.setStretch(1, 2)

        self.verticalLayout.addLayout(self.HGender)

        self.HEmail = QHBoxLayout()
        self.HEmail.setObjectName(u"HEmail")
        self.Email = QLabel(self.centralwidget)
        self.Email.setObjectName(u"Email")
        sizePolicy2.setHeightForWidth(self.Email.sizePolicy().hasHeightForWidth())
        self.Email.setSizePolicy(sizePolicy2)
        self.Email.setFont(font1)
        self.Email.setLayoutDirection(Qt.LeftToRight)
        self.Email.setScaledContents(False)
        self.Email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Email.setMargin(0)
        self.Email.setIndent(0)

        self.HEmail.addWidget(self.Email)

        self.InEmail = QLineEdit(self.centralwidget)
        self.InEmail.setObjectName(u"InEmail")
        sizePolicy3.setHeightForWidth(self.InEmail.sizePolicy().hasHeightForWidth())
        self.InEmail.setSizePolicy(sizePolicy3)
        self.InEmail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.HEmail.addWidget(self.InEmail)


        self.verticalLayout.addLayout(self.HEmail)

        self.btRegister = QPushButton(self.centralwidget)
        self.btRegister.setObjectName(u"btRegister")
        sizePolicy3.setHeightForWidth(self.btRegister.sizePolicy().hasHeightForWidth())
        self.btRegister.setSizePolicy(sizePolicy3)
        self.btRegister.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btRegister.setFont(font2)
        self.btRegister.setLayoutDirection(Qt.LeftToRight)
        self.btRegister.setAutoFillBackground(False)
        self.btRegister.setAutoDefault(False)

        self.verticalLayout.addWidget(self.btRegister)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        RegisterUI.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.InName, self.InCardID)
        QWidget.setTabOrder(self.InCardID, self.InPassword)
        QWidget.setTabOrder(self.InPassword, self.ReInPassword)
        QWidget.setTabOrder(self.ReInPassword, self.InPhone)
        QWidget.setTabOrder(self.InPhone, self.InGender)
        QWidget.setTabOrder(self.InGender, self.InEmail)
        QWidget.setTabOrder(self.InEmail, self.btRegister)

        self.retranslateUi(RegisterUI)

        QMetaObject.connectSlotsByName(RegisterUI)
    # setupUi

    def retranslateUi(self, RegisterUI):
        RegisterUI.setWindowTitle(QCoreApplication.translate("RegisterUI", u"注册账户", None))
        self.UITitle.setText(QCoreApplication.translate("RegisterUI", u"\u6ce8\u518c\u65b0\u8d26\u6237", None))
        self.Name.setText(QCoreApplication.translate("RegisterUI", u"\u59d3\u540d", None))
        self.CardID.setText(QCoreApplication.translate("RegisterUI", u"\u8eab\u4efd\u8bc1", None))
        self.Password.setText(QCoreApplication.translate("RegisterUI", u"\u767b\u5f55\u5bc6\u7801", None))
        self.RePassword.setText(QCoreApplication.translate("RegisterUI", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.Phone.setText(QCoreApplication.translate("RegisterUI", u"\u624b\u673a\u53f7", None))
        self.Gender.setText(QCoreApplication.translate("RegisterUI", u"\u6027\u522b", None))
        self.InGender.setItemText(0, QCoreApplication.translate("RegisterUI", u"\u7537", None))
        self.InGender.setItemText(1, QCoreApplication.translate("RegisterUI", u"\u5973", None))

        self.Email.setText(QCoreApplication.translate("RegisterUI", u"\u7535\u5b50\u90ae\u7bb1", None))
        self.btRegister.setText(QCoreApplication.translate("RegisterUI", u"\u6ce8\u518c", None))
    # retranslateUi

