# http://www.pythonscraping.com/pages/warandpeace.html
# 1. 녹색 글자만 추출하여 출력

from urllib.request import *
from urllib.parse import *
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

green = soup.select('span.green')

# for data in green:
#     data = data.text.split()
#     print(' '.join(data))

# http://www.pythonscraping.com/pages/page3.html
# 2.아이템과 가격($제외)을 추출

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

items = soup.select('tr.gift>td:nth-child(2n-1)')
for item in items:
    item = item.text.split()
    print(item)
    # print(' '.join(item).replace('$', ''))
    # print('item : {}, cost : {}'.format(item[0],item[1].replace('$','')))

# 장우형꺼
# url2='http://www.pythonscraping.com/pages/page3.html'
# html2=request.urlopen(url2)
# soup = BeautifulSoup(html2,'html.parser')
# items = soup.select('#giftList tr.gift td:nth-of-type(1)')
# costs = soup.select('#giftList tr.gift td:nth-of-type(3)')
# for item,cost in zip(items,costs):
#     title = item.text.strip()
#     price = cost.text.strip().replace('$','')
#     print('Title : {}, Cost : {}'.format(title,price))
    

# https://wikidocs.net/
#  1) 책 제목과 설명만 추출
#  2) 이미지 다운

html = urlopen('https://wikidocs.net/')
soup = BeautifulSoup(html, 'html.parser')

# books = soup.select('div.media-body')
# for book in books:
#     print(book)

titles = soup.select('a.book-subject')
# for title in titles:
#     print(title.text)
img = soup.select('img.book-imgae')


from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("https://wikidocs.net/")

soup = BeautifulSoup(html, 'html.parser');

x = soup.select('.book-subject');
y = soup.select('.book-detail');
z = soup.select('.book-image');
# for a, b, c in zip(x, y, z):
#     print(a.text);
#     temp = b.text.replace('\n','').replace(' ', '').replace('-', ' ');
#     print(temp);
#     with open('practice_imgs/{}.png'.format(a.text), "wb") as f:
#         url = 'https://wikidocs.net' + parse.quote(c.attrs['src'].replace('//', '/'), encoding='UTF-8');
#         f.write(urlopen(url).read());

str1 = 'hello world'
str2 = 'world'
a = str1.find(str2)
print(a)