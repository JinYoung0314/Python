
#
# 
# 
# 메뉴 정의
menu =""" 
    ====== 학생 성적 관리 프로그램 ======
    1. 학생 성적 입력
    2. 학생 성적 출력
    3. 학생 성적 확인
    4. 학생 성적 삭제
    5. 종료
    """
#전체 학생 정보
std_dict = {}

# 무한 while 실행 하여 계속 입력 받을 수 있는 상황
while True:
   
    print(menu) # 정의 한거 출력하기
    
    choice = int(input("메뉴 선택 (1~5): ")) # 사용자에게 원하는 메뉴 선택 받기
    
    if choice == 1: #메뉴 선택 1번  정보 입력
        userid = int(input("학번을 입력하세요: ")) # 학번을 출력 받고
        if userid in std_dict:          # 그 학번이 등록 된 경우 등록됨을 알리기
            print("이미 등록된 학번 입니다.") 
            continue # 이것이 실행이 
        # std_data['name'] =input("이름를 입력하세요: \t")
        # std_data['korean'] = int(input("국어 점수를 입력하세요: \t"))
        # std_data['english'] = int(input("영어 점수를 입력하세요: \t"))
        # std_data['math'] = int(input("수학 점수를 입력하세요: \t"))
        # std_data['total'] = std_data['korean'] + std_data['english'] + std_data['math']
        # std_data['avg'] = std_data['total'] /3
        name = input("이름 입력: ")
        kor = int(input("국어 성적 입력: "))
        eng = int(input("영어 성적 입력: "))
        math = int(input("수학 성적 입력: "))
        total = kor + eng + math
        avg = total / 3
        
        std_dict[userid] = {
            "이름": name,
            "국어": kor,
            "영어": eng, 
            "수학": math, 
            "합계": total, 
            "평균": avg,
        }
        print("성적이 저장 되었습니다.")
        
    elif choice == 2: # 전체 학생 성적 출력
        if not std_dict:
            print("등록된 학생 정보가 없습니다")
            continue
        
        print(f"[ 전체 학생 성적 ]")
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")

        for val, tem in std_dict.items():
            print(f"{val}\t{tem['이름']}\t{tem['국어']}\t{tem['영어']}\t{tem['수학']}\t{tem['합계']}\t{tem['평균']:.2f}")
    
    elif choice == 3:
        reserch = int(input("조회할 학번 입력: ")) # 조회할 학번 입력 받기

        if reserch in std_dict: # 조회 할 학번이 전체 학생 수에 해당 된다면 키 값 가지고 빼오기
            user = std_dict[reserch]
            print("\n[ 학생 정보 ]")
            print(f"학번: {userid}")
            print(f"이름: {userid['이름']}")
            print(f"국어: {userid['국어']}")
            print(f"영어: {userid['영어']}")
            print(f"수학: {userid['수학']}")
            print(f"합계: {userid['합계']}")
            print(f"평균: {userid['평균']:.2f}")
        
        else:
            print("해당 학번의 학생 정보가 없습니다")
            
    elif choice == 4: # 삭제 할  학번 골라서 삭제 혹은 정보 없음을 알리기
        sakjae = int(input("삭제 할 학번 입력: "))       
        if sakjae in std_dict:
            del std_dict[sakjae]
            print("학생 정보가 삭제 되었습니다")
            
        elif sakjae not in std_dict:
            print("해당 학번의 학생 정보가 없습니다.")
            
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("1~5사이의 숫자만 입력 하세요") 


# # 무한 while 실행 하여 계속 입력 받을 수 있는 상황
# def input_students(students):
#     student = {}  
#     userid = int(input("학번을 입력하세요: ")) # 학번을 출력 받고
#     if userid in students:          # 그 학번이 등록 된 경우 등록됨을 알리기
#         print("이미 등록된 학번 입니다.") 
#         return # 이것이 실행이 
#     student['id'] = userid
#     student['name'] =input("이름를 입력하세요: \t")
#     student['korean_score'] = int(input("국어 점수를 입력하세요: \t"))
#     student['english_score'] = int(input("영어 점수를 입력하세요: \t"))
#     student['math_score'] = int(input("수학 점수를 입력하세요: \t"))
#     student['total_score'] = student['korean_score'] + student['english_score'] + student['math_score']
#     student['avg_score'] = student['total_score'] /3
#     students[student['id']] = student #고유 식별 번호로 전체 학생 정보에 올리기ㅣ
#     print("성적이 저장 되었습니다.")

