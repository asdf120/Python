"""
    [예] 공공데이타 https://www.data.go.kr
        데이타셋 > 파일데이타 > 표준데이타 에서 JSON 데이타 찾기

        데이타 작은 거 선택하여 다운로드 : 전국고등학교학교군표준데이터.json
        추후에 selenium 이용하여 자동으로 내려받게 하려면?
"""

import urllib.request as req
import os.path, random
import json

savename = "data/전국고등학교학교군표준데이터.json"

# JSON 파일 분석하기 
# 기존 json 파일이 UTF-8이 아니기에 encoding="utf-8"를 추가하면 에러발생
json_file = open(savename,"r")
items = json.load(json_file)
# items = json.load(open(savename, "r"))
# print(items)
# 또는
# s = open(savename, "r", encoding="utf-8").read()
# items = json.loads(s)

# 출력하기 --- (※3)
for item in items['records']:
    # print(item)
     print(item['학구명']+' : ' + item['교육지원청명'])
