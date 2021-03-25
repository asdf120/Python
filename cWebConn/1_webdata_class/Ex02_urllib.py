from urllib import request, error

# urllib.request 에는 s가 안붙음

# 0. 페이지 접근
try:
    site = request.urlopen('http://www.google.com')
except Exception as err:
    print('잘못된 url :', err)
else:
    # 1. 웹 문서 읽기
    print(site)  # 200
    page = site.read()
    # print(page)
    # print('-' * 100)
    # # 2. 웹 페이지 상태값 얻어오기
    # print(site.status)
    # print('-' * 100)
    #
    # # 3. 헤더정보 얻기
    headers = site.getheaders()
    # print(headers)
    # # 헤더의 키 >>>> 헤더의 값
    # for key, value in headers:
    #     print(key, ">>>>", value)
print('프로그램 정상 종료')
