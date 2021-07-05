# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
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
        self.l_author = QLabel(About)
        self.l_author.setObjectName(u"l_author")
        self.l_author.setGeometry(QRect(30, 10, 221, 41))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(True)
        self.l_author.setFont(font)
        self.l_author.setAlignment(Qt.AlignCenter)
        self.l_link = QLabel(About)
        self.l_link.setObjectName(u"l_link")
        self.l_link.setGeometry(QRect(80, 70, 121, 21))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.l_link.setFont(font1)
        self.l_link.setAlignment(Qt.AlignCenter)
        self.l_version = QLabel(About)
        self.l_version.setObjectName(u"l_version")
        self.l_version.setGeometry(QRect(50, 110, 181, 16))
        self.l_version.setFont(font1)
        self.l_version.setAlignment(Qt.AlignCenter)
        self.pb_changelog = QPushButton(About)
        self.pb_changelog.setObjectName(u"pb_changelog")
        self.pb_changelog.setGeometry(QRect(80, 125, 121, 21))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(8)
        self.pb_changelog.setFont(font2)
        self.pb_changelog.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_changelog.setFlat(True)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.l_author.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\">\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a<br/>Vladimir T. (VovaOne)</p></body></html>", None))
        self.l_link.setText(QCoreApplication.translate("About", u"<html><head/><body><p><a href=\"https://github.com/VovaOneReal/OrthoepicTrainer\"><span style=\" text-decoration: underline; color:#0000ff;\">\u041f\u0440\u043e\u0435\u043a\u0442 \u043d\u0430 GitHub</span></a></p></body></html>", None))
        self.l_version.setText(QCoreApplication.translate("About", u"v.2.3 (\u043e\u0442 \u0425\u0425.07.21) \u00a9 2021 \u0433.", None))
        self.pb_changelog.setText(QCoreApplication.translate("About", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0439", None))
    # retranslateUi

