import os
import json
from textwrap import dedent



class BoardService:
    def __init__(self):
        self.file_name = "boards.txt"
        self.sn_name = "sn.txt"
        self.boards = {}
        self.sn = []
        self.load_boards()
        self.load_sn()
        # 0     1   2   3    4    5    6
        #아이디 이름 제목 내용 좋아요 조회수 날짜

    def run(self):
        boardrun = True
        while boardrun:
            # print(type(self.sn))
            # print(self.sn)
            # print(self.boards)
            # print(type(self.boards))
            print(dedent("""
            -------------------------------------------
            자료게시판 서비스입니다.
            
            1. 자료게시글 등록
            2. 자료게시글 보기
            3. 자료게시글 수정
            4. 자료게시글 삭제
            
            9. 자료게시글 서비스 종료
            """))
            select = input(">>>")
            if select == "1":
                print("자료게시글 등록 서비스에 진입합니다.")
                self.add_board()

            elif select == "2":
                print("자료게시글 보기 서비스에 진입합니다.")
                self.list_boards()
                self.view_board()

            elif select == "3":
                print("자료게시글 수정 서비스에 진입합니다.")
                self.modify_board()

            elif select == "4":
                print("자료게시글 삭제 서비스에 진입합니다.")
                self.delete_board()

            elif select == "9":
                print("자료게시글 서비스를 종료합니다.")
                boardrun = False

            else:
                print("잘못된 번호를 입력하셨습니다.\n다시 입력해주세요.")


    def save_boards(self):

        with open(self.file_name, "w", encoding = "utf-8") as f:
            json.dump(self.boards, f,ensure_ascii = False)

    def save_sn(self):

        with open(self.sn_name, "w", encoding = "utf-8") as f:
            data = self.sn
            f.write(f"{data}")


    def load_boards(self):

        if not os.path.exists(self.file_name):
            self.save_boards()
            return

        with open(self.file_name, "r", encoding = "utf-8") as f:
            data = json.load(f)
            for i in data.keys() :
                self.boards[int(i)] = data[i]

        #print(self.boards)

    def load_sn(self):

        if not os.path.exists(self.sn_name):
            self.save_sn()
            return

        with open(self.sn_name, "r", encoding = "utf-8") as f:
            data = f.readlines()
            self.sn.append(int(data[0]))




    def add_board(self):
        print("자료게시글 등록 메뉴에 진입했습니다.")
        name = input("이름 :")
        id = input("id :")
        title = input("제목 :")
        detail = input("내용 :")
        day = input("날짜 :")


        if input(dedent(f"""
        해당 내용으로 게시글 등록을 확정하시겠습니까?

        이름 = {name}
        아이디 = {id}

        제목 = {title}
        내용 = {detail}

        날짜 = {day}

        (y/n)
        """)) == "y" :

            if self.sn == [] :
                self.sn.append(0)
            self.sn[0] += 1
            self.boards[self.sn[0]] = [id, name, title, detail, day, 0, 0]
            self.save_boards()
            self.save_sn()
            print("게시글 등록이 완료되었습니다.")

    def list_boards(self):

        sn = "번호"
        name = "이름"
        id = "id"
        title = "제목"
        detail = "내용"
        day = "날짜"
        hit = "좋아요"
        view = "조회수"

        print("-" * 40)
        print(f"{sn:5}{name:5}{id:5}{title:10}{detail:10}{day:<5}{hit:<5}{view:<5}")
        print("-" * 40)

        board = self.boards
        for i in self.boards.keys():

            if len(board[i][2]) >= 5 and len(board[i][3]) >= 5:
                short = board[i][2][:5] + "..."
                shorts = board[i][3][:5] + "..."
                print(
                    f"{i:<5}{board[i][1]:5}{board[i][0]:5}{short:10}{shorts:10}{board[i][4]:<5}{board[i][5]:<5}{board[i][6]:<5}")
                continue

            if len(board[i][2]) >= 5 :
                short = board[i][2][:5] + "..."
                print(f"{i:<5}{board[i][1]:5}{board[i][0]:5}{short:10}{board[i][3]:10}{board[i][4]:<5}{board[i][5]:<5}{board[i][6]:<5}")
                continue

            if len(board[i][3]) >= 5 :
                short = board[i][3][:5] + "..."
                print(f"{i:<5}{board[i][1]:5}{board[i][0]:5}{board[i][2]:10}{short:10}{board[i][4]:<5}{board[i][5]:<5}{board[i][6]:<5}")
                continue


            print(f"{i:<5}{board[i][1]:5}{board[i][0]:5}{board[i][2]:10}{board[i][3]:10}{board[i][4]:<5}{board[i][5]:<5}{board[i][6]:<5}")


    def view_board(self):
        select = input("자세히 보기는 1번, 뒤로가기는 2번을 입력 :")
        if select == "1":
            selection = int(input("자세히 볼 게시글의 번호를 입력 :"))
            if selection not in self.boards.keys():
                print("존재하지 않는 번호입니다.")
                return

            self.boards[selection][6] += 1
            print(dedent(f"""
            제목 : {self.boards[selection][2]}
            
            작성자 : {self.boards[selection][1]}
            작성자 id : {self.boards[selection][0]}
            작성 날짜 : {self.boards[selection][4]}
            
            내용 : {self.boards[selection][3]}
            
            조회수 : {self.boards[selection][6]}
            좋아요 : {self.boards[selection][5]}
                                                                                    
            """))

            if input("좋아요를 누르시겠습니까? (y/n) :") == "y" :
                print("좋아요를 눌렀습니다.")
                self.boards[selection][5] += 1
                self.save_boards()

            else:
                print("다음에 더욱 좋은 게시글로 찾아뵙겠습니다.")
                self.save_boards()

        else:
            print("자세히 보기를 취소했습니다.")


    def modify_menu(self):
        print(dedent("""
        -----------------------------------
        게시글에서 수정하실 내용을 선택하세요.
        
        1. 이름   2. 아이디   3. 제목   4. 내용
        5. 날짜
        """))


    def modify_board(self):
        print("게시글 수정 메뉴에 진입했습니다.")
        self.list_boards()
        select = int(input("수정할 게시글의 번호 :"))
        if select not in self.boards.keys():
            print("존재하지 않는 번호입니다.")
            return

        print(f"{self.boards[select][1]}회원님의 게시글 수정을 시작합니다.")
        self.modify_menu()
        selection = input("수정하실 내용의 번호를 입력해주세요 :")
        if selection == "1":
            print("이름 변경을 시작합니다.")
            name = input("수정하실 이름 :")
            if input(f"정말로 이름을 {name}으로 수정하시겠습니까? (y/n) :") == "y" :
                self.boards[select][1] = name
                self.save_boards()
                print("이름 수정이 완료되었습니다.")

            else:
                print("이름 수정을 취소했습니다.")

        elif selection == "2":
            print("아이디 변경을 시작합니다.")
            id = input("수정하실 id :")
            if input(f"정말로 id를 {id}로 수정하시겠습니까? (y/n) :") == "y" :
                self.boards[select][0] = id
                self.save_boards()
                print("id 수정이 완료되었습니다.")

            else:
                print("id 수정을 취소했습니다.")

        elif selection == "3":
            print("제목 변경을 시작합니다.")
            title = input("수정할 제목 :")
            if input(f"정말로 제목을 {title}로 수정하시겠습니까? (y/n) :") == "y" :
                self.boards[select][2] = title
                self.save_boards()
                print("제목 수정이 완료되었습니다.")

            else:
                print("제목 수정을 취소했습니다.")

        elif selection == "4":
            print("내용 변경을 시작합니다.")
            detail = input("수정할 내용 :")
            if input(f"정말로 내용을 {detail}로 수정하시겠습니까? (y/n) :") == "y" :
                self.boards[select][3] = detail
                self.save_boards()
                print("내용 수정이 완료되었습니다.")

            else:
                print("내용 수정을 취소했습니다.")

        elif selection == "5":
            print("날짜 변경을 시작합니다.")
            day = input("수정할 날짜 :")
            if input(f"정말로 날짜를 {day}로 수정하시겠습니까? (y/n) :") == "y" :
                self.boards[select][4] = day
                self.save_boards()
                print("날짜 수정이 완료되었습니다.")

            else:
                print("날짜 수정을 완료했습니다.")

        else:
            print("잘못된 숫자를 입력하셨습니다.")



    def delete_board(self):
        print("자료 게시글 삭제 메뉴로 진입합니다.")

        self.list_boards()
        select = int(input("삭제하실 게시글의 번호를 입력해주세요."))
        if select not in self.boards.keys():
            print("존재하지 않는 번호입니다.")
            return

        if input("정말로 해당 게시글을 삭제하시겠습니까? (y/n) :") == "y" :
            del self.boards[select]
            self.save_boards()
            print("게시글 삭제를 완료했습니다.")

        else:
            print("게시글 삭제를 취소했습니다.")









