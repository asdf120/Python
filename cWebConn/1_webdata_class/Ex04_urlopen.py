# urlretrieve(): 파일로 바로 저장
# urlopen(): 파일로 바로 저장하기 않고 메모리에 로딩을 한다.

""" [참고] 파일저장 기본방식
    f = open('a.txt','w')
    f.write("테스트 내용")
    f.close()

    위의 과정을 with 문으로 간략하게 close 필요없음
    with open("a.txt","w") as f:
        f.write("테스트 내용")
"""

# urllib.request.urlopen() 이용하여 다음이미지를 test.png 저장
from urllib import request as req

imgName = 'data/test.png'

img = req.urlopen('https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png').read()
# print(img)
with open(imgName, 'wb') as file:
    file.write(img)
