from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


#클래스 OOP
class qtemplate(QDialog):
    #생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui', self)
        
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None: #return None 임
        # self.label = QLabel('QpushButton', self)
        # self.label.setGeometry(40, 10, 600, 40)
        pass

    
    # event = signal (python)
    def btn1_clicked(self):
        # QMessageBox.information(self, 'signal', 'clicked', 'self.btn1_clicked')
        # QMeassageBox.warning(self, 'signal', 'clicked', 'self.btn1_clicked')
        self.label.setText('메시지 : btn1 click')
        QMessageBox.critical(self, 'signal', 'self.btn1_clicked') #에러창

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
