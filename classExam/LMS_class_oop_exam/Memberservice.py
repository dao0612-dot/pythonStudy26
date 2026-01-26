import os
from textwrap import dedent
from Member import Member

class MemberService:


    def __init__(self):
        self.file_name = "members.txt"
        self.members = []
        self.session = None
        self.load_members()

#=======================================================================================================================
#=======================================================================================================================


    def save_members(self):

        with open(self.file_name, "w",encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())


    def load_members(self):

        if not os.path.isfile(self.file_name):
            self.save_members()
            return

        with open(self.file_name, "r",encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))





    def run(self):
        run = True
        while run:
            self.main_menu()

            select = input(">>>")

            if select == "1": self.add_member()
            elif select == "2": self.login_member()
            elif select == "3": self.logout_member()
            elif select == "4": self.modify_member()
            elif select == "5": self.delete_member()
            elif select == "9": run = False
            else:
                print("시스템 종료")

#=======================================================================================================================
#=======================================================================================================================

    def main_menu(self):
        print(dedent("""
        ==== 엠비씨 LMS 회원관리 (Member) 베이스 ====
        1. 회원가입
        2. 로그인
        3. 로그아웃
        4. 회원 정보 수정
        5. 회원탈퇴
        9. 프로그램 종료
        """))

    def modify_menu(self):
        print(dedent("""
        ------ 변경할 정보 선택 ------
        1. 아이디
        2. 비밀번호
        3. 이름                     
        """))

    def admin_menu(self):
        print(dedent("""
        ==== 관리자 전용 메뉴 ====
        1. 전체 회원 리스트 보기
        2. 회원 권한 변경
        3. 블랙리스트 지정/해제
        9. 프로그램 종료
        """))

#=======================================================================================================================
#=======================================================================================================================

    def add_member(self):
        print("\n[회원가입]")

        uid = input("아이디 :")
        member = self.find_member(uid)

        if member is not None:
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호 :")
        name = input("이름 :")

        if input(dedent(f"""
        아래 내용으로 회원가입을 확정하시겠습니까?
        이름 : {name}
        id : {uid}
        pw : {pw}
        권한 : user
        (y/n)
        """)) == "y" :
            self.members.append(Member(uid, pw, name))
            self.save_members()
            print("회원가입이 완료되었습니다.")

        else:
            print("회원가입을 취소했습니다.")



    def login_member(self):
        if self.session is not None :
            print("이미 로그인 되어있습니다.")
            return

        print("\n[로그인]")

        id = input("아이디 :")
        pw = input("비밀번호 :")

        member = self.find_member(id)
        if member:
            if member.pw == pw:
                if member.active == False:
                    print("비활성 계정입니다.")
                    return

                print("로그인되었습니다.")
                self.session = member
                #print(self.members.index(self.session))
                if member.role == "admin":
                    self.admin_member()


            else:
                print("비밀번호가 틀렸습니다.")
                return
        else:
            print("존자하지 않는 아이디입니다.")
            return


    def logout_member(self):
        if self.session is None:
            print("로그인이 필요한 서비스입니다.")
            return

        if input("정말로 로그아웃하시겠습니까? (y/n) :") == "y" :
            self.session = None
            print("로그아웃 완료")

        else:
            print("로그아웃 취소")

    def modify_member(self):
        print("\n[회원 정보 수정]")

        if self.session is None:
            print("로그인이 필요한 서비스입니다.")
            return

        self.modify_menu()
        sel = input("변경할 정보 선택 :")
        if sel == "1":
            uid = input("변경할 아이디 :")
            if self.find_member(uid) is not None:
                print("중복되는 아이디입니다.")
                return

            if input(f"{uid}로 아이디 변경을 확정하시겠습니까? (y/n) :") == "y":
                self.session.uid = uid
                #print(self.members,self.session.id)
                self.save_members()
                print("아이디 변경을 완료했습니다.")


            else:
                print("아이디 변경을 취소했습니다.")


        elif sel == "2":
            pw = input("변경할 비밀번호 :")
            if input(f"{pw}로 비밀번호 변경을 확정하시겠습니까? (y/n) :") == "y" :
                self.session.pw = pw
                self.save_members()
                print("비밀번호 변경을 완료했습니다.")

            else:
                print("비밀번호 변경을 취소했습니다.")


        elif sel == "3":
            name = input("변경할 이름 :")
            if input(f"{name}으로 이름 변경을 확정하시겠습니까? (y/n) :") == "y" :
                self.session.name = name
                self.save_members()
                print("이름 변경을 완료했습니다.")

            else:
                print("이름 변경을 취소했습니다.")


        else:
            print("변경을 취소했습니다.")

    def delete_member(self):
        print("\n[회원탈퇴]")
        if self.session is None:
            print("로그인이 필요한 서비스입니다.")
            return

        if input("정말로 회원탈퇴를 하시겠습니까? (y/n) :") == "y" :
            #print(type(self.session))
            idx = self.members.index(self.session)
            self.members.pop(idx)
            self.session = None
            self.save_members()
            print("회원탈퇴를 완료했습니다.")

        else:
            print("회원탈퇴를 취소했습니다.")

    def find_member(self, uid):
        for member in self.members:
            if member.uid == uid:
                return member

        return None

    def admin_member(self):
        adminrun = True
        while adminrun:
            self.admin_menu()
            select = input(">>>")

            if select == "1": self.admin_list()
            elif select == "2": self.admin_role()
            elif select == "3": self.admin_black()
            elif select == "9": adminrun = False

            else:
                print("잘못된 번호입니다.")

    def admin_list(self):
        print("\n[전체 회원 리스트]")

        print("-" * 60)
        print(f"{'이름':10} {'id':10} {'권한':10} {'상태'}")
        print("-" * 60)

        for member in self.members:
            state = "활성" if member.active else "비활성"
            print(f"{member.name:10} {member.uid:10} {member.role:10} {state}")

    def admin_role(self):
        print("\n[권한 변경]")

        uid = input("권한을 변경할 유저의 id :")
        member = self.find_member(uid)
        if member is None:
            print("존재하지 않는 유저입니다.")
            return

        role = input("admin / manager / user 중 권한 선택 :")
        if input(f"{member.name}님의 권한을 {role}로 변경 확정하시겠습니까? (y/n) :") == "y":
            member.role = role
            self.save_members()
            print("권한 변경을 완료했습니다.")

        else:
            print("권한 변경을 취소했습니다.")



    def admin_black(self):
        print("\n[블랙리스트 지정/해제]")

        sel = input("1.블랙리스트 지정\n2.블랙리스트 해제\n>>>")
        if sel == "1":
            uid = input("블랙리스트로 지정할 유저의 id :")
            member = self.find_member(uid)
            if member is None:
                print("존재하지 않는 유저입니다.")
                return
            if input(f"정말로 {member.name}님을 블랙하시겠습니까? (y/n) :") == "y":
                member.active = False
                self.save_members()
                print("블랙을 완료했습니다.")
            else:
                print("블랙을 취소했습니다.")

        elif sel == "2":
            uid = input("블랙리스트를 해제할 유저의 id :")
            member = self.find_member(uid)
            if member is None:
                print("존재하지 않는 유저입니다.")
                return
            if input(f"정말로 {member.name}님의 블랙을 해제하시겠습니까? (y/n) :") == "y":
                member.active = True
                self.save_members()
                print("블랙 해제를 완료했습니다.")
            else:
                print("블랙 해제를 취소했습니다.")

        else:
            print("블랙리스트 메뉴를 취소합니다.")


