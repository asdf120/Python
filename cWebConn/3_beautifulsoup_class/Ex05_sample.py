"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈 : get()
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용, jsoup
"""

from bs4 import BeautifulSoup
from urllib import request as req

# 1. 데이타 가져오기
#  http://www.kma.go.kr > [생활과산업] > [서비스] > [인터넷] > RSS
rssUrl = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
res = req.urlopen(rssUrl)
# print(res)  # [결과] http.client.HTTPResponse object

# 2. 필요 데이타 추출하기
soup = BeautifulSoup(res, 'html.parser')
# print(soup) # 파싱 결과확인
# print('-'*100)

# 제목 / 도시 / 시간대별 날씨상태등 추출하여 출력
titles = soup.select('header>title')
# for title in titles:
#     print(title)

cities = soup.select('location>city')
date = soup.select('data>tmEf')
weather = soup.select('data>wf')

city = 0;
num = 0
change_city = len(date) // len(cities)
for date, weather in zip(date, weather):
    print(cities[city].text, date.text, weather.text)
    num += 1
    if change_city == num:
        num = 0
        city += 1

# 진현이꺼
# datas = soup.select('body > location')
# for i in datas:
#     print(i.select('city')[0].text) # 도시
#     for j in i.select('data'):
#         print(j.select('tmEf')[0].text ," - ",j.select('wf')[0].text)  # 시간대,날씨상태

# 영권이형
# loc = soup.select('location')
# for data in loc:
#     city = data.find('city')
#     times = data.find_all('tmef')
#     wxs = data.find_all('wf')
#     print(city.text)
#     for time, wx in zip(times,wxs):
#         print('{} : {}'.format(time.text,wx.text))

# 태양형꺼
# city = [city.text for city in soup.select('city')]
# wf = [wf.text for wf in soup.select('city ~ data > wf')]
# time = [time.text for time in soup.select('city ~ data > tmEf')]
#
# weather, temp = [], []
# for item in zip(wf, time):
#     temp.append(item)
#     if len(temp) % 13 == 0:
#         weather.append(temp)
#         temp = []
#
# for item in zip(city, weather):
#     print(f'---- {item[0]}의 날씨 시작 ----')
#     print(*item[1], sep='\n')
#     print(f'---- {item[0]}의 날씨였습니다 ----')


# 승탁님꺼
# t = soup.select('location');
# for i in t:
#     print(i.select_one('city').text);
#     print();
#     for j in i.select('data'):
#         print(j.select_one('tmEf').text);
#         print(j.select_one('wf').text);
#     print();
