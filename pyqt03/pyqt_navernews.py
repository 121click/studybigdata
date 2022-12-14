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
import pandas as pd # csv save 해야지


# 클래스 OOP
class qTemplate(QWidget):    
    start = 1
    maxDisplay = 100
    saveResult = [] # w저장할 때 담음 데이터 - 딕셔너리 리스트 > DataFrame

    #생성자
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./pyqt03/navernews_2.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None: #위젯들에 대한 정의, 이벤트 시그널 처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)
        # 22.08.18 추가버튼 이벤트 시그널 확장
        self.btnNext.clicked.connect(self.btnNextClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)

    def btnNextClicked(self) -> None:
        self.start = self.start + self.maxDisplay
        self.btnSearchClicked()

    def btnSaveClicked(self) -> None:
        if len(self.saveResult) > 0:
            df = pd.DataFrame(self.saveResult)
            df.to_csv(f'./pyqt03/{self.txtSearch.text()}_뉴스검색결과.csv', encoding='utf-8', index=True)
            QMessageBox.information(self, '저장', '저장되었습니다.')

            # 저장 후 모든 변수 초기화
            self.saveResult = []
            self.start = 1
            self.txtSearch.setText('')
            self.lblStatus.setText('Data: 0 / 0')
            self.lblStatus2.setText('저장된 데이터: 0개')
            # self.tblResult.setRawCount(0)
            self.tblResult.clearContents()
            self.btnNext.setEnabled(True)


    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        link = self.tblResult.item(selected, 1).text() # 선택된 열의 링크
        webbrowser.open(link)


    def btnSearchClicked(self) -> None: # 슬롯(이벤트 핸들러)
        jsonResult=[]
        totalResult=[]
        keyword = 'news'
        search_word = self.txtSearch.text()


        jsonResult = self.getNaverSearch(keyword, search_word, self.start, self.maxDisplay)
        
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post)) 
        # print(totalResult)

        self.makeTable(totalResult) # QTableWidget 에 데이터 뿌리기
        
    # saveResult value할당 lblStatus 값표시
        total = jsonResult['total']
        curr = self.start + self.maxDisplay - 1
        self.lblStatus.setText(f'Data: {curr} / {total}')

        #saveResult 변수에 저장할 데이터를 복사
        
        for post in totalResult:
            self.saveResult.append(post[0])     
        self.lblStatus2.setText(f'저장된 데이터: {len(self.saveResult)}개')
            
        if curr >= 1000:
            self.btnNext.setDisabled(True)
        else:
            self.btnNext.setEnabled(True)


    def makeTable(self, result):

        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result)) #50개, display_count가 지금은 50개
        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])
        self.tblResult.setColumnWidth(0, 350)
        self.tblResult.setColumnWidth(1, 100)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 편집모드 불가, read only

        i = 0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            link = item[0]['originallink']
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(link))           
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

    def getPostData(self, post):
        temp = []
        title = self.strip_tag(post['title'])
        description = post['description']
        originallink = post['originallink']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({'title':title, 
        'description':description, 
        'originallink':originallink, 
        'link':link, 
        'pubDate':pubDate}) # 220818 pubDate 빠진 것 추가

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
    ins = qTemplate()
    app.exec_()
