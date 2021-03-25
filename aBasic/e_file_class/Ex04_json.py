import json

with open('./data/temp.json', 'r', encoding='utf-8') as f:
    data = f.read()

print(type(data))  # str
print(data)

items = json.loads(data)
print(items)
print(type(items))

for key, value in items.items():
    print(key + " : ", value)
    # print(key + " : ",items[key])
    for k_result, v_result in value.items():
        print(k_result, v_result)

# for item in items:
#         print(item, items[item].get('No'))
#
# for item, values in items.items():
#     for i, v in values.items():
#         print(v)
