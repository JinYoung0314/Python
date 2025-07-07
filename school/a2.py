def input_student(students):
    student_id = int(input("학번 입력: "))
    if student_id in students:
                print("이미 등록된 학번 입니다.")
                return
        
    name = input("이름 입력: ")
    korea = int(input("국어 성적 입력: "))
    english = int(input("영어 성적 입력: "))
    math = int(input("수학 성적 입력: "))
    total = korea + english + math
    avg = total / 3
            
    students[student_id] = {
        '이름': name,
        '국어': korea,
        '영어': english,
        '수학': math,
        '합계': total,
        '평균': avg,
    }
    print("성적이 저장 되었습니다.")
            

def print_all_students(students):
    if not students:
            print("지정된 학생 정보가 없습니다")  
            return
                    
    print("\n[ 전체 학생 정보 ]")
    print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
    for val, sml in students.items():
        print(f"{val}\t{sml['이름']}\t{sml['국어']}\t{sml['영어']}\t{sml['수학']}\t{sml['합계']}\t{sml['평균']:.2f}")


def search_student(students):
    student_id =int(input("조회할 학번 입력: "))
    if student_id not in students:
        print("해당 학생의 정보가 없습니다.")
        return
    info = students[student_id]    
    print("\n[학생 정보]")
    print(f"학번: {student_id}")
    print(f"이름: {info['이름']}")
    print(f"국어: {info['국어']}")
    print(f"수학: {info['수학']}")
    print(f"영어: {info['영어']}")
    print(f"합계: {info['합계']}")
    print(f"평균: {info['평균']}")

def delete_student(students):
    student_id = int(input("삭제할 학번 입력: "))
    if student_id not in students:
        print("존재 하지 않는 학번 입니다")
        return
            
    del students[student_id]
    print("학생 정보가 삭제 되었습니다.")

def main():
    #메뉴 출력
    menu = """
    ===== 학생 성적 관리 프로그램 =====
    1. 학생 성적 입력
    2. 학생 성적 출력
    3. 학생 성적 확인
    4. 학생 성적 삭제
    5. 종료
    """

    # 딕셔너리 사용으로 인한 밖에 학생 정보 정의
    students = {}

    # 계속 묻는 것이기 때문에 while True 사용
    while True:
        print(menu)   
        choice =int(input(" 메뉴 선택 (1~5): ")) # 그 후 바로 물어보기 choice

    # choice에 따른 if 조건식 걸기
        if choice == 1:
            input_student(students)
            # student_id = int(input("학번 입력: "))
            # if student_id in students:
            #     print("이미 등록된 학번 입니다.")
            #     continue
            # name = input("이름 입력: ")
            # korea = int(input("국어 성적 입력: "))
            # english = int(input("영어 성적 입력: "))
            # math = int(input("수학 성적 입력: "))
            # total = korea + english + math
            # avg = total / 3
            
            # students[student_id] = {
            #     '이름': name,
            #     '국어': korea,
            #     '영어': english,
            #     '수학': name,
            #     '합계': total,
            #     '평균': avg,
            # }
            # print("성적이 저장 되었습니다.")
            
        elif choice == 2:
            print_all_students(students)
            # if not students:
            #     print("지정된 학생 정보가 없습니다")  
            #     continue
                    
            # print("\n[ 전체 학생 정보 ]")
            # print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
            # for val, sml in students.items():
            #     print(f"{val}\t{sml['이름']}\t{sml['국어']}\t{sml['영어']}\t{sml['수학']}\t{sml['합계']}\t{sml['평균']:.2f}")

        elif choice == 3:
            search_student(students)
            # student_id =int(input("조회할 학번 입력: "))
            # if student_id not in students:
            #     print("해당 학생의 정보가 없습니다.")
            #     continue
            # info = students[student_id]    
            # print("\n[학생 정보]")
            # print(f"학번: {student_id}")
            # print(f"이름: {info['이름']}")
            # print(f"국어: {info['국어']}")
            # print(f"수학: {info['수학']}")
            # print(f"영어: {info['영어']}")
            # print(f"합계: {info['합계']}")
            # print(f"평균: {info['평균']}")
            
        elif choice == 4:
            delete_student(students)
            # student_id = int(input("삭제할 학번 입력: "))
            # if student_id not in students:
            #     print("존재 하지 않는 학번 입니다")
            #     continue
            
            # del students[student_id]
            # print("학생 정보가 삭제 되었습니다.")
        
        elif choice == 5:
            print("프로그램을 종료합니다")
            break
        
        else:
            print("1~5 사이의 숫자를 선택하세요:")
            
if __name__ == "__main__":
    main()
    
    # choice에 따른 오류메시지 조건식 걸기
    # choice 범위에서 벗어나는 것 예외처리 하기