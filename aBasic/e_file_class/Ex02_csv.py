# 1. 리스트의 데이터를 csv로 저장
import csv

data = [[1, '김길동', '책임'], [2, '박길동', '연구원'], [3, '최길동', '선임']]

with open('./data/imsi.csv', 'w', newline='', encoding='utf-8-sig') as f:
    cout = csv.writer(f)  # f라고 명한 파일을 cout에 저장?할수있도록함(stream과 비슷한개념)
    cout.writerow(data)  # cout에 data를 저장

data = []
with open('./data/imsi.csv', 'r', encoding='utf-8-sig') as f:
    cin = csv.reader(f)
    data = [row for row in cin if row]
print(data)

with open('./data/imsi.csv', 'r', encoding='utf-8-sig') as f:
    cin = csv.reader(f)
    data = [row for row in cin]  # 컴프리핸션에 조건문이 필요없게 됨.
print(data)


