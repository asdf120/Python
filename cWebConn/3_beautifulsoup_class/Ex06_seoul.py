"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

from urllib import request
from bs4 import BeautifulSoup

html = 'http://www.seoul.go.kr/seoul/autonomy.do'
site = request.urlopen(html)
site1=site.read()

soup = BeautifulSoup(site1,"html.parser")

# 아래 리스트에 각 구청의 상세 정보를 저장하고 출력하기
구청이름=[]
구청주소=[]
구청전화번호=[]
구청홈페이지=[]
구청홈페이지=[]

'''
    [출력결과]
    구청이름 : xxx
    구청주소 : xxx
'''

# 승탁님
구청이름=[temp.text for temp in soup.select('.tabcont strong')];
구청주소=[temp.text for temp in soup.select('.tabcont li:first-child')];
구청전화번호=[temp.text for temp in soup.select('.tabcont li:nth-of-type(2)')];
구청홈페이지=[temp.text for temp in soup.select('.tabcont li:nth-of-type(3)')];

for a, b, c, d in zip(구청이름, 구청주소, 구청전화번호, 구청홈페이지):
    print('구청이름\t\t{}\n구청주소\t\t{}\n구청전화번호\t{}\n구청홈페이지\t{}'.format(a, b, c, d));

# 태양형
구청이름 = []
구청주소 = []
구청전화번호 = []
구청홈페이지 = []
for name in soup.select('li.tabcont > strong'):
    구청이름.append(name.text)

for index, li in enumerate(soup.select('li.tabcont > ul > li')):
    if index % 3 == 0:
        구청주소.append(li.text.replace('(우) ', ''))
    elif index % 3 == 1:
        구청전화번호.append(li.text.replace('TEL. ', ''))
    else:
        구청홈페이지.append(li.text)

for 이름, 주소, 전번, 홈피 in zip(구청이름, 구청주소, 구청전화번호, 구청홈페이지):
    print(f"""구청이름 : {이름}
구청주소 : {주소}
구청전번 : {전번}
구청홈피 : {홈피}""", end='\n--------------------------------------\n')
