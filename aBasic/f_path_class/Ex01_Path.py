"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
p = Path(r"C:\Windows")    # Path() -> 실존 경로가 있는지 확인은 안함
# print(p)
# print(p.resolve())
print('1------------------------------------------')

test = []
for x in p.iterdir():
    if x.is_dir():
        test.append(x)
# print(test)

# [복습] list comprehension
# print([x for x in p.iterdir() if x.is_dir()])

print('2------------------------------------------')
p = Path('.')
subs = list(p.glob('../a_datatype_class/*.txt'))
print(subs)

