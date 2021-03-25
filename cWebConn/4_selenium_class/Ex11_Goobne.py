"""
    [ 굽네치킨 매장 주소 가져오기 ]

    굽네치킨 http://www.goobne.co.kr > 매장찾기 > 매장찾기
                  http://www.goobne.co.kr/store/search_store.jsp

    개발자모드( F12 ) 열고 페이지 번호를 누르면
    <tbody> 부분이 교체되는 것을 볼 수 있다

    또한 2번 페이지 번호에 <a href="javascript:store.getList('2');">2</a>로 자바스트립트 함수를 호출한다.

    이 때 WebDriver 라는 특정 웹 브라우저의 원격 제어 인터페이스를 이용하고
    selenium 패키지를 이용하여  DOM  요소를 가져오거나 자바스크립트에서 제어하는 동작을 할 수 있도록 한다.
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup

# -------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3)

# 페이지 접근
driver.get('http://www.goobne.co.kr/store/search_store.jsp')

goobne_result = []

# [확인]
'''for idx in range(1,11):
    driver.execute_script('store.getList("%d")' % idx)

    time.sleep(3)
    html = driver.page_source
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    # imsi = soup.findAll("tbody#store_list")
    # imsi = soup.select("tbody#store_list")
    # imsi = soup.findAll("tbody", attrs={"id": "store_list"})
    for store in soup.findAll("tbody", attrs={"id": "store_list"}):
        # print(store)
        # 지점명
        shop_name = soup.select('tr > td:first-child')
        # print(shop_name)
        # 전화번호
        shop_call = soup.select('.store_phone')
        # print(shop_call)
        # 주소
        shop_addr = soup.select('.t_left>a')
        # print(shop_addr)
        for name, call, addr in zip(shop_name, shop_call, shop_addr):
            print('{} ({}) : {}'.format(name.text, call.text, addr.text))
            goobne_result.append([name.text,call.text,addr.text])

print('전체 매장 수 {}'.format(len(goobne_result)))
print('첫번째 출력 매장 : {}'.goobne_result[0][0])'''
'''
    [출력결과]
    지점 ( 전화번호) : 주소
'''
flag = True
idx = 1
while flag:
    driver.execute_script('store.getList("%d")' % idx)

    time.sleep(3)
    html = driver.page_source
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    # imsi = soup.findAll("tbody#store_list")
    # imsi = soup.select("tbody#store_list")
    # imsi = soup.findAll("tbody", attrs={"id": "store_list"})
    for store in soup.findAll("tbody", attrs={"id": "store_list"}):
        if '데이터' in store.text:
            flag = False
        else:
            # 지점명
            shop_name = soup.select('tr > td:first-child')
            # 전화번호
            shop_call = soup.select('.store_phone')
            # 주소
            shop_addr = soup.select('.t_left>a')
            for name, call, addr in zip(shop_name, shop_call, shop_addr):
                print('{} ({}) : {}'.format(name.text, call.text, addr.text))
                goobne_result.append([name.text, call.text, addr.text])

    idx += 1
    print(idx,flag)
