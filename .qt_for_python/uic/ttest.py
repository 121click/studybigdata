# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ttest.ui'
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
        self.btnstart = QPushButton(self.centralwidget)
        self.btnstart.setObjectName(u"btnstart")
        self.btnstart.setGeometry(QRect(20, 20, 191, 31))
        self.txblog = QTextBrowser(self.centralwidget)
        self.txblog.setObjectName(u"txblog")
        self.txblog.setGeometry(QRect(20, 60, 741, 391))
        self.pgbTesk = QProgressBar(self.centralwidget)
        self.pgbTesk.setObjectName(u"pgbTesk")
        self.pgbTesk.setGeometry(QRect(20, 490, 741, 23))
        self.pgbTesk.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnstart.setText(QCoreApplication.translate("MainWindow", u"start", None))
    # retranslateUi

