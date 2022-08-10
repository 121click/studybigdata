from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
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
        btn1 = QPushButton('Click', self)
        btn1.setGeometry(520, 440, 120, 40) # ax ay aw ah


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
