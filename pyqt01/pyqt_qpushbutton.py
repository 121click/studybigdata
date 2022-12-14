from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


#클래스 OOP
class qtemplate(QWidget):
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 640, 480) # ax ay w h
        self.setWindowTitle('QpushButton')
        
        self.show()

    def addControls(self) -> None: #return None 임
        self.label = QLabel('QpushButton', self)
        self.label.setGeometry(10, 10, 600, 40)
        btn1 = QPushButton('Click addcontrol', self)
        btn1.setGeometry(520, 440, 120, 40) # ax ay aw ah

        self.btn1 = QPushButton('Click', self)
        self.btn1.setGeometry(10, 440, 120, 40) # ax ay aw ah
        self.btn1.clicked.connect(self.btn1_clicked)
        # self.btn1.clicked.connect(self.btn1_clicked) # when clicked, connect this method, attach signal
    
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
