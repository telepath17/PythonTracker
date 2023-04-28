# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(463, 363)
        Dialog.setStyleSheet(u"background-color: rgb(201, 241, 238);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 441, 281))
        self.frame.setStyleSheet(u"background-color: rgb(171, 236, 231 );\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 401, 221))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: white;\n"
"")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: white;")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: white;")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"background-color: white;")
        self.dateEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEdit)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 300, 441, 54))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget1)
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

        self.pushButton_3 = QPushButton(self.layoutWidget1)
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


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u043c\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

