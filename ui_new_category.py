# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_new_cat.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(444, 203)
        Dialog.setStyleSheet(u"background-color: rgb(201, 241, 238);")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 401, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(171, 236, 231 );\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 40, 371, 23))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_3 = QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit_3)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(171, 236, 231);\n"
"border: 1px solid rgb(61, 164, 155);\n"
"border-radius: 10px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(61, 164, 155);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(61, 164, 155);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(171, 236, 231);\n"
"border: 1px solid rgb(61, 164, 155);\n"
"border-radius: 10px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(61, 164, 155);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(61, 164, 155);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

