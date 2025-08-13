# 51. 정수 2개 입력 받아 비교하기

# a, b = map(int, input().split())

# print(a != b)

# 52. 정수 입력 받아 참 거짓 평가하기

# n = int(input())

# print(bool(n))

# 53. 참 거짓 바꾸기 

# a = bool(int(input()))

# print(not a)

# 54. 둘 다 참일 경우만 참 출력하기

# a, b = map(int, input().split())

# print(bool(a) and bool(b))

# 55. 하나라도 참이면 참 출력하기

# a, b = map(int, input().split())

# print(bool(a) or bool(b))

# 56. 참/ 거짓이 서로 다를 때에만 참 출력하기

# a, b = map(int, input().split())
# c, d = bool(int(a)), bool(int(b))

# print(c and (not d) or (not c) and d)

# # 57. 참 / 거짓이 서로 같을 때에만 참 출력하기
# a, b = map(int, input().split())

# c, d = bool(int(a)), bool(int(b))

# print((not c) and (not d) or (c and d))

# 58. 둘 다 거짓일 경우만 참 출력하기

# a, b = map(int, input().split())

# c, d = bool(int(a)), bool(int(b))

# print(not(a or b))

# 59. 비트 단위로 NOT 하여 출력하기

# a = int(input())
# print(~a)

# 60. 비트 단위 AND 하여 출력하기

# a, b = map(int, input().split())

# print(a&b)

# 61. 비트 단위 OR 하여 출력하기

# a, b = map(int, input().split())

# print(a|b)

# 62. 비트 단위 XOR 하여 출력하기

# a, b = map(int, input().split())

# print(a ^ b)

# 63. 정수 2개 입력 받아 큰 값 출력하기

# a, b = map(int, input().split())

# c = (a if (a>=b) else b)

# print(c)

# 64. 정수 3개 입력 받아 가장 작은 값 출력하기

# a, b, c = map(int, input().split())

# d = (a if a < b else b ) if ((a if a < b else b) < c) else c

# print(d)

# 65. 정수 3개 입력 받아 짝수만 출력하기

# a, b, c = map(int, input().split())

# if a % 2 == 0:
#     print(a)
    
# if b % 2 == 0:
#     print(b)

# if c % 2 == 0:
#     print(c)

# 66. 정수 3개 입력 받아 짝/홀 출력하기

# a, b, c = map(int, input().split())

# if a % 2 == 0:
#     print('even')

# else:
#     print('odd')

# if b % 2 == 0:
#     print('even')

# else:
#     print('odd')

# if c % 2 == 0:
#     print('even')

# else:
#     print('odd')

# 67. 정수 1개 입력 받아 분류하기

# a = int(input())

# if a < 0:
#     if a % 2 == 0:
#         print('A')
        
# if a < 0:
#     if a % 2 != 0:
#         print('B')
        
# if a > 0:
#     if a % 2 == 0:
#         print('C')
        
# if a > 0:
#     if a % 2 != 0:
#         print('D')
        
# 68. 점수 입력 받아 평가 출력하기

# a = int(input())

# if a >= 90:
#     print('A')

# elif a >= 70:
#     print('B')
    
# elif a >= 40:
#     print('C')
    
# else:
#     print('D')

# 69. 평가 입력 받아 다르게 출력하기

# word = (input())

# if word == 'A':
#     print('best!!!')

# elif word == 'B':
#     print('good!!')

# elif word == 'C':
#     print('run!')

# elif word == 'D':
#     print('slowly~')

# else:
#     print('what?')
    
# 70. 월 입력 받아 계절 출력하기

# a = int(input())

# if a // 3 == 1:
#     print('spring')
    
# elif a // 3 == 2:
#     print('summer')
    
# elif a // 3 == 3:
#     print('fall')
    
# else:
#     print('winter')


