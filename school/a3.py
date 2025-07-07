# 여러 개의 정수 다양한 옵션(키워드 인자)를 입력 받기

# 조건에 따른 함수 계산 / 하는 함수 작성하기
def add_numbers(*args, **kwargs):
    
    option = ['abs' , 'only_even', 'unique']
# 옵션은 선택 사항 -> 조건문
# 옵션 외 포함 -> None 반환 return 그리고 아무것도 계산하지 않음 return None
# 잘못된 옵션이 포함 될 시 None를 반환하기
    for key in kwargs:
        if key not in option:
            return None


# 함수 요구사항-> 
# *-> packing

# 정수 목록은 *agrs로 전달 
# 다음 키워드 옵션 -> **kwargs 전달

#  생략시 -> 기본 값은 False
  
# 정수 목록은 *agrs로 전달 
    numbers = list(args)

# if abs == True -> 모든 숫자 절대값
    if 'abs' in kwargs and kwargs['abs'] == True:
        for idx, val in enumerate(numbers):
            if val < 0:
                numbers[idx] = -val
                
# if only_even == True -> 짝수만 합산
    if 'only_even' in kwargs and kwargs['abs'] == True:
        numbers = [v for v in numbers if v % 2 == 0]
    
# if unique == True -> 중복 제거 후 합산 [ list 건들기?] pop?/ set()!
    if 'unique' in kwargs and kwargs['unique'] == True:
        temp = []
        for val in numbers:
            if val not in temp:
                temp.append(val)
        numbers = temp
        

# 최종합계는 print()로 출력
    total = 0
    for val in numbers:
        total += val
    print(f"합계는 {total}입니다")
# ==============================================================

add_numbers(1, -2, 2, -3)
# 출력 합계는 -2 임

add_numbers(1, -2, 2, -3, abs=True, only_even= True)
#출력: 합계는 4임 # |-2| = 2, |2| 2-> 2+2

add_numbers(1, 2, 2, 3, 3, 4, unique = True)
# 출력: 합계는 15임 # 중복 제거: 1+2+3+4+5

add_numbers(1, 2, 3, round=True)
#출력: None임 # round라는거 안 넣어놨음

# add_numbers(1, -2, 2, -3)
# # 출력 합계는 -2 임

# add_numbers(1, -2, 2, -3, abs=True, only_even=true)
# #출력: 합계는 4임 # |-2| = 2, |2| 2-> 2+2

# add_numbers(1, 2, 2, 3, 3, 4, unique = True)
# # 출력: 합계는 15임 # 중복 제거: 1+2+3+4+5

# add_numbers(1, 2, 3, round=True)
# #출력: None임 # round라는거 안 넣어놨음





 