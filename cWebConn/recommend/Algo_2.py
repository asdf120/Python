import datetime

import numpy as np
import pymysql
import pandas as pd
from sklearn.metrics import mean_squared_error

conn = pymysql.connect(host='localhost',user='orange',password='1234',db='WTF',charset='utf8')
cursor =conn.cursor()

# 리뷰 데이터 가져오기 식당 리스트 가져오기
sql = 'SELECT member_id, res_id, rating_avg FROM Review_test'

cursor.execute(sql)
review_list = cursor.fetchall()

#DB에서 가져온 값을 넘파이 array 전환
r = np.array(review_list)

# 넘파이 array를 df 로 전환 하며 컬럼명 입력
df=pd.DataFrame(r)
df.columns=['mem_id','res_id','rating']


# df를 피벗 테이블을 통해 형태 전환
R_ori= df.pivot_table('rating', index='mem_id',columns='res_id')

# 빈곳을 0으로 채움
rating_matrix=R_ori.fillna(0)
rating_matrix

# 행열 분해를 위해 가져온 데이터의 행열의 크기 측정
R=np.array(R_ori)
num_users,num_items=R.shape
k=3

# 임의 값을 가지는 분해 행열 생성
np.random.seed(1)
P=np.random.normal(scale=1./k, size=(num_users,k))
Q=np.random.normal(scale=1./k, size=(num_items,k))


# 오차(rmse)를 계산하는 함수
from sklearn.metrics import mean_squared_error

def get_rmse(R, P, Q, non_zeros):
    error = 0
    full_pred_matrix = np.dot(P, Q.T)

    x_non_zero_ind = [non_zero[0] for non_zero in non_zeros]
    y_non_zero_ind = [non_zero[1] for non_zero in non_zeros]
    R_non_zeros = R[x_non_zero_ind, y_non_zero_ind]
    print(R_non_zeros)
    full_pred_matrix_non_zeros = full_pred_matrix[x_non_zero_ind, y_non_zero_ind]
    print(full_pred_matrix_non_zeros)
    mse = mean_squared_error(R_non_zeros, full_pred_matrix_non_zeros)
    print(mse)
    rmse = np.sqrt(mse)

    return rmse

# 테이블 R 에서 0이 아닌 값(리뷰가 있는 값)을 위치와 값 추출
non_zeros=[(i,j,R[i,j]) for i in range(num_users) for j in range(num_items) if R[i,j]>0]

# 분해 행열과 오리지날의 오차를 계산
print("초기 오차", get_rmse(R,P,Q,non_zeros))

# 분해 행열을 곱해 예측 행열 구함
pred_matrix =np.dot(P,Q.T)

# 예측 행열과 오리지널 데이터를 비교하여  P와 Q를 지속 수정 한다 SGD 업데이트 공식
steps =1000
learning_rate=0.01
r_lambda=0.01

for step in range(steps):
    for i,j,r in non_zeros:
        eij = r- np.dot(P[i,:],Q[j,:].T)
        P[i,:] = P[i,:]+learning_rate*(eij*Q[j,:]-r_lambda*P[i,:])
        Q[j,:] = Q[j,:]+learning_rate*(eij*P[i,:]-r_lambda*Q[j,:])
    rmse=get_rmse(R,P,Q,non_zeros)
    if (step%50)==0:
        print("step",step,"rmse",rmse)

# 수정된 P와 Q를 곱해 예측 행열을 구한다.
pred_matrix= np.dot(P,Q.T)

#!!식당간 코사인 유사도를 기반으로 연관성 구하기!!

#예측 행열에 컬럼명을 부여하며 DF 으로 전환
test_df = pd.DataFrame(pred_matrix, columns=R_ori.columns)

#오리지널에 빈곳에 0을 채운 행열의 행과 열의 위치를 바꾼다
rating_matrix_T = rating_matrix.transpose()

# 코사인 유사도를 구한다
from sklearn.metrics.pairwise import cosine_similarity

item_sim = cosine_similarity(rating_matrix_T,rating_matrix_T)


#유사도 행열을 컬럼명을 부여하며 DF로 전환
item_sim_df=pd.DataFrame(data=item_sim, index=rating_matrix.columns, columns=rating_matrix.columns)


# 평점 예측 함수
def predict_rating(ratings_arr,items_sim_arr):
    ratings_pred = ratings_arr.dot(items_sim_arr)/np.array([np.abs(items_sim_arr).sum(axis=1)])
    return ratings_pred

# 행열 분해로 구한 예측 행열과 코사인 유사도를 곱한뒤 유사도의 절대값 합으로 나누어 예측값을 구한다
rating_pred = predict_rating(test_df.values,item_sim_df.values)

# df로 전환
rating_pred_df = pd.DataFrame(rating_pred, columns=R_ori.columns, index=R_ori.index)


#df 데이터베이스에 입력하기 위한 형태로 전환
result=rating_pred_df.reset_index().melt('mem_id', var_name='res_id')


# db연결
temps=np.array(result)
conn = pymysql.connect(host='localhost', user='orange', password='1234', db='WTF', charset='utf8')
cursor = conn.cursor()



#현재 시간을 저장
now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d_%H%M%S")
print(formattedDate)


#현재 시간명으로 temp table 생성
sql1 = """CREATE TABLE res_recommend_cosine_similarity_{}(
            res_id INT,
            pred_rating Float,
            member_id INT)""".format(formattedDate)

cursor.execute(sql1)
conn.commit()



#신규 데이터를 입력
for temp in temps:
    list = tuple(temp)
    print(list)

    sql2 = " INSERT INTO res_recommend_cosine_similarity_{} (member_id,res_id,pred_rating) VALUES (%s,%s,%s)".format(formattedDate)

    cursor.execute(sql2, list)
    conn.commit()


# 기존 테이블명 변경
sql3 ='RENAME TABLE res_recommend_cosine_similarity TO res_recommend_cosine_similarity_backup_{}'.format(formattedDate)

cursor.execute(sql3)
conn.commit()


# temp table을 원래 테이블 명으로 변경
sql4 ='RENAME TABLE res_recommend_cosine_similarity_{} TO res_recommend_cosine_similarity'.format(formattedDate)

cursor.execute(sql4)
conn.commit()

# foreign key 추가
sql5 ='ALTER TABLE res_recommend_cosine_similarity ADD CONSTRAINT FOREIGN KEY (res_id) REFERENCES restaurant(res_id)'

cursor.execute(sql5)
conn.commit()


cursor.close()
conn.close()