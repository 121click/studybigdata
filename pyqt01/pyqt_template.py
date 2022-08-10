import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


#클래스 OOP
class qtemplate(QWidget):
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Template!')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
