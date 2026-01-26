from textwrap import dedent


class ItemService:
    def __init__(self):
        self.file_name = "items.txt"
        self.items = []

    def run(self):
        itemrun = True
        while itemrun:
            print(dedent("""
            -------------------------------------------
            교보제 관리 서비스입니다.
            
            1. 교보제 등록
            2. 교보제 전체보기
            3. 교보제 정보 수정
            4. 교보제 품절 처리
            
            9. 교보제 관리 서비스 종료.                                                 
            """))

            select = input(">>>")
            if select == "1":
                print("교보제 등록 메뉴에 진입합니다.")

            elif select == "2":
                print("교보제 전체보기 메뉴에 진입합니다.")

            elif select == "3":
                print("교보제 정보 수정 메뉴에 진입합니다.")

            elif select == "4":
                print("교보제 품절 처리")

            elif select == "9":
                print("교보제 관리 서비스 종료.")

            else:
                print("잘못된 번호를 입력하셨습니다.\n다시 입력해주세요.")

