"""
[ 1단계 ] 조별
    통닭 / 피자 / 햄버거 프랜차이즈 중 하나 선택
    매장명, 전화번호, 주소를 크롤링하여
    파일에 저장하고 DB 저장하기
    (오라클 or mariadb)
------------------------------------------------------
매장명ㅣ전화번호ㅣ주소ㅣ위도ㅣ경도
가산   02-2222 가산
[ 2단계 ]
DB에 위도, 경도 컬럼을 추가
주소를 입력하면 위도, 경도를 알 수 있는 사이트를 연결하여
DB에 해당의 주소 경도, 위도
ex) https://www.vworld.kr/dev/v4api.do
------------------------------------------------------
매장명ㅣ전화번호ㅣ주소ㅣ위도ㅣ경도
가산   02-2222 가산  xxx  yyy
[ 3단계 ]
매장명과 위도, 경도를 가지고 지도 위에 출력하기
"""
# 0. 필요한 pkg 불러오기
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
import cx_Oracle as oracle
import requests
from urllib import parse
import folium
from folium.plugins import MarkerCluster
import time
# 1. 웹 드라이버 객체 생성
driver = webdriver.Chrome('../webdriver/chromedriver')
driver.implicitly_wait(3)
# 2. 페이지 접근
driver.get('http://60chicken.com/bbs/board.php?bo_table=store&page=1&si=&gu=&dong=')
# 3. 데이터 저장을 위해 리스트 생성
chicken60_result = []
# temp 폴더가 없으면 폴더 생성
storeList = Path('temp')
if not storeList.exists():
    storeList.mkdir()
# ------------------------------------------------------------------------
# 홈페이지에서 지점 리스트 가져오기
# 페이지 번호 지정
pageno = 1
while pageno:
    # 드라이버 가져오는 것을 조금 기다리고
    driver.implicitly_wait(3)
    # page 코드를 가져오고
    html = driver.page_source
    # BeautifulSoup 으로 쪼개고
    soup = BeautifulSoup(html, 'html.parser')
    # table 의 값을 가져오는데
    for tr in soup.select('table'):
        # 지점
        store = soup.select('td.td_subject > a')
        # 주소
        addr = soup.select('td.td_location')
        # 전번
        tel = soup.select('td.td_tel')
        # 을 가져와서 csv 파일에 저장 // 파일 한글 처리
        with open('./temp/storeList.csv', 'a', encoding='utf-8-sig', newline='') as f:
            for s, a, t in zip(store, addr, tel):
                # 아까 만들어놓은 리스트에도 추가
                chicken60_result.append([s.text.strip(), a.text.strip()[:2], a.text.strip(), t.text.strip()])
                f.write('{}, {}, {}, {}\n'.format(
                    s.text.replace(',', '.').strip(),
                    a.text.replace(',', '.').strip()[:2],
                    a.text.replace(',', '.').strip(),
                    t.text.replace(',', '.').strip()
                ))
    # 다음 페이지를 보러 ㄱㄱ
    pageno += 1
    driver.get('http://60chicken.com/bbs/board.php?bo_table=store&page={}&si=&gu=&dong='.format(pageno))
    # 근데 다음 페이지가 없다면 반복문 멈춤
    nowpageno = soup.select('strong.pg_current')
    if len(nowpageno) == 0:
        break
# ------------------------------------------------------------------------
# db에 지점명과 주소, 연락처 입력
# db 연결
with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
    with conn.cursor() as cursor:
        # 아까 만든 리스트에서 하나씩 꺼내서 db에 입력
        for c in chicken60_result:
            sql = """ INSERT INTO sixty_chicken(seq, store, area, addr, tel)
                    VALUES(sixty_chicken_seq.nextval, :v_store, :v_area, :v_addr, :v_tel) """
            v_store = c[0]
            v_area = c[1]
            v_addr = c[2]
            v_tel = c[3]
            cursor.execute(sql, (v_store, v_area, v_addr, v_tel))
            conn.commit()
