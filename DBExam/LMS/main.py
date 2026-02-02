from textwrap import dedent

from LMS.common import *
from LMS.service import *



def main():

    print(dedent("""
    =======================================
    엠비씨 LMS 시스템에 오신걸 환영합니다.
    =======================================
    1. 회원가입   2. 로그인   3. 로그아웃
    4. 회원정보 수정
    5. 게시판   6. 성적관리   7. 상점
    9. LMS 시스템 종료
    """))


def admin_menu():
    print(dedent("""
    =======================================
    관리자 전용 화면입니다.
    =======================================
    1. 회원 전체 리스트
    2. 회원 정보 수정
    3. 로그아웃
    9. 시스템 종료
    """))





run = True
while run:

        if Session.is_login():
            if Session.is_admin():
                admin_menu()
                sel = input(">>>")
                if sel == "1": MemberService.admin_list()

                elif sel == "2": MemberService.admin_modify()

                elif sel == "3": MemberService.logout()

                elif sel == "9":run = False

                continue




        main()
        sel = input(">>>")

        if sel == "1":
            MemberService.signup()

        elif sel == "2":
            MemberService.login()

        elif sel == "3":
            MemberService.logout()

        elif sel == "4":
            MemberService.modify()

        elif sel == "5":pass
        elif sel == "6":pass
        elif sel == "7":pass

        elif sel == "9":run = False

