#회원에 관한 crud를 구현
#부메뉴와 함께 run() 메서드를 진행
from textwrap import dedent


class MemberService:
    def __init__(self):
        # 클래스 생성 시 필요한거
        self.file_name = "members.txt"
        self.members = [] #모든 회원이 들어 있는 2차원 리스트



    def run(self):
        #부메뉴 구현 메서드
        subrun = True
        while subrun:
            print(dedent("""
            -------------------------------------------
            회원관리 서비스입니다.
            
            1. 로그인
            2. 회원가입
            3. 회원수정
            4. 회원탈퇴
            5. 로그아웃
            
            9. 회원서비스 종료.
            """))

            select = input(">>>")
            if select == "1":
                print("로그인 메서드 호출")

            elif select == "2":
                print("회원가입 메서드 호출")

            elif select == "3":
                print("회원수정 메서드 호출")

            elif select == "4":
                print("회원탈퇴 메서드 호출")

            elif select == "5":
                print("로그아웃 메서드 호출")

            elif select == "9":
                print("회원서비스 종료")
                subrun = False

            else:
                print("잘못된 번호를 입력하셨습니다.\n다시 입력해주세요.")