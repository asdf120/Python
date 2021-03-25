import tkinter as tk
import cx_Oracle as oracle

total_price = 0
total_quantity = {'떡볶이': 0, '순대': 0, '튀김': 0}


# 메뉴선택 버튼
def menu_click(menu, price):
    global total_price
    total_price += price  # 해당 메뉴 가격만큼 총 금액 증가
    total_quantity[menu] += 1  # 해당 메뉴에 대한 수량 증가
    menu_entry.delete(0, "end")  # 텍스트를 지움
    menu_entry.insert(0, total_price)  # 총 금액 나타내기
    menu_quantity.delete(0, "end")
    menu_quantity.insert(0, total_quantity)  # 총 수량 나타내기


# 주문하기 버튼
def order_click():
    global total_price
    global total_quantity
    menu_entry.delete(0, "end")
    menu_quantity.delete(0, "end")
    # 오라클 연결
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            pass
            sql = """INSERT INTO menu_order( order_number, ddeok, soondae, fried, total_price )
                    VALUES (seq_order_number.nextval, :v_ddeok, :v_soondae, :v_fried, :v_total_price)
                  """
            v_ddeok = total_quantity.get('떡볶이')
            v_soondae = total_quantity.get('순대')
            v_fried = total_quantity.get('튀김')
            cursor.execute(sql, (v_ddeok, v_soondae, v_fried, total_price))  # 해당 sql 실행
        conn.commit()

    # 가격, 수량 초기화
    total_price = 0
    total_quantity = {'떡볶이': 0, '순대': 0, '튀김': 0}

# 전체 주문내역
def order_info():
    with oracle.connect('scott/tiger@localhost:1521/orcl') as conn:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM menu_order"
            cursor.execute(sql)
            order_data = cursor.fetchall()

    with open('./order_info/order_info.txt', 'w', encoding='utf-8') as file:
        file.write('주문번호 떡볶이 순대 튀김 가격' + "\n")
        for (order_num, ddeok, soondae, fried, price) in order_data:
            file.write("   "+ order_num + "     ")
            file.write(str(ddeok) + "    ")
            file.write(str(soondae) + "   ")
            file.write(str(fried) + "   ")
            file.write(str(price) + "\n")


menu_board = tk.Tk()

menu_board.title("메뉴판")
menu_board.geometry("300x300+100+100")  # 메뉴판 사이즈 & 화면이 생성되는 위치

menu_quantity = tk.Entry(menu_board, width=30)
menu_quantity.grid(row=0, columnspan=1)

menu_entry = tk.Entry(menu_board, width=30)
menu_entry.grid(row=1, columnspan=1)

ddeok = tk.Button(menu_board, text='떡볶이 3000원', width=15, overrelief='groove', pady=10,
                  command=lambda: menu_click('떡볶이', 3000))
soondae = tk.Button(menu_board, text='순대 3500원', width=15, overrelief='groove', pady=10,
                    command=lambda: menu_click('순대', 3500))
fried = tk.Button(menu_board, text='모듬튀김 2500원', width=15, overrelief='groove', pady=10,
                  command=lambda: menu_click('튀김', 2500))
order = tk.Button(menu_board, text='주문하기', width=15, overrelief='groove', pady=10,
                  command=lambda: order_click())
info = tk.Button(menu_board, text='주문내역보기', width=15, overrelief='groove', pady=10,
                 command=lambda: order_info())

ddeok.grid(row=2, column=0)
soondae.grid(row=3, column=0)
fried.grid(row=4, column=0)
order.grid(row=5, column=0)
info.grid(row=6, column=0)

menu_board.mainloop()  # 메뉴판 띄우기

