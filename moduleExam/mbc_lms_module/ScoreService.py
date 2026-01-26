from textwrap import dedent


class ScoreService:
    def __init__(self):
        self.file_name = "scores.txt"
        self.scores = []

    def run(self):
        scorerun = True
        while scorerun:
            print(dedent("""
            -------------------------------------------
            성적관리 서비스입니다.
            
            1. 성적등록
            2. 성적보기
            3. 성적수정
            4. 성적삭제 
            
            9. 성적관리 서비스 종료.                                                                                   
            """))

            select = input(">>>")
            if select == "1":
                print("성적등록 서비스로 진입합니다.")

            elif select == "2":
                print("성적보기 서비스로 진입합니다.")

            elif select == "3":
                print("성적수정 서비스로 진입합니다.")

            elif select == "4":
                print("성적삭제 서비스로 진입합니다.")

            elif select == "9":
                print("성적관리 서비스를 종료합니다.")
                scorerun = False

            else:
                print("잘못된 번호를 입력하셨습니다.\n다시 입력해주세요.")