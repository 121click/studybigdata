# selenium 사용하여 웹 페이지 크롤링
# package load
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

def getCoffeeBeanStoreInfo(result):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    wd = webdriver.Chrome('./day03/chromedriver.exe',options=options)
    
    # wd = webdriver.Chrome('./day03/chromedriver.exe')

    for i in range(1, 10+1):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1)
        
        try:
            wd.execute_script(f"storePop2('{i}')")
            time.sleep(0.5) # 팝업 표시하고 좀 끊었다 가야지
            html = wd.page_source
            soup = BeautifulSoup(html, 'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select('table.store_table > tbody > tr > td')
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip()
            store_contact = store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])

        except Exception as e:
            print(e)
            continue        

def main():
    result = []
    print('커피빈 매장정보 크롤링 시작')
    getCoffeeBeanStoreInfo(result)

    # #pandas dataFrame
    columns = ['store_name','store_address', 'store_contact']
    coffeebean_df = pd.DataFrame(result, columns=columns)

    # # 상대경로
    coffeebean_df.to_csv('./coffeebean_shop_info.csv', index=True, encoding='utf-8')

    # # 절대경로
    # hollys_df.to_csv('C:/localRepository/studybigdata/day03/hollys_shop_info2.csv', index=True, encoding='utf-8')
    #     # index 앞에 1,2,3,4... 넣는거 T/F
    
    print('saved!')

    del result[:]


if __name__ == '__main__':
    main()
