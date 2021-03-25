# 1
# try:
#     for i in range(1, 7):
#         result = 7 // i
#         print(result)
# except ZeroDivisionError:
#     print("Not divided by 0")
# finally:
#     print("종료")

# 2.
# sentence = list("Hello Gachon")
# while (len(sentence) + 1):
#     try:
#         print(sentence.pop(0))
#     except Exception as e:
#         print(e)
#         break

# 3. 4
alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
# for a, b in enumerate(zip(alist, blist)):
#     print(b[a]) # a 2 error
for result in enumerate(zip(alist,blist)):
    print(result)

# alist = ["a", "1", "c"]
# blist = ["b", "2", "d"]
# for a, b in enumerate(zip(alist, blist)):
#     print(a/int(b[0]))

# 4. 4번

# 5. 4번

# 6.
# for i in range(3):
#     try:
#         print(i,3//i)
#     except ZeroDivisionError:
#         print('Not divided by 0')

# 7.
# with open('i_have_a_dream.txt',"r") as f:
#     contents = f.read()
#     print(contents)

# 8. 3번
