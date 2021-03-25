from selenium import webdriver as driver
import cx_Oracle as oracle
import csv
from urllib import parse
import requests
import json
import folium
from bs4 import BeautifulSoup

driver = driver.Chrome('../webdriver/chromedriver')
idx = 1  # 페이지 수
flag = True
API_key = 'FC54F0D4-2256-3334-8485-4F36E223A257'  # 웹 API 발급받은 키


def show_map():
    location_list = ['전체','서울', '경기', '강원', '경남', '경북', '광주', '대구', '부산', '세종특별자치시', '울산', '인천', '전남',
                     '전북', '제주특별자치도', '충남', '충북', ]
    print(location_list)
    city = input('지역을 입력해 주세요 : ')

    # 입력한 지역이 location_list에 있으면 실행
    if city in location_list:
        with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
            with conn.cursor() as cursor:
                if city == '전체':
                    sql = """
                        SELECT name, addr, longitude, latitude
                        FROM CHICKEN_STORE
                    """
                else:
                    sql = """
                        SELECT name, addr, longitude, latitude
                        FROM CHICKEN_STORE
                        WHERE addr like '{}%'
                        """.format(city)  # 입력한 지역에 대한 정보를 가져옴

                cursor.execute(sql)
                stores = cursor.fetchall()

        map_location = folium.Map(location=[float(stores[3][3]), float(stores[3][2])], zoom_start=10)
        for store in stores:
            folium.Circle(location=[float(store[3]), float(store[2])], popup=store[0],
                          radius=25,
                          color='red',
                          fill='crimson').add_to(map_location)

        map_location.save('./store_location_{}.html'.format(city))  # 지역별로 html 저장
    # 입력한 지역이 없으면 show_map() 재실행
    else:
        print('다시선택')
        show_map()

show_map()
# 데이터베이스 저장 함수
def save_db():
    # 오라클연결
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            with open('60chicken_list.csv', 'r', encoding='utf-8') as file:
                store = csv.reader(file)  # csv파일을 읽어옴
                for info in store:
                    sql = """INSERT INTO CHICKEN_STORE( name, call, addr, longitude, latitude)
                            VALUES ( :1, :2, :3, :4, :5)"""

                    # 매장중에 좌표가 없는 매장이 있어서 try except 처리
                    try:
                        # 좌표를 얻어오기 위한 웹 api 이용
                        html = requests.get(
                            "http://api.vworld.kr/req/address?service=address&request=getCoord&type=ROAD&key={}&address={}".format(
                                API_key, parse.quote(info[2][3:])))
                        json_data = json.loads(html.text)
                        longitude = json_data['response']['result']['point']['x']
                        latitude = json_data['response']['result']['point']['y']
                    except:
                        print(info[0], '좌표에러')

                    cursor.execute(sql, (info[0], info[1], info[2], longitude, latitude))

                    conn.commit()

    show_map()  # 저장 완료 후, show_map() 호출


while flag:  # flag가 True일동안 실행
    # 페이지의 정보를 얻어옴
    driver.get('http://www.60chicken.com/bbs/board.php?bo_table=store&page={}&si=&gu=&dong='.format(idx))

    # 해당 페이지가 63까지 있는것을 확인후, 63전까지 해당 코드실행
    if idx is not 63:
        html = driver.page_source  # 페이지 정보를 받아옴
        soup = BeautifulSoup(html, 'html.parser')  # html 파싱

        # 매장 이름, 전화번호, 주소를 가져옴
        shop_name = soup.select('td.td_subject>a')
        shop_call = soup.select('td.td_subject > span > a')
        shop_addr = soup.select('td.td_location')

        for name, call, addr in zip(shop_name, shop_call, shop_addr):
            store = '{} ({}) : {}'.format(name.text.replace(' ', '').strip(),
                                          call.text.replace(' ', ''),
                                          addr.text.strip())
            # 텍스트 파일로 저장
            with open('60chicken_list.txt', 'a', encoding='utf-8') as file:
                file.write(store + '\n')
            # csv 파일로 저장
            with open('60chicken_list.csv', 'a', encoding='utf-8', newline='') as file:
                w = csv.writer(file)
                w.writerow([name.text.replace(' ', '').strip(),
                            call.text.replace(' ', ''),
                            addr.text.strip()])

    else:  # 페이지의 끝인 경우
        flag = False  # flag를 false로 저장하고 while문 종료
        print("페이지가 없음")
        save_db()  # save_db()함수 실행

    idx += 1  # 페이지 데이터 저장이 끝나면 +1씩 증가
