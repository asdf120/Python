# 1. 사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.
# 또 숫자 중에서 평균을 출력하여 보자.
# num = []
# num.append(int(input('정수를 입력 : ')))
# num.append(int(input('정수를 입력 : ')))
# num.append(int(input('정수를 입력 : ')))
# num.append(int(input('정수를 입력 : ')))
# num.append(int(input('정수를 입력 : ')))
# sum = 0
# for i in num:
#     sum += i
# print('평균 = ' ,sum / len(num))

# 2. 사용자에게서 받은 문자들을 역순으로 출력한다.
word = input('문자열입력 : ')
print(word[::-1])

# 4. 전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가 입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자.
phone = [[], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
         ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
         ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
string = input('문자열을입력하시오: ')
result = ''
for char in string:
    for i in range(len(phone)):
        if char.upper() in phone[i]:
            result += str(i + 1)
print(result)