# ------------------------------------------------------------------------
# db에 좌표값 입력
# DB 연결
with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
    with conn.cursor() as cursor:
        # 좌표찾기 웹페이지 열고
        driver.get('http://0ff.kr/api_/d_geocode_new.php?addr=')
        # 리스트에서 주소를 가져와서
        for ad in chicken60_result:
            # 페이지에 주소를 입력 후 좌표찾기 버튼 클릭
            driver.execute_script('document.getElementsByName("addr")[0].value=\"' + ad[2] + '\"')
            driver.find_element_by_class_name('input_submit').click()
            # 결과 페이지의 소스 가져온 후, BeautifulSoup 으로 쪼개고
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            # x, y 좌표값 찾고
            lat = soup.select('body > div.sub > div:nth-child(4) > table.d_geocode_info_tb > tbody > tr:nth-child(6) > td')
            long = soup.select('body > div.sub > div:nth-child(4) > table.d_geocode_info_tb > tbody > tr:nth-child(7) > td')
            v_x = lat[0].text
            v_y = long[0].text
            v_ad = ad[2]
            # # 좌표가 null 인 값 처리
            # # > null 값은 '~~호' 처럼 호수가 있을 때 생김
            # # > 정규식으로 가능할 것 같기도 하고
            # for i in v_ad.split(' '):
            #     if '호' in i:
            #         print('★'*50, i)
            #         i = ''
            #         print('☆'*50 + i + '☆'*5)
            #     a = i, end=''
            #     print('a!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:', a)
            # db에 업뎃
            sql = "UPDATE sixty_chicken SET latitude='{}', longitude='{}' WHERE addr='{}'".format(v_x, v_y, v_ad)
            cursor.execute(sql)
            conn.commit()
# ------------------------------------------------------------------------
# 지도 만들기
# 크롬 창 띄우지 않고 불러오기 위해 option 사용
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
# 구글 지도를 불러온 후 현 위치 좌표가 찍힐때까지 대기
driver = webdriver.Chrome('../webdriver/chromedriver', chrome_options=options)
driver.get('https://www.google.co.kr/maps/')
time.sleep(5)
# 현재 url 을 가져와서 좌표 값 변수에 지정
url = driver.current_url
nowX = url[31:36]
nowY = url[42:48]
print('현재위치 x:{} // y:{}'.format(nowX, nowY))
# 현재 위치를 기반으로하는 지도 생성
map_temp = folium.Map(location=[nowX, nowY], zoom_start=15, tiles='Stamen Toner')
# db 에서 좌표 값 불러오기
with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
    with conn.cursor() as cursor:
        # 만들어놓은 리스트 사용
        for store in chicken60_result:
            # 검색 기준은 지점명
            v_store = store[0]
            sql = "SELECT latitude, longitude FROM sixty_chicken WHERE store= :0"
            cursor.execute(sql, (v_store,))
            xy = cursor.fetchall()
            # 지도에 marker 띄우기
            try:
                # # marker cluster 시도 > 실패
                # https://oboki.net/workspace/python/folium-%EC%A7%80%EB%A6%AC%EC%A0%95%EB%B3%B4-%EC%8B%9C%EA%B0%81%ED%99%94/
                # marker_cluster = MarkerCluster().add_to(map_temp)
                # 지도에 지점 좌표 찍기
                folium.Marker(
                    location=[xy[0][0], xy[0][1]],
                    popup=v_store,
                    icon=folium.Icon(color='blue', icon='star')
                ).add_to(map_temp)
            except Exception as e:
                print('error :', e)
            else:
                continue
# 만들어놓은 지도 저장
map_temp.save('./temp/map5.html')
# 끝!
print('=' * 50)
# 60계 치킨 매장 개수는?
print('60계 치킨 매장 개수는?', len(chicken60_result))