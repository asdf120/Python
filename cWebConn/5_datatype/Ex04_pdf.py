"""
   패키지 필요 (Terminal에서) > pip install pdfminer3k
"""

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen


def readPDF(pdfFile):
    # pdf 리소스 관리자
    rsrcmgr = PDFResourceManager()
    # pdf 내부의 텍스트 입출력을 위한 객체
    retstr = StringIO() # 문자열을 파일처럼 처리
    # 파리미터 객체
    laparams = LAParams()
    # pdf 내용을 텍스트로 변환하기 위한 객체
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # pdf 내용을 텍스트로 변환하는 작업
    process_pdf(rsrcmgr, device, pdfFile)
    # 반환된 문자열
    content = retstr.getvalue() #pdf값
    retstr.close()
    return content


# pdf -> string
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
# print(outputString)
pdfFile.close()

# string -> file write
with open("result/pdf/result.txt", "w") as f:  # data / pdf 폴더 있어야 함
    f.write(outputString)
    # print('파일 저장됨')
