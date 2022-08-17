# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic01.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Template(object):
    def setupUi(self, Template):
        if not Template.objectName():
            Template.setObjectName(u"Template")
        Template.resize(400, 300)
        font = QFont()
        font.setFamily(u"D2Coding")
        Template.setFont(font)
        self.btn1 = QDialogButtonBox(Template)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(290, 20, 91, 71))
        self.btn1.setOrientation(Qt.Vertical)
        self.btn1.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pushButton = QPushButton(Template)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 260, 93, 28))
        self.txt1 = QLabel(Template)
        self.txt1.setObjectName(u"txt1")
        self.txt1.setGeometry(QRect(30, 30, 64, 15))

        self.retranslateUi(Template)
        self.btn1.accepted.connect(Template.accept)
        self.btn1.rejected.connect(Template.reject)

        QMetaObject.connectSlotsByName(Template)
    # setupUi

    def retranslateUi(self, Template):
        Template.setWindowTitle(QCoreApplication.translate("Template", u"QPushbutton", None))
        self.pushButton.setText(QCoreApplication.translate("Template", u"PushButton", None))
        self.txt1.setText(QCoreApplication.translate("Template", u"121", None))
    # retranslateUi

