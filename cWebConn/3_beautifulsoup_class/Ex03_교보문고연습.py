'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''

from urllib.request import *
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("https://search.kyobobook.co.kr/web/search?vPstrKeyWord=python&orderClick=LAG")

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# titles = soup.select('table.type_list tr div.title strong')
titles = soup.select('div.title strong')
# for title in titles:
#     print(title.string)
#
# print('총 :', len(titles),'권')


''' 
    웹 페이지에서 도서 이미지를 다운받아 imgs 폴더 안에 책이름.jpg 저장
'''
imgs = soup.select('td.image a > img')
for img_link in imgs:
    title = r'imgs/'+img_link.attrs['alt']+'.jpg'
    img = urlopen(img_link.attrs['src']).read()
    with open(title, 'wb') as file:
        file.write(img)

# for img_link in imgs:
#     # print(img_link)
#     # print(img_link.attrs['src'])
#     img = urlopen(img_link.attrs['src']).read()
#     with open('imgs/' + img_link.attrs['src'], 'wb') as file:
#         file.write(img)

# 형민이꺼
# url = soup.select('div.cover >a > img')
# for i in url:
#     isrc = i.attrs['src']
#     title = i.attrs["alt"].strip().replace('/', '_')
#     print(isrc)
#     imgName = 'imgs/{}.png'.format(title)
#     urlretrieve(isrc, imgName)

# 장우형꺼
imgs = soup.select('.cover img')
for img in imgs:
    photo=urlopen(img.attrs['src']).read()
    title = img.attrs['alt'].strip().replace('/','_')
    with open('imgs/{}.jpg'.format(title),'wb') as f:
        f.write(photo)