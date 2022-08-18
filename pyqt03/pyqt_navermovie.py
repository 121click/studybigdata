import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
from urllib.parse import quote
import urllib.request
import json
import webbrowser


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
class qtemplate(QWidget):
    #생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt02/navermovie.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None: #위젯들에 대한 정의, 이벤트 시그널 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 2).text() # 선택된 열의 링크
        webbrowser.open(link)


    def btnSearchClicked(self) -> None: # 슬롯(이벤트 핸들러)
        jsonResult=[]
        totalResult=[]
        keyword = 'movie'
        search_word = self.txtSearch.text()
        display_count=100

        # QMessageBox.information(self, '검색', f'{search_word} 검색 시작합니다.')

        jsonResult = self.getNaverSearch(keyword, search_word, 1, display_count)
        # 
        
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post)) 
        # print(totalResult)

        self.makeTable(totalResult) # QTableWidget 에 데이터 뿌리기
        return # return 뒤에 아무것도 없으면 그냥 return none


    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(3)
        self.tblResult.setRowCount(len(result)) 
        self.tblResult.setHorizontalHeaderLabels(['영화제목','상영년도', '뉴스링크']) #뉴스와 비교해서 좀 바뀌었지.
        self.tblResult.setColumnWidth(0, 250)
        self.tblResult.setColumnWidth(1, 100)
        self.tblResult.setColumnWidth(2, 100) # 3번째 컬럼 길이
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 편집모드 불가, read only

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            subtitle = self.strip_tag(item[0]['subtitle'])
            pubdate = item[0]['pubDate']
            link = item[0]['link']

            self.tblResult.setItem(i, 0, QTableWidgetItem(f'{title} / {subtitle}'))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubdate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(link))
            i += 1

    def strip_tag(self, title): # html 태그 제거
        ret = title.replace('&lt;', '<')
        ret = ret.replace('&gt;', '>')
        ret = ret.replace('&quot;', '"')
        ret = ret.replace('&apos;', "'")
        ret = ret.replace('&amp;', '&')
        ret = ret.replace('<b>', '')
        ret = ret.replace('</b>', '')
        return ret

        # for i in range(len(totalResult)):
        #     for j in range(5):
        #         self.tblResult.setItem(i, j, QTableWidgetItem(totalResult[i][0][self.tblResult.horizontalHeaderItem(j).text()]))

    def getPostData(self, post):
        temp = []
        title = post['title']
        subtitle = post['subtitle']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({'title':title, 'subtitle':subtitle, 'link':link, 'pubDate':pubDate})
        return temp



    # Naver api main function

    def getNaverSearch(self, keyword, search, start, display):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json'\
            f'?query={quote(search)}&start={start}&display={display}'
        print(url)

        req = urllib.request.Request(url)
        req.add_header('X-Naver-Client-Id','SIS_2bMdjFoNkoFhBxQl')
        req.add_header('X-Naver-Client-Secret', 'toHFqL4b81')

        res = urllib.request.urlopen(req) # response로 오타냈는데 response니까 닫히고 뒤로 더 안 들어가지. 끊긴 곳 잘 찾기
        if res.getcode() == 200:
            print('정상')
        else:
            print('에러')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qtemplate()
    app.exec_()
