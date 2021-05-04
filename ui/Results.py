# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Results.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Results(object):
    def setupUi(self, Results):
        if not Results.objectName():
            Results.setObjectName(u"Results")
        Results.resize(440, 300)
        Results.setMinimumSize(QSize(440, 300))
        Results.setMaximumSize(QSize(440, 300))
        self.l_grade = QLabel(Results)
        self.l_grade.setObjectName(u"l_grade")
        self.l_grade.setGeometry(QRect(20, 70, 401, 61))
        self.l_grade.setAlignment(Qt.AlignCenter)
        self.l_comment = QLabel(Results)
        self.l_comment.setObjectName(u"l_comment")
        self.l_comment.setGeometry(QRect(20, 130, 401, 51))
        self.l_comment.setAlignment(Qt.AlignCenter)
        self.l_comment.setWordWrap(True)
        self.pb_cont = QPushButton(Results)
        self.pb_cont.setObjectName(u"pb_cont")
        self.pb_cont.setGeometry(QRect(20, 200, 401, 41))
        self.pb_again = QPushButton(Results)
        self.pb_again.setObjectName(u"pb_again")
        self.pb_again.setGeometry(QRect(20, 250, 121, 31))
        self.pb_menu = QPushButton(Results)
        self.pb_menu.setObjectName(u"pb_menu")
        self.pb_menu.setGeometry(QRect(160, 250, 121, 31))
        self.pb_exit = QPushButton(Results)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(300, 250, 121, 31))
        self.l_header = QLabel(Results)
        self.l_header.setObjectName(u"l_header")
        self.l_header.setGeometry(QRect(0, 0, 440, 60))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(22)
        font.setBold(True)
        self.l_header.setFont(font)
        self.l_header.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Results)

        QMetaObject.connectSlotsByName(Results)
    # setupUi

    def retranslateUi(self, Results):
        Results.setWindowTitle(QCoreApplication.translate("Results", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.l_grade.setText(QCoreApplication.translate("Results", u"8 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0445 \u043e\u0442\u0432\u0435\u0442\u043e\u0432 \u0438\u0437 10", None))
        self.l_comment.setText(QCoreApplication.translate("Results", u"<html><head/><body><p>\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439</p></body></html>", None))
        self.pb_cont.setText(QCoreApplication.translate("Results", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435", None))
        self.pb_again.setText(QCoreApplication.translate("Results", u"\u0415\u0449\u0451 \u0440\u0430\u0437", None))
        self.pb_menu.setText(QCoreApplication.translate("Results", u"\u0412 \u043c\u0435\u043d\u044e", None))
        self.pb_exit.setText(QCoreApplication.translate("Results", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.l_header.setText(QCoreApplication.translate("Results", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

