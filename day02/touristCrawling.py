# Ody77GLuYeR%2FeFqbpduMN2Bi4Cka2fztbgnj6E2Eux1kUhy3e4epR28XKBUaObiqPoVzAizxXMBPXtMyuC9v9Q%3D%3D

'''데이터 포털 API 크롤링'''
import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd


ServiceKey = "Ody77GLuYeR%2FeFqbpduMN2Bi4Cka2fztbgnj6E2Eux1kUhy3e4epR28XKBUaObiqPoVzAizxXMBPXtMyuC9v9Q%3D%3D"

#CODE1

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200: #200 ok, 40X error, 50X server error
            print(f'[{datetime.datetime.now()}] Url Request Success')
            return res.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL')
        return None

def getTourismStatsItem(yyyymm, nat_cd, ed_cd):
    service_url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    # params = f'?_type=json&serviceKey={ServiceKey}&YM={yyyymm}&NAT_CD={nat_cd}&ED_CD={ed_cd}'
    
    params = f'?_type=json&serviceKey={ServiceKey}'
    params += f'&YM={yyyymm}'
    params += f'&NAT_CD={nat_cd}'
    params += f'&ED_CD={ed_cd}'
    url = service_url + params

    # print(url)
    retData = getRequestUrl(url)

    if retData == None:
        return None
    else:
        return json.loads(retData)

def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []
    result = []
    natName = ''
    dataEND =f'{nEndYear}{12:0>2}'
    isDataEnd = False #data 확인용, flag 초기화, true false 1 0 으로 가능

    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            if isDataEnd: break # if isDataEnd == True: break와 같음

            yyyymm = f'{year}{month:0>2}'
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)

            if jsonData['response']['header']['resultMsg'] == 'OK':
                # print(jsonData)
                # data가 없으면 break
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = True
                    dataEND = f'{year}{month-1:0>2}'
                    print(f'제공되는 데이터는 {year}년 {month-1}월 까지 있습니다.')
                    break

                print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '')
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']

                jsonResult.append({'nat_name':natName, 'nat_cd': nat_cd, 'yyyymm': yyyymm, 'visit_cnt': num})
                result.append([natName, nat_cd, yyyymm, num])

    return (jsonResult, result, natName, ed, dataEND)



def main():
    jsonResult = []
    result = []
    natName = ''
    ed = ''
    dataEND = ''

    print('<<국내 입국한 외국인 통계데이터 수집>>')

    nat_cd = input('국가코드를 입력하세요:  (CH 112 JP 130 USA 140 ph 155)')
    nStartYear = int(input('시작년도를 입력하세요: '))
    nEndYear = int(input('종료년도를 입력하세요: '))
    ed_cd = 'E' # D: 한국인 외래 관광객 E : 외국인 입국한 관광객
    
    (jsonResult, result, natName, ed, dataEND) = \
        getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)

    if natName == '':
        print('데이터가 없습니다. 공공데이터 포털을 확인해주세요.')
        return
    else:
        #save file as csv
        columns = ['입국국가', '국가코드', '입국연월', '입국자수']
        result_df = pd.DataFrame(result, columns=columns)
        result_df.to_csv(f'./{natName}_{ed}_{nStartYear}_{dataEND}.csv', encoding='utf8', index=False)

        print('csv file saved.')
        





        # df = pd.DataFrame(result, columns=['nat_name', 'nat_cd', 'yyyymm', 'visit_cnt'])
        # df.to_csv(f'{natName}_{ed}_{dataEND}.csv', encoding='utf-8', mode='w', index=True)
        # print(f'{natName}_{ed}_{dataEND}.csv 파일로 저장되었습니다.')




if __name__ =='__main__':
    main()
