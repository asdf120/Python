"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""
from urllib.parse import urljoin

baseUrl = 'http://www.example.com/html/a.html'

print(urljoin(baseUrl, 'b.html'))
print(urljoin(baseUrl, 'sub/c.html'))
print(urljoin(baseUrl, '/sub/c.html'))
print(urljoin(baseUrl, '../sub/c.html'))
print(urljoin(baseUrl, '../temp/d.html'))

print(urljoin(baseUrl, 'http://www.daum.net'))
