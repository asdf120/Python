'''
    # compile
     - 동일한 정규표현식을 매번 다시 쓰기 번거로움을 해결
     - compile로 해당표현식을 re.RegexObject 객체로 저장하여 사용가능
'''

import re

pattern = re.compile(r'[\w]+@[\w.]+')
result = pattern.search('test@gmail.com hahaha good')
if result:
    print(result.group())

# ----------------------------------------
webs = ['http://www.test.co.kr',
        'https://www.test1.com',
        'http://www.test.com',
        'ftp://www.test.com',
        'http:://www.test.com',
        'htp://www.test.com',
        'http://www.google.com',
        'https://www.homepage.com.']

# pattern = re.compile(r'https?://[\w.]+\w$')
pattern = re.compile(r'https?://[\w.]+\w+$')

result = list(map(lambda w: pattern.search(w), webs))  # w라는 인자가 들어왔을때 pattern.search(w)를 리턴해줌
print(result)

for url in result:
    if url:
        print(url.group())
