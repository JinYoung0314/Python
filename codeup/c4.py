# 27. 10진 정수 입력 받아 16진수로 출력하기

# a = input()

# s = int(a)
# #x=> 16진수 o-> 8진수
# print('%x'% s)



# # 28. 10진 정수 받아 16 진수로 출력하기

# a = input()

# s = int(a)
# #-> x,X -> 출력 16진수 값이 ff, FF임. 
# print('%X' %s) 



# # 29. 16진 정수 입력 받아 8잔수로 출력하기

# a = input()
# t= int(a, 16)
# print('%o'%t)



# # 30. 영문자 1개 입력 받아 10진수로 
# # s = ord(input()) => 입력 받은 문자를 10진수 유니코드 값으로 변환 후 저장하게 됨 
# s = ord(input())                          #유니코드란 세계 여러나의 문자를 
                                            #공통된 값으로 저장 될 때 
# print(s)



# # 31. 정수 입력 받아  유니코드 문자로 변환하기

# w = int(input())   
# print(chr(w))  # -> chr -> 정수를 유니코드화 하여 출력
                 # -> ord -> 유니코드?를 입력 받아 정수로 출력


                 
# # 32. 정수 1개 입력 받아 부호 바꾸기

# s = int(input())

# print(-s) # -로 음수로 부호를 변환



# #33. 문자 1개 입력 받아 다음 문자 출력하기

# s = ord(input()) #문자를 받아 유니코드, 아스키로 변환

# print(chr(s+1))  #그 수를 +1하여 유니로 변환



# # 34. 정수 2개를 입력 받아 차 계산하기

# w,w1 = (input().split(' '))

# w = int(w)
# w1 = int(w1)
# tw = w - w1

# print(tw)
# #  ------------------------
# w, w1 = map(int, input().split())
# print(w - w1)
 
 

# #35. 실수 2개 입력 받아 곱 계산하기

# s, s1 = map(float, input().split(' '))

# print(s * s1)



# #36. 단어 여러번 출력하기

# w, n = input().split(' ')
# print(w * int(n))



# #37. 문장 여러번 출력하기

# n = input()
# s = input()
# print(int(n)*s )



#38. 정수 2개 입력 받아 거듭제곱 계산하기

s, s1 = map(int, input().split(' '))

ts = s**s1

print(ts)
