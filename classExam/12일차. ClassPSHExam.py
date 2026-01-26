import os
from textwrap import dedent


class MemberClass : #객체를 담당하는 클래스 사용법은 변수 = MemberClass() 생성

    #클래스에서 self는 객체의 주소를 가지고 있음.
    #def __init__(self) 클래스 구현시 필수
    def __init__(self) : #객체 생성시 만드는 기본값 (생성자)
        self.members = [] #객체에 members 리스트를 만든다.
        self.session = None #객체에 session변수를 만들고 기본값으로 None처리한다.
        self.file_name = "file_name.txt" #객체에 파일 이름을 넣는다.
        self.load_member() # 실행할 때 기본값이 생성(실행)되는 것을 이용해 처음에 돌린다.

    def save_member(self):
        #왜??? 파일처리는 수정을 하지 않는다. r(읽기전용), w(덮어쓰기), a(마지막에 추가)
        with open(self.file_name,"w",encoding = "utf-8") as f:
            #     file_name.txt  덮어쓰기          한글처리    -> f라는 변수에 넣어라
            for member in self.members: #메모리에 있는 self.members 2차원 리스트에 있는 리스트를 1줄씩 가져와!
                # member 변수에 넣어라
                f.write(f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n")



    def load_member(self): #앞으로 만들 메서드는 ()안에 self가 필수
        self.members = []  #빈 배열로 생성(혹시나, 이전에 리스트가 남아있을 수 있음)

        if not os.path.exists(self.file_name): #동일 디렉토리에 파일명이 없으면???
            self.save_member()                 #save_member() 메서드 호출 (open()으로 파일 생성)
            return                             #load_member() 메서드를 빠져나와라~

        with open(self.file_name,'r',encoding = "utf-8") as f :
            #      members.txt   읽기전용        한글처리 필수  -> f라는 변수에 넣어라
            for line in f: #f변수에 있는 파일객체를 줄단위로 반복함.
                data = line.strip().split("|") #1줄 읽은 값을 엔터제거 파이프를 기준으로 잘라
                # 1줄 읽은 값을 엔터제거 |를 기준으로 잘라 -> 1차원 리스트로 생성
                #["kkw","1234","김기원","admin","True"]
                data[4] = True if data[4] == "True" else False
                # 리스트 5번째 값이 문자열로 "True"이면 불타입 True로 변경 아니면 False
                self.members.append(data)
                #2차원 배열인 members 맨뒤에 추가~~~ for 종료할 때까지


    def add_member(self) :
        id = input("가입할 id :") #키보드로 입력한 값을 id 변수에 넣음


        if any(id in row for row in self.members):
            print("이미 존재하는 id 입니다.")
            return #함수(메서드)를 빠져나온다

        #중복 id가 없으면 아래쪽 코드 실행
        pw = input("가입할 pw :")
        name = input("가입자 명 :")
        role = "user"


        if input(dedent(f"""
        해당 내용으로 가입 확정하시겠습니까?
        이름 : {name}
        id : {id}
        pw : {pw}
        권한 : {role}
        
        (y/n)
        """)) == "y" :
            print("회원가입이 완료되었습니다.")
            self.members.append([id,pw,name,role,True])
            self.save_member()

        else:
            print("회원가입을 취소했습니다.")
            return

    def login_member(self) :
        print("로그인 페이지로 진입합니다.")
        id = input("id :")
        pw = input("pw :")

        #enumerate() 함수 활용하면 좋음. 2차원배열의 인덱스를 구하기 귀찮음.
        for member in self.members:
            if member[0] == id :
                idx = self.members.index(member)
                if member[1] == pw:
                    if not member[4]:
                        print("휴면계정입니다. 관리자에게 문의하세요.")
                        return
                    print("로그인이 완료되었습니다.")
                    self.session = idx
                    return

        print("아이디 또는 비밀번호가 잘못되었습니다.")

    def logout_member(self) :
        if self.session == None :
            print("로그인이 필요한 서비스입니다.")
            return

        if input("정말로 로그아웃 하시겠습니까? (y/n) :") == "y" :
            self.session = None
            print("로그아웃을 완료했습니다.")
        else:
            print("로그아웃을 취소했습니다.")
            return

    def modify_member(self) :
        if self.session is None: #현재 session의 값이 None이면???
            print("로그인이 필요한 서비스입니다.")
            return

        id = input("수정할 id :")
        x = id
        if any(x in row for row in self.members):
            print("이미 존재하는 id입니다.")
            return
        pw = input("수정할 pw :")
        name = input("수정할 이름 :")
        if input(dedent(f"""
        해당 내용으로 회원정보 수정을 확정하시겠습니까?
        이름 : {name}
        id : {id}
        pw : {pw}
        권한 : {self.members[self.session][3]}
        
        (y/n)
        """)) == "y" :
            print("수정을 완료했습니다.")
            self.members[self.session][0] = id
            self.members[self.session][1] = pw
            self.members[self.session][2] = name
            self.save_member()

        else:
            print("수정을 취소했습니다.")
            return

    def delete_member(self) :
        if self.session is None :
            print("로그인이 필요한 서비스입니다.")
            return

        if input("정말로 회원탈퇴하시겠습니까? (y/n) :") == "y" :
            self.members.pop(self.session)
            print("회원 탈퇴가 완료되었습니다.")
            self.session = None
            self.save_member()

        else:
            print("회원 탈퇴를 취소했습니다.")
            return


    def admin_menu(self) :
        print(dedent(f"""
        ====== 관리자 메뉴 ======
        
        1. 회원 전체보기
        2. 타회원 정보 수정
        3. 관리자 지정/해지
        4. 휴면 계정 지정/해지    
        
        9. 상위 메뉴로 나가기
                 
        """))


    def admin_member(self) :
        if self.session == None:
            print("로그인이 필요한 서비스입니다.")
            return

        if self.members[self.session][3] != "admin" :
            print("권한이 없습니다.")
            return

        self.admin_menu()
        select = input(">>>")
        if select == "1" :
            self.list_members()

        elif select == "2" :
            self.modify_admin()

        elif select == "3" :
            self.admin_select()

        elif select == "4" :
            self.admin_active()

        elif select == "9" :
            print("상위 메뉴로 돌아갑니다.")
            return



    def list_members(self) :
        name = "이름"
        id = "아이디"
        role = "권한"
        act = "활성화 여부"

        print('-' * 50)
        print(f"{name:10}{id:10}{role:10}{act:10}")
        print('-' * 50)
        for i in self.members :
            if i[4] == True :
                active = "활성화"
            else:
                active = "비활성화"
            print(f"{i[2]:10}{i[0]:11}{i[3]:12}{active:10}")

    def modify_admin(self):
        print("타회원 정보 수정 메뉴로 진입하였습니다.")
        self.list_members()
        select = input("정보를 수정할 회원의 id :")
        x = select
        if not any(x in row for row in self.members):
            print("존재하지 않는 id입니다.")
            return

        id = input("수정할 id :")
        pw = input("수정할 pw :")
        name = input("수정할 이름 :")

        if input(dedent(f"""
        해당 내용으로 변경을 확정하시겠습니까?
        
        이름 : {name}
        id : {id}
        pw : {pw}

        (y/n)
        """)) == "y":
            idx = None
            for member in self.members :
                if member[0] == x:
                    idx = self.members.index(member)
                    break
            self.members[idx][0] = id
            self.members[idx][1] = pw
            self.members[idx][2] = name
            print("지정한 회원의 정보가 수정되었습니다.")
            self.save_member()

        else:
            print("지정한 회원의 정보 수정이 취소되었습니다.")
            return


    def admin_select(self):
        print("관리자 지정 메뉴로 진입하였습니다.")
        self.list_members()
        if input("관리자 지정은 1번, 관리자 해지는 2번 입력 :") == "1" :
            select = input("관리자로 지정할 회원의 id :")
            if input("정말로 해당 회원을 관리자로 지정하시겠습니까? (y/n) :") == "y" :
                idx = None
                for i in self.members :
                    if select == i[0]:
                        idx = self.members.index(i)
                        break
                if idx == None:
                    print("잘못된 회원 id입니다.")
                    return
                self.members[idx][3] = "admin"
                print("관리자 지정을 완료했습니다.")
                self.save_member()

            else:
                print("관리자 지정을 취소했습니다.")
                return

        else:
            select = input("관리자를 해지할 회원의 id :")
            if input("정말로 해당 회원의 관리자 권한을 해지하시겠습니까? (y/n) :") == "y":
                idx = None
                for i in self.members:
                    if select == i[0]:
                        idx = self.members.index(i)
                        break
                if idx == None:
                    print("잘못된 회원 id입니다.")
                    return

                self.members[idx][3] = "user"
                print("관리자 해지를 완료했습니다.")
                self.save_member()

            else:
                print("관리자 해지를 취소했습니다.")
                return


    def admin_active(self):

        self.list_members()
        if input("휴면계정 전환은 1번, 해지는 2번 입력 :") == "1":
            select = input("휴면계정으로 전환할 회원의 id :")
            if input("정말로 해당 회원을 휴면계정 처리하시겠습니까? (y/n) :") == "y":
                idx = None
                for i in self.members:
                    if select == i[0]:
                        idx = self.members.index(i)
                        break
                if idx == None:
                    print("잘못된 회원 id입니다.")
                    return
                self.members[idx][4] = False
                print("휴면계정 전환을 완료했습니다.")
                self.save_member()

            else:
                print("휴면계정 전환을 취소했습니다.")
                return


        else:
            select = input("휴면계정을 해지할 회원의 id :")
            if input("정말로 해당 회원의 휴면계정을 해지하시겠습니까? (y/n) :") == "y":
                idx = None
                for i in self.members:
                    if select == i[0]:
                        idx = self.members.index(i)
                        break
                if idx == None:
                    print("잘못된 회원 id입니다.")
                    return
                self.members[idx][4] = True
                print("휴면계정 해지를 완료했습니다.")
                self.save_member()

            else:
                print("휴면계정 해지를 취소했습니다.")
                return






    def main_menu(self):
        print(dedent("""
        ======= 엠비씨 아카데미 LMS 시스템 =======
        
        1. 회원가입   2. 로그인   3. 로그아웃
        4. 회원정보 변경   5. 회원탈퇴
        6. 관리자 메뉴
        
        9. 시스템 종료
        """))


    def main(self) :

        while True:
            self.main_menu()
            select = input(">>>")

            if select == "1":
                self.add_member()

            elif select == "2":
                self.login_member()

            elif select == "3":
                self.logout_member()

            elif select == "4":
                self.modify_member()

            elif select == "5":
                self.delete_member()

            elif select == "6":
                self.admin_member()

            elif select == "9":
                print("시스템을 종료합니다.")
                break

            else:
                print("잘못된 번호입니다.")


app = MemberClass() #가장 중요한 포인트 (지금까지 만든 클래스를 객체로 만들고)
app.main() #객체에 있는 .main 메서드를 실행한다.