'''
    http://en.wikipedia.org/wiki/Comparison_of_text_editors
    화면의 테이블 먼저 확인
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, 'html.parser')

# class가 wikitable인 태그들 중에서 첫번째 태그 선택
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")
# print(rows)

# wt : 텍스트 쓰기 모드
# result/csv 폴더 있어야 함 ( 추후에 폴더 생성하는 코드 추가 )
# newline='' : 줄바꿈 없음
# encoding="utf-8" : 한글처리
csvFile = open("result/csv/data.csv", "wt", newline='', encoding="utf-8")
writer = csv.writer(csvFile)

#
try:
    for row in rows:
        # print(row)
        csvRow = []
        # td, th 태그의 내용을 리스트에 추가
        for cell in row.find_all(['td','th']):
            # print(cell)
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    print('저장됨')
    csvFile.close()
    # 생성된 csv 파일은 엑셀로 열어보기