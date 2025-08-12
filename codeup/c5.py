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

a, b = map(int, input().split())

c, d = bool(int(a)), bool(int(b))

print(not(a or b))

# 59. 비트 단위로 NOT 하여 출력하기

