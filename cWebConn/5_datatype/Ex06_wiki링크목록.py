from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Christopher_Columbus')
bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

'''
links = bs.find_all('a')
print(len(links))
for link in links:
    if 'href' in link.attrs:   # 속성값 중에 href 속성이 있으면
        print(link.attrs['href'])
'''

# 불필요한 링크목록들이 많아서 제외한다
# /wiki/로 지정하고 특수문자(,?,!,:,),. 가 포함된 url 만 수집
import re

links = bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
print(len(links))
for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])