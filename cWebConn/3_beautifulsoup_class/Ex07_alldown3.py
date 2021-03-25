"""
    파이썬은 파일하나를 모듈로 취급한다면 다른 파일의 함수를 복사하지 않고 바로 호출한다.

    [주의] import Ex07_alldown1 코드부터 에러발생하지만 실행은 됨

"""


from bs4 import BeautifulSoup
from urllib.parse import *
from urllib.request import *
import os, time, re

# 에러 발생해도 실행은됨
import Ex07_alldown1
import Ex07_alldown2


# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {} # set or dictionary

# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    # ------------------------------------------------------
    # 해당 링크 다운로드
    savepath = Ex07_alldown2.download_file(url)
    if savepath is None:
        return

    # 이미 처리한 파일인지 확인
    if savepath in proc_files:
        return
    proc_files[savepath] = True
    '''
        {
            키 : savepath 밸류 : True
        }
    '''

    # 링크 추출
    with open(savepath,'r', encoding='utf-8') as file:
        html = file.read()
    links = Ex07_alldown1.enum_links(html,url)
    # print(links)
    for link_url in links:
        # print(link_url)
        # 링크의 루트경로 외의 경로를 무시
        if link_url.find(root_url) != 0:
            continue
        # 경로가 html로 끝나면
        if re.search('.html',link_url):
            analyze_html(link_url,root_url)
            continue

        # 다운로드
        Ex07_alldown2.download_file(link_url)

if __name__ == "__main__":
    # URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)



