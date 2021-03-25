"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""


# (1) 인자도 리턴값도 없는 함수
def nothing():
    print('함수안 실행')
    return '리턴값'


nothing()
print(nothing())  # 리턴값이 없으면 none


# (2) TODO 리턴값이 여러개인 경우 *GOOD*
def func(arg1, arg2):
    return arg1 + arg2, arg1 * arg2


result = print(func(2, 3))  # print()에 리턴값이 없기때문에 함수값 다음라인에 none 출력
print(result)

result = func(2, 3)
print(result)

hap, gob = func(2, 3)
print('합', hap)
print('곱', gob)
print()


# (3) 위치인자 (positional argument)
def func(greeting, name):
    print(greeting, '!!!', name, '님')


func('안녕', '기묭관')
func('John', 'Hello')

# (4) 키워드인자 (keyword argument)
func(name='올라프', greeting='울라')


# (5) 매개변수(인자)의 기본값 지정
def func(greeting='Hello', name='아무개'):
    print(greeting, '!!!!', name, '님')


func('안녕')
func('안녕', '김용관')
func(name='이름')
print()


# [참고] 나중에 읽기
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
    return result


buggy('가')
buggy('나')
buggy('하', [1, 2, 3])
buggy('다')
result = buggy('라')
print(result)
print()
'''
#----------------------------------------------------------------
#(5) 위치 인자 모으기 (*) 중요

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?
'''


# TODO *args 엄청 중요
def func(a, b, c=0, *args):
    sum = a + b + c
    print(args)
    for i in args:
        sum += i
    return sum


print('===================== positional argument ======================')
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))  # args에 7,8,9가 튜플로 들어간다


# ******************************************************************
# (6) 키워드 인자 모으기 : **kwargs

def func(a, b, c=0, **kwargs):
    sum = a + b + c
    print(kwargs)
    for k in kwargs:
        sum += kwargs.get(k)
    return sum


print('============== keyword argument 모음 =======================')
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, kor=7))
print(func(4, 5, 6, math=7, kor=8, java=9))
