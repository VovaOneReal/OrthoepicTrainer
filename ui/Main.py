# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
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
        self.pb_start = QPushButton(self.centralwidget)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setGeometry(QRect(260, 410, 261, 41))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.pb_start.setFont(font1)
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
        self.l_description.setGeometry(QRect(140, 90, 511, 221))
        self.l_description.setFont(font1)
        self.l_description.setTextFormat(Qt.RichText)
        self.l_description.setWordWrap(True)
        self.pb_settings = QPushButton(self.centralwidget)
        self.pb_settings.setObjectName(u"pb_settings")
        self.pb_settings.setGeometry(QRect(700, 420, 31, 31))
        icon1 = QIcon()
        icon1.addFile(u"../materials/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_settings.setIcon(icon1)
        self.pb_settings.setIconSize(QSize(16, 16))
        self.pb_about = QPushButton(self.centralwidget)
        self.pb_about.setObjectName(u"pb_about")
        self.pb_about.setGeometry(QRect(740, 420, 31, 31))
        icon2 = QIcon()
        icon2.addFile(u"../materials/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_about.setIcon(icon2)
        self.pb_night = QPushButton(self.centralwidget)
        self.pb_night.setObjectName(u"pb_night")
        self.pb_night.setGeometry(QRect(20, 420, 31, 31))
        icon3 = QIcon()
        icon3.addFile(u"../materials/icons/night.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_night.setIcon(icon3)
        self.pb_night.setIconSize(QSize(16, 16))
        self.l_form_info = QLabel(self.centralwidget)
        self.l_form_info.setObjectName(u"l_form_info")
        self.l_form_info.setEnabled(True)
        self.l_form_info.setGeometry(QRect(100, 320, 591, 31))
        self.l_form_info.setFont(font)
        self.l_form_info.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0444\u043e\u044d\u043f\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0440\u0435\u043d\u0430\u0436\u0451\u0440", None))
        self.le_word_amount.setText("")
        self.le_word_amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0442\u0440\u0435\u043d\u0438\u0440\u0443\u0435\u043c\u044b\u0445 \u0441\u043b\u043e\u0432...", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.l_header.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0444\u043e\u044d\u043f\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0440\u0435\u043d\u0430\u0436\u0451\u0440", None))
        self.l_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u0412\u0430\u043c \u043f\u043e \u043e\u0447\u0435\u0440\u0435\u0434\u0438 \u0431\u0443\u0434\u0443\u0442 \u043f\u043e\u043a\u0430\u0437\u0430\u043d\u044b \u0441\u043b\u043e\u0432\u0430 \u0431\u0435\u0437 \u0443\u0434\u0430\u0440\u0435\u043d\u0438\u0439. \u0412\u0430\u0448\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 - \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0442\u0443 \u0433\u043b\u0430\u0441\u043d\u0443\u044e, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043f\u0430\u0434\u0430\u0435\u0442 \u0443\u0434\u0430\u0440\u0435\u043d\u0438\u0435.</p><p align=\"justify\">\u0412 \u043f\u043e\u043b\u0435 \u043d\u0438\u0436\u0435 \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0432\u0432\u0435\u0441\u0442\u0438 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c.</p></bo"
                        "dy></html>", None))
        self.pb_settings.setText("")
        self.pb_about.setText("")
        self.pb_night.setText("")
        self.l_form_info.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic;\">\u0414\u043b\u044f \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0438 \u0432\u0441\u0435\u0445 \u0441\u043b\u043e\u0432 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043b\u044c. <br/>\u0414\u043b\u044f \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u043f\u043e-\u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043f\u043e\u043b\u0435 \u043f\u0443\u0441\u0442\u044b\u043c.</span></p></body></html>", None))
    # retranslateUi

