# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navernews.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"D2Coding")
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u"naver_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 451, 81))
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 30, 431, 28))
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.splitter.addWidget(self.label)
        self.txtSearch = QLineEdit(self.splitter)
        self.txtSearch.setObjectName(u"txtSearch")
        self.splitter.addWidget(self.txtSearch)
        self.btnSearch = QPushButton(self.splitter)
        self.btnSearch.setObjectName(u"btnSearch")
        self.splitter.addWidget(self.btnSearch)
        self.tblResult = QTableWidget(Form)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setGeometry(QRect(10, 100, 451, 341))
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\ub124\uc774\ubc84 \ub274\uc2a4 \uac80\uc0c9", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Search", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9\uc5b4", None))
        self.btnSearch.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9\uc5b4", None))
    # retranslateUi

