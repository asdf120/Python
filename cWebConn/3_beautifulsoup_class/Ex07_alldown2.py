"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request as req
import os, time, re  # re : 정규식


def download_file(url):
    p = parse.urlparse(url)
    print(p)
    # print(type(p))
    savepath = './' + p.netloc + p.path
    # print(savepath)

    if re.search('/$', savepath):  # /$ url의 마지막부분을 의미
        savepath += 'index.html'
        print(savepath)

    # 내 폴더에 파일이 존재하는지 확인
    if os.path.exists(savepath):
        return savepath

    # 다운받을 폴더를 생성
    savdir = os.path.dirname(savepath)
    if not os.path.exists(savdir):
        os.makedirs(savdir)

    # 다운받기
    try:
        print('download=',savepath)
        req.urlretrieve(url,savepath)
        time.sleep(2)
        return savepath
    except:
        print('fail download...',url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)
