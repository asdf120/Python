# sample.json 파일을 읽어서 총합 출력하기

import json

with open('./data/sample.json', 'r', encoding='utf-8') as sample:
    data = sample.read()

fruit = json.loads(data)
print(fruit)

# amount_price = 0
# for key in fruit:
#     price = fruit[key].get('price') * fruit[key].get('count')
#     print(key+"의 값은 :", price)
#     amount_price += price
# print('총 가격 : ',amount_price)

for key, value in fruit.items():
    for k_value, v_value in value.items():
        temp = v_value
        print(v_value)

    print(temp)