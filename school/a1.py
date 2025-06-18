
# 메뉴 정의
menu = f""" 
    ===== 학생 성적 관리 프로그램 =====
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
        std_data = {}  
        userid = int(input("학번을 입력하세요: ")) # 학번을 출력 받고
        if userid in std_dict:          # 그 학번이 등록 된 경우 등록됨을 알리기
            print("이미 등록된 학번 입니다.") 
            continue
        std_data['id'] = userid
        std_data['name'] =input("이름를 입력하세요: \t")
        std_data['korean_score'] = int(input("국어 점수를 입력하세요: \t"))
        std_data['english_score'] = int(input("영어 점수를 입력하세요: \t"))
        std_data['math_score'] = int(input("수학 점수를 입력하세요: \t"))
        std_data['total_score'] = std_data['korean_score'] + std_data['english_score'] + std_data['math_score']
        std_data['avg_score'] = std_data['total_score'] /3
        std_dict[std_data['id']] = std_data #고유 식별 번호로 전체 학생 정보에 올리기ㅣ
        print("성적이 저장 되었습니다.")
        
    elif choice == 2: # 전체 학생 성적 출력
        print(f"[ 전체 학생 성적 ]")
        print(f"학번    이름    국어    영어    수학    합계    평균")
        #오류 체크 밑의 print문 for문으로 바꾸어서 전체 학생 출력하기 지금은 1명의 학생 뿐임
            # print(f"{std_data['id']:<8}{std_data['name']:<5}{std_data['korean_score']:>3}{std_data['english_score']:>7}{std_data['math_score']:>8}{std_data['total_score']:>9}{std_data['avg_score']:>9.2f}")
   
    elif choice == 3:
        reserch = int(input("조회할 학번 입력: ")) # 조회할 학번 입력 받기
        #오류 체크 개인 학생 정보가 아닌 user 변수명으로 바꿔야 할 듯 함
        if reserch in std_dict: # 조회 할 학번이 전체 학생 수에 해당 된다면 키 값 가지고 빼오기
            user = std_dict[reserch]
            print(["학생 정보"])
            print(f"학번: {std_data['id']}") 
            print(f"이름: {std_data['name']}") 
            print(f"국어: {std_data['korean_score']}") 
            print(f"영어: {std_data['english_score']}") 
            print(f"수학: {std_data['math_score']}") 
            print(f"합계: {std_data['total_score']}") 
            print(f"평균: {std_data['avg_score']}") 
        else:
            print("해당 학번의 학생 정보가 없습니다")
            
    elif choice == 4: # 삭제 할  학번 골라서 삭제 혹은 정보 없음을 알리기
        sakjae = input("삭제 할 학번 입력: ")       
        if user in std_dict[sakjae]:
            del std_dict
        elif user not in std_dict[sakjae]:
            print("해당 학번의 학생 정보가 없습니다.")
            
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("1~5사이의 숫자만 입력 하세요")