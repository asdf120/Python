import datetime
from surprise import SVD
from surprise import Dataset
from surprise import accuracy

# DB예서 리뷰 데이터 가져오기

import numpy as np
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost',user='orange',password='1234',db='WTF',charset='utf8')
cursor =conn.cursor()

# 리뷰 데이터 가져오기 식당 리스트 가져오기
sql = 'SELECT member_id, res_id, rating_avg FROM Review_test'

cursor.execute(sql)
review_list = cursor.fetchall()

r = np.array(review_list)


df=pd.DataFrame(r)
df.columns=['mem_id','res_id','rating']

#평점이 없는 m_id와 res_id 추출
from numpy import nan
R_ori= df.pivot_table('rating', index='mem_id',columns='res_id')
zero_maxtrix=R_ori[R_ori==nan].reset_index().melt('mem_id', var_name='res_id')[['mem_id','res_id']]


#가져온 데이터를 학습
from surprise import Reader

reader=Reader(rating_scale=(0.01,5))
data = Dataset.load_from_df(df[['mem_id','res_id','rating']], reader=reader)
trainset=data.build_full_trainset()

algo=SVD(n_epochs=20,n_factors=50, random_state=0)
algo.fit(trainset)

#현재 시간을 저장
now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d_%H%M%S")
print(formattedDate)

#현재 시간명으로 temp table 생성
sql1 = """CREATE TABLE res_recommend_svd_{}(
            res_id INT,
            pred_rating Float,
            member_id INT)""".format(formattedDate)

cursor.execute(sql1)
conn.commit()


#데이터 입력
for a,b in zero_maxtrix.values:
    result = algo.predict(a,b)
    data=(result[0],result[1],result[3])
    print(data)
    sql2 = " INSERT INTO res_recommend_svd_{} (member_id,res_id,pred_rating) VALUES (%s,%s,%s)".format(formattedDate)

    cursor.execute(sql2, data)
    conn.commit()


# 기존 테이블명 변경
sql3 ='RENAME TABLE res_recommend_svd TO res_recommend_svd_backup_{}'.format(formattedDate)

cursor.execute(sql3)
conn.commit()


# temp table을 원래 테이블 명으로 변경
sql4 ='RENAME TABLE res_recommend_svd_{} TO res_recommend_svd'.format(formattedDate)

cursor.execute(sql4)
conn.commit()

# foreign key 추가
sql5 ='ALTER TABLE res_recommend_svd ADD CONSTRAINT FOREIGN KEY (res_id) REFERENCES restaurant(res_id)'

cursor.execute(sql5)
conn.commit()


# 닫기
cursor.close()
conn.close()

