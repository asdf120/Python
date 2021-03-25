from pathlib import Path
from _datetime import datetime

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home())

p1 = Path('Ex03_createPath.py')
print(p1.stat())

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
tm = p1.stat().st_ctime
# print(tm)

zt = datetime.fromtimestamp(tm)
print(zt)

# ------------------------------------------------
# 3. 디렉토리 생성
p1 = Path('temp/imsi/test')
p1.mkdir(exist_ok=True, parents=True)

# ------------------------------------------------
# 4. 파일 생성
# with open('./imsi/a.txt', 'w', encoding='utf-8') as f:
#     f.write('홍길동화이팅 ')

# f = Path('./imsi/b.txt')
# f.touch()

# ------------------------------------------------
#  5. 경로 제거
p = Path('temp/imsi/test')
# p.rmdir()  # 디렉토리 내부에 파일이 있으면 지워지지 않음

# 디렉토리 내부에 파일이 있어도 지워줌
import shutil

# shutil.rmtree('imsi')
shutil.copytree('../e_file_class', 'test')
