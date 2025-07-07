menu = """
===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료
"""

students = {}

while True:
    print(menu)
    choice =int(input("메뉴 선택 (1~5)"))
    
    if choice == 1: # 학생 성적 입력
        stu_id = int(input("학번 입력해주세요: "))
        if stu_id in students:
            print("이미 등록 되어 있는 학번 임")
            continue
        name = input("이름을 입력 하세요")
        korea = int(input("국어 점수를 입력 하세요"))
        english= int(input("영어 점수를 입력 하세요"))
        math = int(input("수학 점수를 입력 하세요"))
        total = korea + english + math
        avg = total / 3
        
        students[stu_id] = {
            '이름' : name,
            '국어' : korea,
            '영어' : english,
            '수학' : math,
            '합계' : total,
            '평균' : avg,
        }
        print("저장이 완료 되었음")
        
    elif choice == 2: # 학생 성적 출력
        if not students:
            print("학생 정보가 없음")
            continue
        
        print("\n[ 전체 학생 정보 ]")
        print("학번,\t이름,\t,국어\t영어,\t수학,\t합계\t평균")
        for val, sml in students.items():
            print(f"{val}\t{sml['이름']}\t{sml['국어']}\t{sml['영어']}\t{sml['수학']}\t{sml['합계']}\t{sml['평균']:.2f}")
            
    elif choice == 3: # 학생 성적 확인
        stu_id = int(input("조회 할 학번"))
        if stu_id not in students:
            print("학생 정보 없음")
            continue
        info = students[stu_id]
        print("\n[학생 정보]")
        print(f"학번: {stu_id}")
        print(f"이름: {info['이름']}")
        print(f"국어: {info['국어']}")
        print(f"영어: {info['영어']}")
        print(f"수학: {info['수학']}")
        print(f"합계: {info['합계']}")
        print(f"평균: {info['평균']:.2f}")
        
    elif choice == 4: # 학생 성적 삭제
        stu_id = int(input("삭제 할 학번"))
        if stu_id not in students:
            print("학생 정보 없음")
            continue
        del students[stu_id]
        print("학생 정보 삭제")
        
    elif choice == 5: # 종료
        print("이제 종료함")
        break
    
    else:
        print("1~5부터의 번호를 입력해주세요")
        
    
        