# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112  # 숫자형
b = ['1', '2', '3']  # 리스트
c = '987'  # 문자열
d = tuple(b)  # 튜플  d = ('1','2','3')
e = dict(k=5, j=6)  # 딕셔너리 e = { 'k' : 5, 'j' : 6 }

# for entry in e:  # a는 반복이 안되지만 b부터 e까지는 반복된다.
#     print(e[entry])
#
# for entry in e.items():
#     print(entry)    # dictionary는 하나의 튜플로 관리

# [연습] 1부터 10까지의 합 출력
sum = 0
for num in range(1, 11):
    sum = sum + num
print(sum)

# 홀수의 합
sum = 0
for num in range(1, 11, 2):  # 1~11까지 2씩 뛰어서 출력
    sum = sum + num
print(sum)
print()
# =========================================================
# while  ( 안해도 될듯 )

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break


"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for num in range(2, 10):
    for dan in range(1, 10):
        print(num, '*', dan, '=', num * dan, end=" ")
    print()


for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %2d " % (j, i, i * j), end="");
    print();
