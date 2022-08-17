import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time


# UI 쓰레드와 작업 쓰레드 분리
class Worker(QThread):
    # QThread는 화면을 그릴 권한이 없어.
    # 화면을 그릴 권한이 있는 클래스에게 그릴 수 있도록 signal을 보내야 함., 통신 통해서 그릴 수 있도록.
    valChangeSignal = pyqtSignal(int) # 
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.working = True # 클래스 내부변수 working 을 지정
    
    def run(self):
        while self.working:
            for i in range(1000000):
                print(f'출력: {i}')
                # self.pgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i) # ui thread에게 화면 그리라고 signal
                time.sleep(0.0001) # 1ms



#클래스 OOP
class qtemplate(QMainWindow):
    #생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/ttask.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None: #return None 임
        self.btnStart.clicked.connect(self.btn1_clicked)
        # Worker 클래스를 생성하고, start() 메서드를 호출하여 쓰레드를 시작
        self.worker = Worker(self)
        self.worker.valChangeSignal.connect(self.updateProgress) # signal을 받아서 처리하는 부분 'updateProgress'


    @pyqtSlot(int) # decorator, 없어도 되긴 하지만 혹시 모르니까.
    def updateProgress(self, val): # signal을 받아서 처리하는 부분 val이 Worker 쓰레드에서 전달받은 반복값
        self.pgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 999999:
            self.worker.working = False

        

           
    # event = signal (python)
    def btn1_clicked(self):
       self.txbLog.append('실행!')
       self.pgbTask.setRange(0, 999999) # 응답없음! 아마도...?
       self.worker.start()
       self.worker.working = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
