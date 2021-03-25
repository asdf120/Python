# from calculator import sum_func, minus_func, devide_func, multiply_func
from calculator import *

user_input = input("사직연산 프로그램 : ").split(" ")
first_val, second_val = int(user_input[0]), int(user_input[2])

fourcal = user_input[1]

if fourcal == "+":
    result = sum_func(first_val, second_val)
elif fourcal == "-":
    result = minus_func(first_val, second_val)
elif fourcal == "/":
    result = devide_func(first_val, second_val)
else:
    result = multiply_func(first_val, second_val)
print("실행 결과는", result)
