# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Training.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Training(object):
    def setupUi(self, Training):
        if not Training.objectName():
            Training.setObjectName(u"Training")
        Training.resize(790, 470)
        Training.setMinimumSize(QSize(790, 470))
        Training.setMaximumSize(QSize(790, 470))
        Training.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar = QProgressBar(Training)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(-10, 450, 811, 23))
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.l_header = QLabel(Training)
        self.l_header.setObjectName(u"l_header")
        self.l_header.setGeometry(QRect(0, 0, 791, 81))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(22)
        font.setBold(True)
        self.l_header.setFont(font)
        self.l_header.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(Training)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 219, 771, 81))
        self.lo_training = QHBoxLayout(self.horizontalLayoutWidget)
        self.lo_training.setObjectName(u"lo_training")
        self.lo_training.setContentsMargins(0, 0, 0, 0)
        self.l_example = QLabel(Training)
        self.l_example.setObjectName(u"l_example")
        self.l_example.setGeometry(QRect(16, 320, 761, 41))
        self.l_example.setAlignment(Qt.AlignCenter)
        self.pb_next = QPushButton(Training)
        self.pb_next.setObjectName(u"pb_next")
        self.pb_next.setGeometry(QRect(180, 380, 431, 41))
        self.pb_back = QPushButton(Training)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setGeometry(QRect(10, 10, 31, 31))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(51, 153, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush2 = QBrush(QColor(240, 240, 240, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
        self.pb_back.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"../materials/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_back.setIcon(icon)
        self.pb_back.setIconSize(QSize(16, 16))
        self.l_stats = QLabel(Training)
        self.l_stats.setObjectName(u"l_stats")
        self.l_stats.setGeometry(QRect(180, 430, 431, 20))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.l_stats.setFont(font1)
        self.l_stats.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Training)

        QMetaObject.connectSlotsByName(Training)
    # setupUi

    def retranslateUi(self, Training):
        Training.setWindowTitle(QCoreApplication.translate("Training", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.progressBar.setFormat(QCoreApplication.translate("Training", u"%v \u0438\u0437 %m", None))
        self.l_header.setText(QCoreApplication.translate("Training", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.l_example.setText(QCoreApplication.translate("Training", u"TextLabel", None))
        self.pb_next.setText(QCoreApplication.translate("Training", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.pb_back.setText("")
        self.l_stats.setText(QCoreApplication.translate("Training", u"000 / 000 / 000", None))
    # retranslateUi

