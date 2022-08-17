# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ttask.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setFamily(u"D2Coding")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(20, 20, 191, 31))
        self.txbLog = QTextBrowser(self.centralwidget)
        self.txbLog.setObjectName(u"txbLog")
        self.txbLog.setGeometry(QRect(20, 60, 741, 391))
        self.pgbTask = QProgressBar(self.centralwidget)
        self.pgbTask.setObjectName(u"pgbTask")
        self.pgbTask.setGeometry(QRect(20, 490, 741, 23))
        self.pgbTask.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"start", None))
    # retranslateUi

