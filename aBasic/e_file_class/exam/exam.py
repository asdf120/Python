# 1.

sum = 0
count = 0
with open('./data/sample.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        count += 1
        sum += int(line)

with open('./data/result.txt', 'w', encoding='utf-8') as result:
    result.write('총 점수는 : {}'.format(sum) + "\n")
    result.write('평균 : {}'.format(round(sum / count, 2)))

# 2,3
with open('./data/dream.txt', 'r', encoding='utf-8') as file:
    letter_count = 0
    line_count = 0
    word_count = 0
    while True:
        line = file.readline()
        if not line:
            break
        for sentence in line.replace(" ", "").strip():
            letter_count += 1
        for sentence in line.split():
            word_count += 1
        # 2번
        print('{}--{}'.format(line_count, line), end='')
        line_count += 1

print()
print()
# 3번
print('총 글자의 수 : {}'.format(letter_count))
print('총 단어의 수 : {}'.format(word_count))
print('총 줄의 수 : {}'.format(line_count))

# 4번
from pathlib import Path
import time
from random import randint

logtemp = Path('../logtemp')
logtemp.mkdir(exist_ok=True, parents=True)

with open('../logtemp/temp_log.txt', 'a', encoding='utf-8') as file:
    n = 10
    for num in range(n):
        print(time.strftime('%y-%m-%d %H:%M:%S ') + ''.join(["{}".format(randint(0, 9)) for num in range(0, n)]))
        file.write(time.strftime('%y-%m-%d %H:%M:%S ') + ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])+'\n')
# https://copycodes.tistory.com/547
