# 1. BMI(Body Mass Index)는 체중(kg)을 신장(m)의 제곱(**2)으로 나눈 값으로 체지방 축적을 잘 반영하기 때문에 비만도 판정에
# 많이 사용한다. 사용자로부터 신장과 체중을 입력 받아서 BMI 값에 따라서 다음과 같은 메시지를 출력하는 프로그램을 작성하여 보자.
weight = float(input('무게(킬로그램) : '))
height = float(input('키(미터) : '))
BMI = round((weight / (height ** 2)), 2)

print('당신의 BMI : {}'.format(BMI))
if BMI >= 20 and BMI <= 24.9:
    print('정상')
elif BMI >= 25 and BMI <= 29.9:
    print('과체중')
elif BMI >= 30:
    print('비만')

# 2. 1부터 99까지 2자리의 정수로 이루어진 복권이 있다고 하자. 2자리가 전부 일치하면 1등상 100만원을 받는다.
# 2자리 중에서 하나만 일치하면 50만원을 받고 하나도 일치하지 않으면 상금은 없다
