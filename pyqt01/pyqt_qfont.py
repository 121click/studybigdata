import sys
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


#클래스 OOP
class qtemplate(QWidget):
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Template!')
        self.text = 'FFFFFF'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        #그리는 함수 추가
        self.drawText(event, paint)
        paint.end()
    
    #텍스트 그리기 위한 사용자 함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50, 50, 50))
        paint.setFont(QFont('D2Coding', 10))
        paint.setPen(QColor(0, 34, 3))
        paint.drawText(5, 100, 'Nice')
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
