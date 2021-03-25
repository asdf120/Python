import xml.etree.ElementTree as et

# [참고] 위치인자와 키워드인자 구별


tree = et.ElementTree(file='./data/temp.xml')
root = tree.getroot()
print('root :', root)

print('root tag :', root.tag)

for child in root:
    # print(child.tag)
    for data in child:
        print(data.tag, ':', data.text)

    print("-" * 25)
