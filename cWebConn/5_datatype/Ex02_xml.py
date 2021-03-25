"""
[예제] 기상청
    http://www.weather.go.kr > 메뉴 > 생활과산업 > 서비스 > 인터넷
    RSS > 중기예보 > 전국
    크롬에서 url 확인 : http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108


 1) 서버의 부담을 줄이고자 xml파일을 다운받는다. (urllib.request.urlretrieve()이용 )
 2) 저장한 파일을 읽는다
 3) BeautifulSoup을 이용해서 파싱한다.
    [주의] xml파일을 html.parser로 분석하는데 태그명들을 소문자로 변환해서 분석하기에 이름에 주의!
"""
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# 1) 서버의 부담을 줄이고자 xml파일을 다운받는다
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "data/forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# 2) 저장한 파일을 읽는다
xml = open(savename, "r", encoding="utf-8").read()

# 3) BeautifulSoup을 이용해서 파싱한다
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)
# 4) 데이타 추출하기
info = {}
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

# 각 지역의 날씨를 구분해서 출력하기
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("| - ", name)