# 할리스 커피숍 매장정보 크롤링

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def hollysStoreInfo(result):

    for page in range(1,54):
        hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        # print(hollys_url)
        html = urllib.request.urlopen(hollys_url)
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.find('tbody')

        for store in tbody.find_all('tr'):
            if len(store) <= 3:
                break

            store_td = store.find_all('td')

            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string

        result.append([store_name]+[store_sido]+[store_address]+[store_phone])

# result

print('완료!')


def main():
    result = []
    print('할리스 커피숍 매장정보 크롤링 시작')
    
    hollysStoreInfo(result)

    #pandas dataFrame
    columns = ['store_name', 'store_sido', 'store_address', 'store_phone']
    hollys_df = pd.DataFrame(result, columns=columns)

    # 상대경로
    # hollys_df.to_csv('./hollys_shop_info.csv', index=True, encoding='utf-8')

    # 절대경로
    hollys_df.to_csv('C:/localRepository/studybigdata/day03/hollys_shop_info2.csv', index=True, encoding='utf-8')
        # index 앞에 1,2,3,4... 넣는거 T/F
    
    print('saved!')

    del result[:]



if __name__ == '__main__':
    main()




# for page in range(1,54):
#     Hollys_url = 'https://www.hollys.co.kr/store/store_list.html?page=' + str(page)

