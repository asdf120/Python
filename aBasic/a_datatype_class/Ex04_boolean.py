# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

# 논리연산
hungry = True
sleepy = False
print(type(hungry))
print(hungry)
print(not(not hungry))
print(hungry and sleepy)
print(hungry & sleepy)
print(not n)
print()


"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False



"""

if('아'):
    print('True')
else:
    print('False')

if([]):
    print('True2')
else:
    print('False2')

if(0):
    print('True3')
else:
    print('False3')

if(-1):
    print('True4')
else:
    print('False4')
print()

a = 11
b = 9
print('a'+'b')

fact = "Python is funny"
print(str(fact.rfind('n')))

text = 'Gachon CS50 - programming with python'
text2 = " Human cs50 knowledge belongs to the world "
text.lower()
print(text[:5] + text[-1] + text[6] + text2.split()[0])

class_name = 'introduction programming with python'
for i in class_name:
    if i == 'python':
        i = i.upper()

print(class_name)

a = '10'
b = '5-2'.split('-')[1]
print(a * 3 + b)

a = "abcd e f g"
b = a.split()
c = (a[:3][0])
d = (b[:3][0][0])
print(c + d)

result = "CODE2018"
print("{0},{1}".format(result[-1], result[-2]))