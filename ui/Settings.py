# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(380, 339)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QSize(380, 230))
        Settings.setMaximumSize(QSize(380, 500))
        icon = QIcon()
        icon.addFile(u"../materials/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        self.pb_save = QPushButton(Settings)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setGeometry(QRect(60, 290, 101, 31))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        self.pb_save.setFont(font)
        self.pb_cancel = QPushButton(Settings)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setGeometry(QRect(220, 290, 101, 31))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(10)
        self.pb_cancel.setFont(font1)
        self.gridLayoutWidget = QWidget(Settings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 341, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sb_1 = QSpinBox(self.gridLayoutWidget)
        self.sb_1.setObjectName(u"sb_1")
        self.sb_1.setMinimum(1)
        self.sb_1.setMaximum(999)
        self.sb_1.setValue(10)

        self.gridLayout.addWidget(self.sb_1, 1, 1, 1, 1)

        self.cb_1 = QCheckBox(self.gridLayoutWidget)
        self.cb_1.setObjectName(u"cb_1")
        self.cb_1.setChecked(True)

        self.gridLayout.addWidget(self.cb_1, 8, 1, 1, 1)

        self.sb_3 = QSpinBox(self.gridLayoutWidget)
        self.sb_3.setObjectName(u"sb_3")
        self.sb_3.setMaximum(9999)
        self.sb_3.setValue(2000)

        self.gridLayout.addWidget(self.sb_3, 10, 1, 1, 1)

        self.l_2 = QLabel(self.gridLayoutWidget)
        self.l_2.setObjectName(u"l_2")
        self.l_2.setFont(font1)

        self.gridLayout.addWidget(self.l_2, 2, 0, 1, 1)

        self.l_9 = QLabel(self.gridLayoutWidget)
        self.l_9.setObjectName(u"l_9")
        self.l_9.setFont(font1)
        self.l_9.setWordWrap(True)

        self.gridLayout.addWidget(self.l_9, 5, 0, 1, 1)

        self.l_8 = QLabel(self.gridLayoutWidget)
        self.l_8.setObjectName(u"l_8")
        self.l_8.setFont(font1)
        self.l_8.setWordWrap(True)

        self.gridLayout.addWidget(self.l_8, 6, 0, 1, 1)

        self.cb_3 = QCheckBox(self.gridLayoutWidget)
        self.cb_3.setObjectName(u"cb_3")

        self.gridLayout.addWidget(self.cb_3, 6, 1, 1, 1)

        self.sb_2 = QSpinBox(self.gridLayoutWidget)
        self.sb_2.setObjectName(u"sb_2")
        self.sb_2.setMaximum(999)
        self.sb_2.setValue(3)

        self.gridLayout.addWidget(self.sb_2, 2, 1, 1, 1)

        self.l_4 = QLabel(self.gridLayoutWidget)
        self.l_4.setObjectName(u"l_4")
        self.l_4.setFont(font1)
        self.l_4.setWordWrap(True)

        self.gridLayout.addWidget(self.l_4, 8, 0, 1, 1)

        self.cb_2 = QCheckBox(self.gridLayoutWidget)
        self.cb_2.setObjectName(u"cb_2")

        self.gridLayout.addWidget(self.cb_2, 3, 1, 1, 1)

        self.l_1 = QLabel(self.gridLayoutWidget)
        self.l_1.setObjectName(u"l_1")
        self.l_1.setFont(font1)

        self.gridLayout.addWidget(self.l_1, 1, 0, 1, 1)

        self.l_5 = QLabel(self.gridLayoutWidget)
        self.l_5.setObjectName(u"l_5")
        self.l_5.setFont(font1)
        self.l_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.l_5, 10, 0, 1, 1)

        self.cb_4 = QCheckBox(self.gridLayoutWidget)
        self.cb_4.setObjectName(u"cb_4")

        self.gridLayout.addWidget(self.cb_4, 5, 1, 1, 1)

        self.l_6 = QLabel(self.gridLayoutWidget)
        self.l_6.setObjectName(u"l_6")
        self.l_6.setFont(font1)

        self.gridLayout.addWidget(self.l_6, 10, 2, 1, 1)

        self.l_7 = QLabel(self.gridLayoutWidget)
        self.l_7.setObjectName(u"l_7")
        self.l_7.setFont(font1)
        self.l_7.setWordWrap(True)

        self.gridLayout.addWidget(self.l_7, 3, 0, 1, 1)

        self.l_10 = QLabel(self.gridLayoutWidget)
        self.l_10.setObjectName(u"l_10")
        self.l_10.setFont(font1)
        self.l_10.setCursor(QCursor(Qt.WhatsThisCursor))
        self.l_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.l_10, 7, 0, 1, 1)

        self.sb_4 = QSpinBox(self.gridLayoutWidget)
        self.sb_4.setObjectName(u"sb_4")
        self.sb_4.setMaximum(99)
        self.sb_4.setValue(2)

        self.gridLayout.addWidget(self.sb_4, 7, 1, 1, 1)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pb_save.setText(QCoreApplication.translate("Settings", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pb_cancel.setText(QCoreApplication.translate("Settings", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.cb_1.setText("")
        self.l_2.setText(QCoreApplication.translate("Settings", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0439 \u0434\u043b\u044f \u0441\u043b\u043e\u0432\u0430:", None))
        self.l_9.setText(QCoreApplication.translate("Settings", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0435\u043c\u044b\u0435 \u0441\u043b\u043e\u0432\u0430", None))
        self.l_8.setText(QCoreApplication.translate("Settings", u"\u0423\u043c\u043d\u043e\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0441\u043b\u043e\u0432", None))
        self.cb_3.setText("")
        self.l_4.setText(QCoreApplication.translate("Settings", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c\u0443 \u0441\u043b\u043e\u0432\u0443", None))
        self.cb_2.setText("")
        self.l_1.setText(QCoreApplication.translate("Settings", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432 \u043f\u043e-\u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e:", None))
        self.l_5.setText(QCoreApplication.translate("Settings", u"\u0447\u0435\u0440\u0435\u0437", None))
        self.cb_4.setText("")
        self.l_6.setText(QCoreApplication.translate("Settings", u"\u043c\u0441\u0435\u043a", None))
        self.l_7.setText(QCoreApplication.translate("Settings", u"\u0421\u0431\u0440\u043e\u0441 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0441\u043b\u043e\u0432\u0430, \u0435\u0441\u043b\u0438 \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u0430 \u043e\u0448\u0438\u0431\u043a\u0430", None))
#if QT_CONFIG(tooltip)
        self.l_10.setToolTip(QCoreApplication.translate("Settings", u"\u0415\u0441\u043b\u0438 \u043d\u0430 \u044d\u0442\u043e \u0441\u043b\u043e\u0432\u043e \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c \u044d\u0442\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0430\u0437, \u0442\u043e \u043e\u043d\u043e \u043d\u0430\u0447\u043d\u0451\u0442 \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0442\u044c\u0441\u044f \u0447\u0430\u0449\u0435.", None))
#endif // QT_CONFIG(tooltip)
        self.l_10.setText(QCoreApplication.translate("Settings", u"\u043f\u043e\u0440\u043e\u0433 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f", None))
    # retranslateUi

