# 71. 0 입력 될 때가지 무한 출력하기

# a = 1

# while a != 0:
#     a = int(input())
#     if a != 0:
#         print(a)
#     if a == 0:
#         break

# 72. 정수 1개 입력 받아 카운트 다운 출력하기

a = 3

while a != 0:
    a = int(input())
    if a != 0:
        if a != 0:
            a -= 1
            print(a)
    
    if a == 0:
        break
    