# def print_studentss(students):
#     if not students:
#             print("등록된 학생 정보가 없습니다")
            
#     else:
#         print(f"[ 전체 학생 성적 ]")
#         print(f"학번    이름    국어    영어    수학    합계    평균")

#         for val in students.values():
#             print(f"{val['id']:<8}{val['name']:<5}{val['korean_score']:>3}{val['english_score']:>7}{val['math_score']:>8}{val['total_score']:>9}{val['avg_score']:>9.2f}")
            
    

# def reserch_students(students):
#     reserch = int(input("조회할 학번 입력: ")) # 조회할 학번 입력 받기

#     if reserch in students: # 조회 할 학번이 전체 학생 수에 해당 된다면 키 값 가지고 빼오기
#         user = students[reserch]
#         print(["학생 정보"])
#         print(f"학번: {user['id']}") 
#         print(f"이름: {user['name']}") 
#         print(f"국어: {user['korean_score']}") 
#         print(f"영어: {user['english_score']}") 
#         print(f"수학: {user['math_score']}") 
#         print(f"합계: {user['total_score']}") 
#         print(f"평균: {user['avg_score']}") 
#     else:
#         print("해당 학번의 학생 정보가 없습니다")
         

# def delete_students(students):
#     sakjae = int(input("삭제 할 학번 입력: "))       
#     if sakjae in students:
#         del students[sakjae]
#         print("학생 정보가 삭제 되었습니다")
              
#     elif sakjae not in students:
#         print("해당 학번의 학생 정보가 없습니다.")

# def main():
#     # 메뉴 정의
#     menu = f""" 
#         ===== 학생 성적 관리 프로그램 =====
#         1. 학생 성적 입력
#         2. 학생 성적 출력
#         3. 학생 성적 확인
#         4. 학생 성적 삭제
#         5. 종료
#         """
#     #전체 학생 정보
#     students = {}
    
#     while True:
    
#         print(menu) # 정의 한거 출력하기
        
#         choice = int(input("메뉴 선택 (1~5): ")) # 사용자에게 원하는 메뉴 선택 받기
        
#         if choice == 1: #메뉴 선택 1번  정보 입력
#             input_students(students)
            
#             # student = {}  
#             # userid = int(input("학번을 입력하세요: ")) # 학번을 출력 받고
#             # if userid in students:          # 그 학번이 등록 된 경우 등록됨을 알리기
#             #     print("이미 등록된 학번 입니다.") 
#             #     continue # 이것이 실행이 
#             # student['id'] = userid
#             # student['name'] =input("이름를 입력하세요: \t")
#             # student['korean_score'] = int(input("국어 점수를 입력하세요: \t"))
#             # student['english_score'] = int(input("영어 점수를 입력하세요: \t"))
#             # student['math_score'] = int(input("수학 점수를 입력하세요: \t"))
#             # student['total_score'] = student['korean_score'] + student['english_score'] + student['math_score']
#             # student['avg_score'] = student['total_score'] /3
#             # students[student['id']] = student #고유 식별 번호로 전체 학생 정보에 올리기ㅣ
#             # print("성적이 저장 되었습니다.")
            
#         elif choice == 2: # 전체 학생 성적 출력
#             print_studentss(students)
#             # if not students:
#             #     print("등록된 학생 정보가 없습니다")
            
#             # else:
#             #     print(f"[ 전체 학생 성적 ]")
#             #     print(f"학번    이름    국어    영어    수학    합계    평균")

#             #     for val in students.values():
#             #         print(f"{student['id']:<8}{student['name']:<5}{student['korean_score']:>3}{student['english_score']:>7}{student['math_score']:>8}{student['total_score']:>9}{student['avg_score']:>9.2f}")
        
