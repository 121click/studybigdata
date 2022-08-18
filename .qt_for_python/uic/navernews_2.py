# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navernews_2.ui'
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
        Form.resize(650, 515)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(650, 515))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u"naver_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 631, 80))
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 30, 421, 28))
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
        self.btnNext = QPushButton(self.groupBox)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(580, 30, 31, 28))
        self.tblResult = QTableWidget(Form)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setGeometry(QRect(10, 100, 631, 371))
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(0)
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(532, 480, 111, 28))
        self.lblStatus = QLabel(Form)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setGeometry(QRect(10, 490, 251, 16))
        self.lblStatus2 = QLabel(Form)
        self.lblStatus2.setObjectName(u"lblStatus2")
        self.lblStatus2.setGeometry(QRect(280, 490, 241, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\ub124\uc774\ubc84\ub274\uc2a4 \uac80\uc0c9", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Search", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9\uc5b4", None))
#if QT_CONFIG(tooltip)
        self.btnSearch.setToolTip(QCoreApplication.translate("Form", u"\uc0c8\ub85c\uac80\uc0c9", None))
#endif // QT_CONFIG(tooltip)
        self.btnSearch.setText(QCoreApplication.translate("Form", u"\uac80\uc0c9", None))
#if QT_CONFIG(tooltip)
        self.btnNext.setToolTip(QCoreApplication.translate("Form", u"\uacc4\uc18d\uac80\uc0c9", None))
#endif // QT_CONFIG(tooltip)
        self.btnNext.setText(QCoreApplication.translate("Form", u">", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"\ub370\uc774\ud130\uc800\uc7a5", None))
        self.lblStatus.setText(QCoreApplication.translate("Form", u"Data : ", None))
        self.lblStatus2.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5\ud560\ub370\uc774\ud130 >", None))
    # retranslateUi

