# 0. 패키지(모듈) 임포트
import cx_Oracle as oci

# 1. 연결객체 얻어오기
conn = oci.connect('scott/tiger@localhost:1521/orcl')

# 2. 커서객체 얻어오기
# cursor = conn.cursor()

# 3. sql 문장
# sql = "SELECT * FROM emp"

# 4. sql 문장 실행
# cursor.execute(sql)
# datas = cursor.fetchall()
# print(datas)

# 5. 커서객체 닫기
# cursor.close()

# 6. 커넥션 닫기

with oci.connect('scott/tiger@localhost:1521/orcl') as conn:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        datas = cursor.fetchall()

for data in datas:
    print(data)

# for tuple in datas:
#     print(f'{tuple[0]:13} {tuple[1]:1} {tuple[2]:6}')