#         elif choice == 3:
#             reserch_students(students)
#             # reserch = int(input("조회할 학번 입력: ")) # 조회할 학번 입력 받기

#             # if reserch in students: # 조회 할 학번이 전체 학생 수에 해당 된다면 키 값 가지고 빼오기
#             #     user = students[reserch]
#             #     print(["학생 정보"])
#             #     print(f"학번: {user['id']}") 
#             #     print(f"이름: {user['name']}") 
#             #     print(f"국어: {user['korean_score']}") 
#             #     print(f"영어: {user['english_score']}") 
#             #     print(f"수학: {user['math_score']}") 
#             #     print(f"합계: {user['total_score']}") 
#             #     print(f"평균: {user['avg_score']}") 
#             # else:
#             #     print("해당 학번의 학생 정보가 없습니다")
                
#         elif choice == 4: # 삭제 할  학번 골라서 삭제 혹은 정보 없음을 알리기
#             delete_students(students)
#             # sakjae = int(input("삭제 할 학번 입력: "))       
#             # if sakjae in students:
#             #     del students[sakjae]
#             #     print("학생 정보가 삭제 되었습니다")
                
#             # elif sakjae not in students:
#             #     print("해당 학번의 학생 정보가 없습니다.")
                
#         elif choice == 5:
#             print("프로그램을 종료합니다.")
#             break
        
#         else:
#             print("1~5사이의 숫자만 입력 하세요")

# if __name__ == "__main__":
#     main()

# menu = """
# ===== 학생 성적 관리 프로그램 =====
# 1. 학생 성적 입력 
# 2. 학생 성적 출력
# 3. 학생 성적 확인
# 4. 학생 성적 삭제
# 5. 종료 
# """

# students = {}

# while True:
#     print(menu)
#     # print("\n===== 학생 성적 관리 프로그램 =====")
#     # print("1. 학생 성적 입력")
#     # print("2. 학생 성적 출력")
#     # print("3. 학생 성적 확인")
#     # print("4. 학생 성적 삭제")
#     # print("5. 종료")
    
#     choice = input("메뉴 선택 ( 1 ~ 5 )")
    
#     if choice == "1":
#         student_id = int(input("학번 입력"))
#         if student_id in students:
#             print("이미 등록 된 학번 입니다")
#             continue
#         name = input("이름 입력")
#         kor = int(input("국어 성적 입력: "))
#         eng = int(input("영어 성적 입력: "))
#         mat = int(input("수학 성적 입력: "))
#         total = kor + eng + mat
#         avg = total / 3
#         students[student_id] = {
#             "이름": name,
#             "국어": kor,
#             "영어": eng,
#             "수학": mat,
#             "합계": total,
#             "평균": avg,
            
#         }
#         print("성적이 저장 되었습니다")
        
#     elif choice == "2":
#         if not students:
#             print("저장 된 학생 정보가 없습니다.")
#             continue
#         print("[ 전체 학생 성적 ]")
#         print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
#         for sid, info in students.items():
#             print(
#                 f"{sid}\t{info['이름']}\t{info['국어']}\t{info['영어']}\t{info['수학']}\t{info['합계']}\t{info['평균']:.2f}"
#             )
            
#     elif choice == "3":
#         student_id =int(input("조회할 학번 입력: "))
#         if student_id in students:
#             info = students[student_id]
#             print("\n[학생 정보]" )
#             print(f"이름: {info['이름']}")
#             print(f"국어: {info['국어']}")
#             print(f"영어: {info['영어']}")
#             print(f"수학: {info['수학']}")
#             print(f"합계: {info['합계']}")
#             print(f"평균: {info['평균']:.2f}")
#         else:
#             print("해당 학번의 학생 정보가 없습니다.")
            
    
#     elif choice == "4":
#         student_id = int(input("삭제할 학번 입력: "))
#         if student_id in students:
#             del students[student_id]
#             print("학생 정보가 삭제 되었습니다")
            
#         else:
#             print("해당 학번의 학생 정보가 없습니다")
            
#     elif choice == "5":
#         print("프로그램을 종료합니다.")
#         break
    
#     else:
#         print("잘못된 입력입니다. 1~5 사이의 숫자를 선택하세요.")
        