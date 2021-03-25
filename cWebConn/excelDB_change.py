import csv
import re

import pymysql

# conn = pymysql.connect(host="localhost", user='orange', password='1234', db='WTF', charset='utf8')
conn = pymysql.connect(host="3.36.159.100", user='root', password='root', db='wtf', charset='utf8')

cursor = conn.cursor()

#
day = 'change'
#식당 정보 가져오기
with open('recommend/restaurant/restaurant_{}.csv'.format(day),'r',newline='',encoding='utf-8') as f :
    rows = csv.reader(f)
    next(rows, None)


    for row in rows:
        print(row)
        # 리뷰수가 null인 경우 0으로 전환
        if row[8]=='':
            print(row[8])
            row[8]=0

        # like_count , 제거
        row[9]=row[9].replace(',','')


        sql = """INSERT INTO restaurant (res_id,res_name,res_tell,res_addr,res_runtime,res_keyword,res_latitude,res_longitude,res_rating,like_count) 
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(sql, row)
        print("32line : ", row[1])
        conn.commit()

with open('recommend/menu/menu_{}.csv'.format(day),'r',newline='',encoding='utf-8') as f :
    rows = csv.reader(f)
    next(rows, None)

    for row in rows:
        print(row)

        # res_id가 튜플형태로 들어가 있어 처리
        row[0] = re.findall("\d+",row[0])

        sql = 'INSERT INTO menu (res_id,menu,price) VALUES (%s,%s,%s)'
        cursor.execute(sql, row)

        conn.commit()

with open('recommend/restaurant_pic/restaurant_pic_{}.csv'.format(day),'r',newline='',encoding='utf-8') as f :
    rows = csv.reader(f)
    next(rows, None)

    for row in rows:
        print(row)

        # res_id가 튜플로 들어가 있어 처리
        row[0] = re.findall("\d+",row[0])


        sql = 'INSERT INTO restaurant_pic(res_id, rtr_pic_loc) VALUES(%s,%s)'

        cursor.execute(sql, row)

        conn.commit()

cursor.close()
conn.close()