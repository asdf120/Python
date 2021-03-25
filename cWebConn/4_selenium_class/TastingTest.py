from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pymysql
import requests
import json
from selenium.webdriver.common.keys import Keys
# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 자원로드될 때까지 3초 기다림
url = "https://map.naver.com/v5/search/금천구%20맛집"
driver.get(url)
#Iframe이 열리길 기다린 후 Iframe으로 스위칭
time.sleep(3)
driver.switch_to.frame('searchIframe')
#페이징
pages = driver.find_elements_by_class_name('zJJPW')
for page in pages:
    page.click()
    # 스크롤 맨아래로 내리기
    body = driver.find_element_by_css_selector('body')
    body.click()
    for i in range(11):
        print("스크롤 다운")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
    #식당 세부정보를 보기위한 클릭 버튼을 리스트에 담기
    res_list=driver.find_elements_by_class_name('Ow5Yt')
    print(len(res_list))
    for res_button in res_list:
        print(res_button)
        #클릭을 사용하면 동적 element는 작동하지 않음 enter를 사용
        res_button.send_keys(Keys.ENTER)
        time.sleep(3)
        #세부 정보Iframe은 deafult에 종속되므로 다시 default로 돌아감
        driver.switch_to.default_content()
        #세부 정보 Iframe으로 전환
        driver.switch_to.frame('entryIframe')
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        #가게 이름 가져오기
        try:
            res_name = soup.select("#_title > span._3XamX")[0].text
            print(res_name)
            raiting = soup.select('span ._1Y6hi > em')[0].text
            print(raiting)
        except:
            res_name =""
        time.sleep(1)
        #전화 번호
        try:
            res_tell = soup.select('div > span._3ZA0S')[0].text
            print(res_tell)
        except:
            res_tell=""
        #주소
        try:
            res_addr = soup.select('span._2yqUQ')[0].text
            print(res_addr)
        except:
            res_addr=""
        res_addr_temp=res_addr.split(" ")[0:4]
        addr = ""
        for temps in res_addr_temp:
            addr = addr + temps +" "
        print(addr)
        url='http://api.vworld.kr/req/address?service=address&request=getCoord&address={}&type=ROAD&key=767B7ADF-10BA-3D86-AB7E-02816B5B92E9&'.format(addr)
        r = requests.get(url)
        temp=json.loads(r.content)
        try:
            res_latitude=temp['response']['result']['point']['x']
            res_logitude=temp['response']['result']['point']['y']
            print(res_latitude)
            print(res_logitude)
        except:
            res_latitude = ""
            res_logitude = ""
        #운영시간
        try:
            res_runtime = soup.select('li._1M_Iz._2KHqk > div > div > div')[0].text
            print(res_runtime)
        except:
            try:
                driver.find_element_by_class_name('li._1M_Iz._2KHqk > div > a').send_keys(Keys.ENTER)
                time.sleep(0.2)
                res_runtime_temp=soup.select('span._20pEw')
                res_runtime = res_runtime_temp[0].text + res_runtime_temp[1].text
                print(res_runtime)
            except:
                res_runtime=""
        #분류
        try:
            res_keyword = soup.select('#_title > span._3ocDE')[0].text
            print(res_keyword)
        except:
            res_keyword=""
        driver.find_element_by_xpath('//*[contains (@href, "menu")]').click()
        #메뉴
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        shopMenu = soup.select('div > span.cbGGg')
        shopPrice = soup.select('div.UnMvu')
        # db 연결
        conn = pymysql.connect(host="localhost", user='orange', password='1234',db='WTF',charset='utf8')
        cursor = conn.cursor()
        # db 저장
        sql="""INSERT INTO restaurant (res_name,res_tell,res_addr,res_runtime,res_keyword,res_latitude,res_logitude) 
        VALUES(%s,%s,%s,%s,%s,%s,%s)"""
        data=(res_name,res_tell,res_addr,res_runtime,res_keyword,res_latitude,res_logitude)
        print(data)
        cursor.execute(sql,data)
        conn.commit()
        sql2="SELECT res_id FROM restaurant WHERE res_tell =%s"
        cursor.execute(sql2, res_tell)
        res_id = cursor.fetchall()[0]
        print("pk :",res_id)
        #메뉴와 가격 DB 입력
        for m,p in zip(shopMenu,shopPrice):
            sql3='INSERT INTO menu (res_id,menu,price) VALUES (%s,%s,%s)'
            print('메뉴명 :{}, 가격:{}'.format(m.text,p.text))
            cursor.execute(sql3, (res_id,m.text,p.text))
            conn.commit()
        conn.close()
        #searchIframe으로 돌아가기
        driver.switch_to.default_content()
        driver.switch_to.frame('searchIframe')
driver.close()