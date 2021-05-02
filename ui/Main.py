# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(790, 470)
        MainWindow.setMinimumSize(QSize(790, 470))
        MainWindow.setMaximumSize(QSize(790, 470))
        icon = QIcon()
        icon.addFile(u"../materials/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.le_word_amount = QLineEdit(self.centralwidget)
        self.le_word_amount.setObjectName(u"le_word_amount")
        self.le_word_amount.setGeometry(QRect(260, 360, 261, 41))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        self.le_word_amount.setFont(font)
        self.le_word_amount.setFocusPolicy(Qt.ClickFocus)
        self.le_word_amount.setAlignment(Qt.AlignCenter)
        self.b_start = QPushButton(self.centralwidget)
        self.b_start.setObjectName(u"b_start")
        self.b_start.setGeometry(QRect(260, 410, 261, 41))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.b_start.setFont(font1)
        self.l_header = QLabel(self.centralwidget)
        self.l_header.setObjectName(u"l_header")
        self.l_header.setGeometry(QRect(0, 0, 791, 81))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(22)
        font2.setBold(True)
        self.l_header.setFont(font2)
        self.l_header.setAlignment(Qt.AlignCenter)
        self.l_description = QLabel(self.centralwidget)
        self.l_description.setObjectName(u"l_description")
        self.l_description.setGeometry(QRect(100, 100, 581, 241))
        self.l_description.setFont(font1)
        self.l_description.setTextFormat(Qt.RichText)
        self.l_description.setWordWrap(True)
        self.b_settings = QPushButton(self.centralwidget)
        self.b_settings.setObjectName(u"b_settings")
        self.b_settings.setGeometry(QRect(700, 420, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"../materials/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_settings.setIcon(icon1)
        self.b_settings.setIconSize(QSize(16, 16))
        self.b_about = QPushButton(self.centralwidget)
        self.b_about.setObjectName(u"b_about")
        self.b_about.setGeometry(QRect(740, 420, 31, 31))
        icon2 = QIcon()
        icon2.addFile(u"../materials/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_about.setIcon(icon2)
        self.b_night = QPushButton(self.centralwidget)
        self.b_night.setObjectName(u"b_night")
        self.b_night.setGeometry(QRect(20, 420, 31, 31))
        icon3 = QIcon()
        icon3.addFile(u"../materials/icons/night.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_night.setIcon(icon3)
        self.b_night.setIconSize(QSize(16, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0444\u043e\u044d\u043f\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0440\u0435\u043d\u0430\u0436\u0451\u0440 v.2.0", None))
        self.le_word_amount.setText("")
        self.le_word_amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0442\u0440\u0435\u043d\u0438\u0440\u0443\u0435\u043c\u044b\u0445 \u0441\u043b\u043e\u0432...", None))
        self.b_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.l_header.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0444\u043e\u044d\u043f\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0440\u0435\u043d\u0430\u0436\u0451\u0440", None))
        self.l_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u0412\u0430\u043c \u043f\u043e \u043e\u0447\u0435\u0440\u0435\u0434\u0438 \u0431\u0443\u0434\u0443\u0442 \u043f\u043e\u043a\u0430\u0437\u0430\u043d\u044b \u0441\u043b\u043e\u0432\u0430 \u0431\u0435\u0437 \u0443\u0434\u0430\u0440\u0435\u043d\u0438\u0439. \u0412\u0430\u0448\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 - \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u0443 \u0433\u043b\u0430\u0441\u043d\u0443\u044e, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043f\u0430\u0434\u0430\u0435\u0442 \u0443\u0434\u0430\u0440\u0435\u043d\u0438\u0435.</p><p align=\"justify\">\u0412 \u043f\u043e\u043b\u0435 \u043d\u0438\u0436\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0432\u0432\u0435\u0441\u0442\u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c.</p><p a"
                        "lign=\"justify\"><span style=\" font-style:italic;\">\u0412\u0432\u0435\u0434\u044f &quot;0&quot;, \u0432\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u0435 \u0441\u043b\u043e\u0432\u0430.<br/>\u041e\u0441\u0442\u0430\u0432\u0438\u0432 \u0432\u0432\u043e\u0434 \u043f\u0443\u0441\u0442\u044b\u043c, \u0432\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432 \u043f\u043e-\u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e.</span></p></body></html>", None))
        self.b_settings.setText("")
        self.b_about.setText("")
        self.b_night.setText("")
    # retranslateUi

