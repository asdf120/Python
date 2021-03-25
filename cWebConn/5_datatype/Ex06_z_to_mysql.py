'''
    [ mysql  테이블 만들기 ]

    create database pythondb;
    show databases;
    use pythondb;

    create table wikidata(
        id int primary key auto_increment,
        title varchar(200),
        content text,
        created timestamp default current_timestamp
    )

    show tables;
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import random
import MySQLdb

# mysql 서버 접속
conn = MySQLdb.connect(host='localhost', port=3306, \
                       db='pythondb', user='scott', passwd='tiger')
cursor = conn.cursor()


# 테이블에 저장
def store(title, content):
    # 제목과 내용에 ' or " 있으면 INSERT 에러 발생
    title = title.replace("'","''") # ' -> ''
    title = title.replace('"','\"') # " -> \"
    content = content.replace("'","''") # ' -> ''
    content = content.replace('"','\"') # " -> \"
    sql = "INSERT INTO wikidata(title,content) values('%s','%s')"\
            %(title,content)
    cursor.execute(sql)
    conn.commit()
    '''
        INSERT INTO wikidata(title,content) values('abc','xyz')  - OK
        INSERT INTO wikidata(title,content) values('abc','x'yz') - Error
        INSERT INTO wikidata(title,content) values('abc','x''yz')  - OK
        "(큰따옴표)는 sql="" 안에 """ 형식이 되기에 에러 발생
    '''


# 위키피디아의 url 수집
# http://en.wikipedia.org/wiki/Yi_Sun-sin 브라우저 > 소스보기 > 검색 '/wiki/'하면 많은 링크가 나온다
def getLinks(url):
    html = urlopen('http://en.wikipedia.org'+url)
    obj = bs(html, 'html.parser')
    # h1 태그의 내용
    title = obj.find('h1').get_text()
    # id가 mw-content-text인 div 태그 내부의 p 태그의 텍스트
    content = obj.find('div', { 'id':'mw-content-text'}).find('p').get_text()
    # print(title)
    # print(content) # 내용이 없을 수도 있다 -> 다른 정보를 추출하기

    # 테이블에 저장
    store(title, content)
    # 링크를 리턴함 ( 정규표현식 : ^시작, $끝,  * 0회 이상 반복 )
    return obj.find('div',{ 'id':'bodyContent'}).findAll('a',
                                    href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Christopher_Columbus');
# links = getLinks('/wiki/Yi_Sun-sin'); # 도중에 한글을 가져와서 에러 발생하는데 해결하려면?
# print(links)
try:
    count = 0
    while len(links) > 0:
        # url 리스트 중에서 랜덤으로 url 선택
        newArticle = links[ random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        # 해당 문서에 포함된 새로운 링크를 가져옴
        links = getLinks(newArticle)
        count += 1
        if count >= 5:  # 5건만 처리
            break

finally:
    cursor.close()
    conn.close()
    print('완료')

