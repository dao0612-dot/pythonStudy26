import os
from textwrap import dedent

from testExam.domain.Member import Member
from testExam.common.Session import Session

class MemberService:


    def __init__(self):
        """
        MemberService 클래스의 초기값 및 클래스를 실행할 시 돌아가는 첫번째 동작(메서드)
        """
        self.members = []
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.FILE_PATH = os.path.join(self.BASE_DIR,"..","data","members.txt")
        self.load()




    def save(self):
        """
        with open으로 지정된 파일을 덮어쓰기 상태로 열어 f변수 안에 넣는다.

        for member in self.members: 로 self.members 리스트 안에 있는
        객체를 하나씩 member변수에 넣어 연결시킨다.

        f.write(member.to_line()) 으로 member 객체안에 내장된 to_line()메서드를
        호출해서 실행하고, 규격화된 문자열로 만들어 미리 열어둔 텍스트 파일에 덮어쓴다.
        """
        with open(self.FILE_PATH, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())


    def load(self):
        """
        self.FILE_PATH가 존재하지 않을 시,
        self.save()메서드를 호출하고 메서드를 탈출한다.

        이 때 self.save()메서드는 with open으로 텍스트 파일을 열기 때문에,
        만약 텍스트 파일이 없을 시 새로 생성한다.
        """
        if not os.path.isfile(self.FILE_PATH):
            self.save()
            return


        with open(self.FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))

    def member_add(self):
        """
        [회원가입용 메서드]

        uid 변수로 아이디 인풋을 받고, self.members 리스트에 객체를
        하나씩 m에 넣어 m.uid 변수가 uid 변수와 일치하는지 확인한다.

        이 때 일치하는게 하나라도 있으면, any()함수는 True값을 반환한다.
        전부 일치하지 않으면 False를 반환한다.

        pw와 name 또한 인풋된 내용을 변수에 넣고 최종확인을 시켜준다.
        확인되면 self.members.append(Member(uid, pw,name))을 호출해
        self.members 리스트에 Member(uid,pw,name)을 실행한
        클래스 객체를 추가한다.

        role과 active는 초기값을 세팅했으므로
        결과적으론 uid,pw,name,role,active를 전부 가진 클래스 객체가
        하나 생성되고, 그것을 self.members 리스트에 추가한다.
        """

        print("\n[회원가입]")

        uid = input("아이디 :")
        if any(m.uid == uid for m in self.members):
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호 :")
        name = input("이름 :")

        if input(dedent(f"""
        해당 내용으로 회원가입을 완료하시겠습니까?
        이름 : {name}
        아이디 : {uid}
        비밀번호 : {pw}
        권한 : user
        (y/n)
        >>>""")) == "y":
            self.members.append(Member(uid, pw,name))
            self.save()
            print("회원가입이 완료되었습니다.")

        else:
            print("회원가입을 취소했습니다.")


    def login(self):
        """
        [로그인용 메서드]

        uid와 pw 변수에 인풋내용을 넣고, for문을 돌린다.
        member변수에 self.members 객체를 하나씩 넣는다.

        이 때 member객체에 uid변수가 uid 변수(인풋내용)
        과 일치할 시, 하위 구문 if로 넘어간다.

        하위구문 if에서 마찬가지로 member.pw가 pw와 일치할 시
        이번엔 member.active가 False인지 확인한다.

        이 때 member.active가 False라면,
        하위 구문인 프린트 내용과 리턴을 실행하여 메서드를 빠져나간다.

        모든 과정이 올바르게 진행됐다면, Session.login(인수)메서드를
        호출하여 Session.login_member = member 가 된다.
        Session.login(인수) 메서드 항목참조

        """
        print("\n[로그인]")
        uid = input("아이디 :")
        pw = input("비밀번호 :")

        for member in self.members:
            if member.uid == uid:
                if member.pw == pw:
                    if not member.active:
                        print("비활성 계정입니다.")
                        return

                    Session.login(member)
                    # print(Session.login_member)
                    # print(member)
                    print("로그인이 완료되었습니다.")
                    return



        print("존재하지 않는 아이디 또는 비밀번호 입니다.")


    def logout(self):
        """
        [로그아웃용 메서드]

        인풋 내용이 y라면 Session.logout()메서드를 실행해
        Session_login_member = None 가 된다.
        Session.logout() 메서드 항목참조
        """
        if input("정말로 로그아웃 하시겠습니까? (y/n) :") == "y":
            Session.logout()
            print("로그아웃을 완료했습니다.")



    def show(self):
        """
        [로그인한 회원 정보보기용 메서드]

        로그인 된 회원의 정보(Session.login_member.변수명)
        를 f포맷팅을 이용해 깔끔하게 프린트한다.

        """
        print(dedent(f"""
        {Session.login_member.name}님의 회원정보
        id = {Session.login_member.uid}
        pw = {Session.login_member.pw}
        권한 = {Session.login_member.role}
        """))

    def modify_menu(self):
        """
        [회원정보 수정 메뉴용 메서드]
        """
        print(dedent(f"""
        --- 회원정보 수정 선택지 ---
        1. id
        2. pw
        3. 이름

        그 외. 뒤로가기
        """))

    def modify(self):
        """
        [회원정보 수정용 메서드]

        if not Session.is_login(): 문구로 로그인인지 비로그인인지 판단

        self.show()와 self.modify_menu() 메서드를 통해
        내 정보의 현 상황을 확인 후, 수정할 정보를 선택

        uid 즉 아이디의 경우만 any()함수로 중복되지 않는지 확인한다.

        나머지는 정말로 바꿀건지 if문으로 물어보고, y를 누르면
        Session.login_member.uid = uid로 변경.
        self.members의 리스트 안에 있는 객체에 연결된
        Session.login_member.uid를 변경함으로써,
        동일하게 연결 되어있는 리스트 안에 객체의 uid가
        변경된다.
        그 후 self.save()메서드를 호출해서
        텍스트 파일에 변경된 리스트를 저장한다.

        pw, name 이하동문

        """
        if not Session.is_login():
            print("로그인이 필요한 서비스입니다.")
            return


        self.show()
        self.modify_menu()
        sel = input("변경하실 정보를 선택 :")
        if sel == "1":
            uid = input("변경할 id :")
            if any(m.uid == uid for m in self.members):
                print("이미 존재하는 아이디입니다.")
                return
            if input(f"{uid}로 아이디를 변경하시겠습니까? (y/n) :") == "y":
                Session.login_member.uid = uid
                self.save()
                print("아이디 변경을 완료했습니다.")

            else:
                print("아이디 변경을 취소했습니다.")

        elif sel == "2":
            pw = input("변경하실 pw :")
            if input(f"{pw}로 비밀번호를 변경하시겠습니까? (y/n) :") == "y":
                Session.login_member.pw = pw
                self.save()
                print("비밀번호 변경을 완료했습니다.")

            else:
                print("비밀번호 변경을 취소했습니다.")

        elif sel == "3":
            name = input("변경하실 이름 :")
            if input(f"{name}으로 이름을 변경하시겠습니까? (y/n) :") == "y":
                Session.login_member.name = name
                self.save()
                print("이름 변경을 완료했습니다.")

            else:
                print("이름 변경을 취소했습니다.")

        else:
            print("회원정보 수정을 취소합니다.")
            return



    def delete(self):
        """
        [회원탈퇴용 메서드]

        로그인한 회원(Session.login_member)기준으로,
        정말로 회원 탈퇴를 할 것인지 물어보고
        y를 누르면 회원탈퇴 처리 후 self.save() 메서드를 호출해
        변경된 리스트를 텍스트 파일에 저장한다.

        """
        print("\n[회원탈퇴]")

        if input(f"{Session.login_member.name}님 정말로 회원탈퇴를 하시겠습니까? (y/n) :") == "y":
                self.members.remove(Session.login_member)
                Session.logout()
                self.save()
                print("회원탈퇴를 완료했습니다.")
                return

        else:
            print("회원탈퇴를 취소했습니다.")




    def admin_list(self):
        """
        [관리자용 전체 회원 리스트 메서드]

        상단의 분류는 따로 출력 후, 회원들의 정보는
        for문을 통해 self.members의 객체의 정보를
        하나씩 member에 넣어서 print문을 실행한다.

        """
        print("\n[회원 리스트]")
        print("-" * 60)
        print(f"{'이름':10}{'id':10}{'권한':10}{'상태':10}")
        print("-" * 60)

        for member in self.members:
            if member.active:
                active = "활성"
            else:
                active = "비활성"

            print(f"{member.name:10}{member.uid:10}{member.role:10}{active:10}")


    def admin_modify(self):
        """
        [관리자용 유저 정보 수정 메서드]
        전체 유저 보기 메서드를 호출하여 리스트를 확인하고,
        그 중에서 변경할 회원의 id를 인풋받는다.
        이 때 인풋받은 회원의 id가 for문 검증을 통해
        리스트 안에 없을 시 회원이 존재하지 않는다고 반환

        이후 변경할 정보를 메뉴 번호로 인풋받은 후
        알맞는 메뉴의 코드를 실행
        각각의 메뉴에서 항상 최후 확인을 실행
        수정을 완료하면 self.save()를 호출하여
        지속적으로 텍스트 파일에 갱신한다.

        """
        self.admin_list()
        user = None
        sel = input("정보를 변경할 회원의 id :")
        for member in self.members:
            if sel == member.uid:
                user = member

        if user == None:
            print("존재하지 않는 회원입니다.")
            return
        print(dedent("""
        ------ 변경할 회원정보 ------
        1. id   2. 이름   3. 권한
        """))

        select = input(">>>")
        if select == "1":
            uid = input("변경할 id :")
            if input(f"{user.name}님의 id를 {uid}로 변경하시겠습니까? (y/n) :") == "y":
                user.uid = uid
                self.save()
                print(f"{user.name}님의 id 변경이 완료되었습니다.")

            else:
                print(f"{user.name}님의 id 변경을 취소했습니다.")

        elif select == "2":
            name = input("변경할 이름 :")
            if input(f"{user.name}님의 이름을 {name}으로 변경하시겠습니까? (y/n) :") == "y":
                user.name = name
                self.save()
                print(f"{user.name}님으로 이름 변경 완료되었습니다.")

            else:
                print(f"{user.name}님의 이름 변경을 취소했습니다.")

        elif select == "3":
            role = input("변경할 권한\n(admin / manager / user)\n>>>")
            if  role == "user" or role == "manager" or role == "admin":
                if input(f"{user.name}님의 권한을 {role}로 변경하시겠습니까? (y/n) :") == "y":
                    user.role = role
                    self.save()
                    print(f"{user.name}님의 권한 변경을 완료했습니다.")

                else:
                    print(f"{user.name}님의 권한 변경을 취소했습니다.")
            else:
                print("올바른 권한명이 아닙니다.")
                return

        else:
            print("잘못된 번호를 입력하셨습니다.")


    def admin_active(self):
        """
        [관리자용 휴면계정 지정/해제 메서드]
        self.admin_modify()와 동일하게 특정 유저의 아이디를 인풋받고,
        그 아이디를 검증, 이후 정말로 코드를 실행할 것인지 여부 확인,
        최종적으로 지정한 유저의 .active = False처리 시킨다.
        해제는 .active = True처리 시킨다.
        변동사항이 발생했으므로 self.save() 메서드를 호출하여
        텍스트 파일에 저장한다.

        """

        self.admin_list()
        print(dedent("""
        ------ 휴면계정 지정/해제 ------
        1. 휴면계정 지정
        2. 휴면계정 해제
        
        그 외. 뒤로가기
        """))

        sel = input(">>>")
        if sel == "1":
            user = None
            select = input("휴면계정 지정할 회원 id :")
            for member in self.members:
                if member.uid == select:
                    user = member
                    if not user.active:
                        print("이미 비활성화된 계정입니다.")
                        return

            if user == None:
                print("존재하지 않는 회원입니다.")
                return

            if input(f"{user.name}님의 계정을 비활성화 하시겠습니까? (y/n) :") == "y":
                user.active = False
                self.save()
                print("비활성화를 완료했습니다.")

            else:
                print("비활성화를 취소했습니다.")

        elif sel == "2":
            user = None
            select = input("휴면계정 해제할 회원 id :")
            for member in self.members:
                if member.uid == select:
                    user = member
                    if user.active:
                        print("이미 활성화된 계정입니다.")
                        return

            if user == None:
                print("존재하지 않는 회원입니다.")
                return

            if input(f"{user.name}님의 계정을 활성화 하시겠습니까? (y/n) :") == "y":
                user.active = True
                self.save()
                print("활성화를 완료했습니다.")

            else:
                print("활성화를 취소했습니다.")


        else:
            print("작업을 취소합니다.")



    def member_guest_menu(self):
        """
        로그인하지 않았을 시 나오는 게스트 메뉴
        if not Session.is_login():

        """
        print(dedent("""
        ------ LMS 회원가입/로그인 시스템 ------
        1. 회원가입
        2. 로그인
        
        9. LMS시스템으로 돌아가기                
        """))

    def member_main_menu(self):
        """
        로그인 했을 시 나오는 회원 전용 메뉴

        """
        print(dedent("""
        ------ LMS 회원정보관리 시스템 ------
        1. 로그아웃
        2. 회원정보수정
        3. 회원탈퇴
        
        9. LMS시스템으로 돌아가기
        """))

    def admin_menu(self):
        """
        로그인 한 유저의 role (등급)이 admin일 경우
        나오는 메뉴

        """
        print(dedent("""
        ------ 관리자 전용 메뉴 ------
        1. 회원 전체 리스트
        2. 회원정보 변경
        3. 휴면계정 지정/해제
        
        9. 관리자 메뉴 종료
        """))






    def run(self):
        subrun = True
        while subrun:
            if not Session.is_login():
                self.member_guest_menu()
                sel = input(">>>")
                if sel == "1": self.member_add()
                elif sel == "2": self.login()
                elif sel == "9": subrun = False
                else: print("잘못된 번호를 입력하셨습니다.")



            else:
                if Session.login_member.role == "admin":
                    self.admin_menu()
                    sel = input(">>>")
                    if sel == "1": self.admin_list()
                    elif sel == "2": self.admin_modify()
                    elif sel == "3": self.admin_active()
                    elif sel == "9": subrun = False

                else:
                    self.member_main_menu()
                    sel = input(">>>")
                    if sel == "1": self.logout()
                    elif sel == "2" : self.modify()
                    elif sel == "3" : self.delete()
                    elif sel == "9" : subrun = False
                    else: print("잘못된 번호를 입력하셨습니다.")



