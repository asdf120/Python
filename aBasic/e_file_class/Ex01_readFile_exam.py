""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""


def count_words(filename):
    # try:
    #     file = open('./data/' + filename, 'r', encoding='utf-8')
    # except Exception as e:
    #     pass
    # else:
    #     content = file.read()
    #     words = content.split()
    #     print(filename + "의 단어 갯수 :", len(words))
    #     file.close()

    try:
        with open('./data/' + filename, 'r', encoding='utf-8') as file:
            # content = file.read()
            # words = content.split()
            print(filename + "의 단어 갯수 :", len(file.read().split()))
    except Exception as e:
        pass


# 존재하지 않는 파일명도 있음
filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames:
    count_words(filename)
