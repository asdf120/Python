''' 다른 프로그램의 main() 역할
    Ex02_csv_insert.py에서 실행하면 __name__ 변수에 __main__ 값이 들어가고
    다른 파일에서 이 파일을 실행하면 파일명과 동일한 Ex02_csv_insert라는 값이 들어간다.
'''
from collections import deque

import cx_Oracle as oracle
import csv


def create_DBtable():
    # pass
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            sql = """
                create table supply (
                    id integer primary key,
                    supplier_name varchar(30),
                    invoice_number varchar(20),
                    part_number varchar(20),
                    cost integer,
                    purchase_date date
                )
            """
            cursor.execute(sql)
            sql2 = "create sequence seq_supply_id"
            cursor.execute(sql2)


def save_DBtable(data):
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO supply(id, supplier_name, invoice_number, part_number, cost, purchase_date)
                VALUES (seq_supply_id.nextval, :0, :1, :2, :3, :4)
            """
            cursor.execute(sql, data)
        conn.commit()  # 반드시 커밋해줄것


def save_DBtable2(data):
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO supply(id, supplier_name, invoice_number, part_number, cost, purchase_date)
                VALUES (seq_supply_id.nextval, :v_name, :v_invoice, :v_part, :v_cost, :v_date)
            """
            # 실행
            v_name = data[0]
            v_invoice = data[1]
            v_part = data[2]
            v_cost = data[3]
            v_date = data[4]
            cursor.execute(sql, (v_name, v_invoice, v_part, v_cost, v_date))
            # [주의] 변수가 1개여도 튜플로 만듦
            # cursor.execute(sql, (v_name,))
        conn.commit()  # 반드시 커밋해줄것


def view_DBtable(table):
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM " + table
            cursor.execute(sql)
            # for row in rows:
            #     print(row)
            return cursor.fetchall()

if __name__ == '__main__':
    # 1. DB 테이블 생성
    # create_DBtable()

    # 2. 데이터 입력
    # file_name = '../files/supply.csv'
    # file = open(file_name, 'r')
    # datas = csv.reader(file, delimiter=',')  # delimiter 파일에 들어있는 데이터를 구분지어줌
    # next(datas, None)  # 한줄(보통 맨 첫줄)을 읽어서 아무일도 하지않음
    # for row in datas:
    #     print(row)
    # save_DBtable(row)
    # save_DBtable2(row)

    datas = view_DBtable('supply')

    # for data in datas:
    #     print(data)

    print(*view_DBtable('supply'), sep='\n')

