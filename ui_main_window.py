# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 660)
        MainWindow.setStyleSheet(u"background-color: rgb(201, 241, 238);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setStyleSheet(u"background-color: rgb(171, 236, 231 );\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.mainframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.mainframe)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.tableView_2 = QTableView(self.mainframe)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setStyleSheet(u"QTableView{\n"
"border: 1px solid rgb(61, 164, 155);\n"
"border-radius: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.tableView_2)

        self.label = QLabel(self.mainframe)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.mainframe)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: white")

        self.verticalLayout.addWidget(self.comboBox)

        self.tableView = QTableView(self.mainframe)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView{\n"
"border: 1px solid rgb(61, 164, 155);\n"
"border-radius: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.tableView)


        self.verticalLayout_2.addWidget(self.mainframe)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.pushButton_3.setLocale(QLocale(QLocale.Ukrainian, QLocale.Ukraine))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_2.setLocale(QLocale(QLocale.Ukrainian, QLocale.Ukraine))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.pushButton.setLocale(QLocale(QLocale.Ukrainian, QLocale.Ukraine))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043a\u0435\u0440 \u0412\u0438\u0442\u0440\u0430\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0456\u0439", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
    # retranslateUi

