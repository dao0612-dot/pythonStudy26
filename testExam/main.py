from textwrap import dedent

from testExam.common.Session import Session
from testExam.service.MemberService import MemberService





def guest_menu():
    """
    로그인하지 않은 경우 즉, Session.is_login()이 False일 경우
    현재 화면을 확인하는 사람이 게스트이므로 게스트 메뉴를 호출한다.
    """

    print(dedent("""
      ====== 엠비씨 아카데미 LMS 시스템 ======
      [guest]님 환영합니다.
      1. 회원가입/로그인
      2. 성적관리 (로그인 필요)
      3. 게시판 (로그인 필요)
      4. 상점 (로그인 필요)

      9. LMS시스템 종료
      """))


def main_menu():
    """
    로그인을 했을 경우 즉, if not Session.is_login()이 False가 아닐 경우
    현재 화면을 확인하는 사람이 로그인 한 유저이므로 메인 메뉴를 호출한다.
    """

    print(dedent(f"""
    ====== 엠비씨 아카데미 LMS 시스템 ======
    [{Session.login_member.name}]님 환영합니다.
    1. 회원정보 관리
    2. 성적관리
    3. 게시판
    4. 상점 
    
    9. LMS시스템 종료
    """))







run = True
while run:

    user = MemberService()
    if not Session.is_login():
        guest_menu()

    else:
        main_menu()

    sel = input(">>>")

    if sel == "1": user.run()
    elif sel == "2": pass
    elif sel == "3": pass
    elif sel == "4": pass
    elif sel == "9": run = False
    else:
        print("잘못된 번호를 입력하셨습니다.")
