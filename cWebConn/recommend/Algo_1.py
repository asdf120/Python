import datetime
import numpy as np
import pymysql
import pandas as pd
from sklearn.metrics import mean_squared_error

# rmse 측정 함수
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

# 행열 분해 함수
def matrix_facorization(R, K, steps=200, learning_rate=0.01, r_lambda=0.01):
    num_users, num_items = R.shape

    np.random.seed(1)
    P = np.random.normal(scale=1. / K, size=(num_users, K))  # size(x,y) x는 행의 갯수 y는 열의 갯수
    Q = np.random.normal(scale=1. / K, size=(num_items, K))

    prev_rmse = 10000
    break_count = 0

    # R >0 인 인덱스, 값을 저장

    non_zores = [(i, j, R[i, j]) for i in range(num_users) for j in range(num_items) if R[i, j] > 0]

    # SGD 기법으로 P와 Q 매트릭스 학습

    for step in range(steps):
        for i, j, r in non_zores:
            # 나눈 행열과 실제값 사이 오차 구함
            eij = r - np.dot(P[i, :], Q[j, :].T)
            # SGD 업데이트 공식
            P[i, :] = P[i, :] + learning_rate * (eij * Q[j, :] - r_lambda * P[i, :])
            Q[j, :] = Q[j, :] + learning_rate * (eij * P[i, :] - r_lambda * Q[j, :])

        rmse = get_rmse(R, P, Q, non_zores)
        if (step % 10) == 0:
            print("iteration step :", step, "rmse :", rmse)

    return P, Q


#member_id로 안먹어본 식당을 구하는 함수
def get_unate_food(ratings_matrinx, member_id):
    user_rating = ratings_matrinx.loc[member_id, :]

    already_ate = user_rating[user_rating > 0].index.tolist()

    res_list = ratings_matrinx.columns.tolist()

    unate_list = [res for res in res_list if res not in already_ate]

    return unate_list



# 안먹어본 식당과 행열분해로 식당 추천 함수
def recom_res_by_userid(pred_df, userId,unate_list, top_n=10):
    recomm_res = pred_df.loc[userId,unate_list].sort_values(ascending =False)[:top_n]
    return recomm_res


# 최종 함수
def recommend_restaurant01():
    # DB 연결
    conn = pymysql.connect(host='localhost', user='orange', password='1234', db='WTF', charset='utf8')
    cursor = conn.cursor()

    # 리뷰 데이터 가져오기 식당 리스트 가져오기
    sql = 'SELECT member_id, res_id, rating_avg FROM Review_test'

    cursor.execute(sql)
    review_list = cursor.fetchall()

    r = np.array(review_list)

    df = pd.DataFrame(r)
    df.columns = ['mem_id', 'res_id', 'rating']

    # 가져온 리뷰 테이블을 2차원 테이블로 재배치
    R_ori = df.pivot_table('rating', index='mem_id', columns='res_id')

    # 행열 분해 함수 SGD 공식을 통해 오차 최소화
    P, Q = matrix_facorization(R_ori.values, K=50, steps=200, learning_rate=0.01, r_lambda=0.01)

    # 분해한 행열을 다시 곱셈
    pred_matrix = np.dot(P, Q.T)
    ratings_pred_matrix = pd.DataFrame(data=pred_matrix, index=R_ori.index, columns=R_ori.columns)

    return ratings_pred_matrix

ratings_pred_matrix=recommend_restaurant01()

results=ratings_pred_matrix.reset_index().melt('mem_id', var_name='res_id')

temps=np.array(results)
temps



#DB 연결
conn = pymysql.connect(host='localhost', user='orange', password='1234', db='WTF', charset='utf8')
cursor = conn.cursor()


#현재 시간을 저장
now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d_%H%M%S")
print(formattedDate)


#현재 시간명으로 temp table 생성
sql1 = """CREATE TABLE res_recommend_matrix_decomposition_{}(
            res_id INT,
            pred_rating Float,
            member_id INT)""".format(formattedDate)

cursor.execute(sql1)
conn.commit()


for temp in temps:
    list = tuple(temp)
    print(list)

    #temp table 에 데이터 입력
    sql2 = "INSERT INTO res_recommend_matrix_decomposition_{} (member_id,res_id,pred_rating) VALUES (%s,%s,%s)".format(formattedDate)

    cursor.execute(sql2, list)
    conn.commit()


# 기존 테이블명 변경
sql3 ='RENAME TABLE res_recommend_matrix_decomposition TO res_recommend_matrix_decomposition_backup{}'.format(formattedDate)

cursor.execute(sql3)
conn.commit()


# temp table을 원래 테이블 명으로 변경
sql4 ='RENAME TABLE res_recommend_matrix_decomposition_{} TO res_recommend_matrix_decomposition'.format(formattedDate)

cursor.execute(sql4)
conn.commit()

# foreign key 추가
sql5 ='ALTER TABLE res_recommend_matrix_decomposition ADD CONSTRAINT FOREIGN KEY (res_id) REFERENCES restaurant(res_id)'

cursor.execute(sql5)
conn.commit()


cursor.close()
conn.close()