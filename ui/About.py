# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(280, 150)
        About.setMinimumSize(QSize(280, 150))
        About.setMaximumSize(QSize(280, 150))
        icon = QIcon()
        icon.addFile(u"../materials/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        About.setWindowIcon(icon)
        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 221, 41))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(About)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 70, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(About)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 120, 181, 16))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.label.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\">\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a<br/>Vladimir T. (VovaOne)</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><p><a href=\"https://github.com/VovaOneReal/OrthoepicTrainer\"><span style=\" text-decoration: underline; color:#0000ff;\">\u041f\u0440\u043e\u0435\u043a\u0442 \u043d\u0430 GitHub</span></a></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("About", u"v.2.0 (\u043e\u0442 02.05.21) \u00a9 2021 \u0433.", None))
    # retranslateUi

