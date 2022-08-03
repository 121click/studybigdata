from encodings.utf_8 import encode
import os
import sys
import urllib.request
import datetime
import json
import time

client_id = 'SIS_2bMdjFoNkoFhBxQl'
client_secret = 'toHFqL4b81'


'''after connect request from url, response return f'''

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200: #200 ok, 40X error, 50X server error
            print(f'[{datetime.datetime.now()}] Url Request Success')
            return res.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL')
        return None


'''핵심 함수, 네이버 API 검색'''

def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'
    text = urllib.parse.quote(srcText)
    params = f'?query={text}&start={start}&display={display}'
    
    url = base + node + params
    resDecode = getRequestUrl(url)

    if resDecode == None:
        return None
    else:
        return json.loads(resDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']

    pubDate = datetime.datetime.strptime(post['pubDate'],'%a, %d %b %Y %H:%M:%S +0900')
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:%S') #2022-08-02 15:57:99
    
    jsonResult.append({'cnt':cnt,  'title':title,'pDate':pubDate, 'link':link, 'originallink':originallink,
     'description':description, 'pDate':pubDate})
    return jsonResult


'''실행 최초 함수'''

def main():
    node = 'news'
    srcText = input('검색어를 입력하세요: ')
    cnt = 0
    jsonResult = []
    
    jsonRes = getNaverSearch(node, srcText, 1, 50)
    #print (jsonRes)
    total = jsonRes['total']

    while((jsonRes != None) and (jsonRes['display'] != 0)):
        for post in jsonRes['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt) #jsonRes랑 jsonResult랑 여기선 다른거야.

        start = jsonRes['start'] + jsonRes['display'] #1+50, 
        jsonRes = getNaverSearch(node, srcText, start, 50)

    print(f'전체 검색 : {total}건')

    #file output

    with open(f'./{srcText}.json', mode= 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, sort_keys = True, ensure_ascii=False, indent=4)
        outfile.write(jsonFile)

    print(f'{cnt} 건 가져옴')
    print(f'./{srcText}.json SAVED')


if __name__ == '__main__':
    main()

