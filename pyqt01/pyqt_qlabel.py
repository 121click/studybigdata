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
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QLabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png')) # 윈도우 아이콘 지정
        label1 = QLabel('label1', self)
        label2 = QLabel('label2', self)
        label1.setStyleSheet(
            'border-width: 4px;'
            'border-style: dot-dot-dash;'
            'border-color: red;'
            'image: url(./pyqt01/image/image1.png)'
           )               

        label2.setStyleSheet(
            'border-width: 4px;'
            'border-style: dot-dot-dash;'
            'border-color: red;'
            'image: url(./pyqt01/image/image2.png)'
           )            
        

        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
