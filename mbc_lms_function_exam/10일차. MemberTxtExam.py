#회원관리용 더미데이터를 파일(메모장)로 저장하여 관리해보자.

import os
from textwrap import dedent

from pure_eval.utils import ast_name

# 회원관리 curd를 사용자 지정 함수로 만들어 보자.
# c : 회원가입
# r : 회원리스트 관리자인경우 회원암호 변경, 블랙리스트로생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt" #회원 정보를 저장할 메모장 파일명
members = [] #지금은 비어있지만 좀 있다 메모장에 있는 내용을 가져와 리스트 처리함
#members는 2차원 배열로 될 것이다.
#[[                   ],[                  ],[                 ]]
#          0                     1                    2
#  [아이디, 비밀번호, 이름, 권한, 활성화여부]
#    0       1      2    3     4
#                       [아이디, 비밀번호, 이름, 권한, 활성화여부]
#                                            [아이디, 비밀번호, 이름, 권한, 활성화여부]
#
# members[1][3] -> 두번째 회원의 권한을 말함!

#  uid    pw     name  role  active
#[아이디, 비밀번호, 이름, 권한, 활성화여부]
# "kkw"  "1234" "김기원" "admin" "True
#kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임

#파일 처리용 함수들
def save_members():
    """
    members 리스트 내용을 members.txt 파일에 저장
    """

    with open(FILE_NAME, "w", encoding="utf-8") as f: # with는 자동으로 close를 진행하기 때문에 많이 쓴다.
        for member in members: #members는 메모리에 있는 2차원 배열
            data = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"
            f.write(data)



def load_members(): #텍스트파일을 전체 불러와 리스트로 만듬!!! 왜??!?!?!!!? 중간 수정이 안됨
    """
    members.txt 파일을 읽어서 members 리스트에 저장
    """

    #파일이 없으면 새파일 생성 (암기)
    if not os.path.exists(FILE_NAME): #지금 디렉토리에 FILE_NAME이 없으면!!!
        #  os.path 는 현재 위치 -> os는 내부 라이브러리지만 기본적으로 포함되지 않아 import 해야함
        save_members()   #빈 파일이 members.txt로 생성됨
        return

    else:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|") #스플릿을 해야지 리스트가 된다.
                #for문에서 지시문과 받는 변수를 같은 지역변수로 지정하면 큰일난다. 중첩됨. 용도가 다르면 항상 다른 변수로 지정해라
                data[4] = True if data[4] == "True" else False
                members.append(data)



    #있으면 파일을 열어서 한 줄씩 읽기


#load_members() 함수 종료




# 프로그램에서 사용될 함수들
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    uid = input("아이디 :")

    #아이디 중복검사
    for member in members:
        if member[0] == uid: # member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]
            #                    id            pw         name       role       active
            print("이미 존재하는 아이디 입니다.")
            return #함수에서 빠져나간다

    pw = input("비밀번호 :")
    name = input("이름 :")

    #권한 선택
    print("1. admin   2. manager   3. user")
    roleSelect = input("권한 선택 :")

    role = "user" #잘못 클릭해도 user 권한으로 기본값. else를 생략해도 된다. 기본값이 있어서 이걸 따라가면 되기에
    if roleSelect == "1":
        role = "admin"

    elif roleSelect == "2":
        role = "manager"

    #======== 입력 종료 =========
    print(f"아이디 : {uid} 이름 : {name}")
    print(f"권한 : {role}  암호 : {pw}")
    #======== 입력값 확인 =======

    save_True = input("저장하려면 y를 누르세요 :")
    if save_True == "y":
        #w저장 시작!!!
        members.append([uid, pw, name, role, True]) #리스트로 만듬 (.append로 members 리스트에 추가)
        save_members() # 리스트를 파일에 저장
        print("회원가입완료")
        member_login()


    else:
        print("회원가입취소")

#member_add() 함수 종료




    print("member_add 함수를 종료합니다.")


# 회원가입용 함수 종료

def member_login_menu():
    print("로그인 화면으로 진입합니다.")
    global session
    # 로그인에 필요한 기능을 넣음
    if session is not None:
        print("이미 로그인 중입니다.")
        return

    member_login()
    if session is not None:
        return
    print("로그인에 3회 이상 실패할 시 로그인 메뉴를 강제로 종료합니다.")

    member_login()
    if session is not None:
        return

    member_login()
    if session is not None:
        return
    print("로그인에 3회 이상 실패했습니다. 로그인을 강제 종료합니다.")
    return

def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    global session #전역변수로 생성한 값을 가져옴!!! (이미 로그인한 상태?? or None)
    # 로그인에 필요한 기능을 넣음

    print("=======로그인 페이지입니다========")
    id = input("아이디 :")
    pw = input("비밀번호 :")

    for idx, member in enumerate(members) :
        #앞 변수가 0부터 순차적으로 올라가는 숫자
        #뒷 변수가 2차원 리스트가 순차적으로 들어간다.
        if id == member[0]: #키보드로 입력한 id와 리스트에 있는 0번 인덱스 값(리스트의 아이디)이 같으면 True
            if pw == member[1]:
                if member[4]:
                    print(f"{member[2]}님 로그인 성공")
                    print(f"{member[3]}권한으로 로그인 되었습니다.")
                    session = idx #전연변수에 로그인한 주소를 넣음
                    return

                else:
                    print("비활성화 계정입니다.")
                    return

    print("로그인에 실패했습니다.")

    # enumerate() for문은 반복문으로 인덱스를 찾아옴
    #idx -> 1차원 주소
    #member -> 2차원 리스트






    print("member_login 함수를 종료합니다.")


# 회원로그인용 함수 종료

def member_admin():
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드
    member_list()
    modify_user = int(input("정보를 수정할 회원의 번호 :")) - 1
    mod = []
    for i in range(len(members)):
      mod.append(i)

    if modify_user not in mod :
        print("존재하지 않는 회원번호입니다.")
        return






    member_admin_modify_menu()
    select = input(">>>")
    if select == "1":
        ad_id = input("수정할 id :")
        if input(f"{members[modify_user][2]}님의 id를 {ad_id}로 변경을 확정하시겠습니까? (y/n) :") == "y":
            print("id 수정을 완료했습니다.")
            members[modify_user][0] = ad_id
            save_members()

        else:
            print("id 수정을 취소했습니다.")

    elif select == "2":
        ad_pw = input("수정할 pw :")
        if input(f"{members[modify_user][2]}님의 pw를 {ad_pw}로 변경을 확정하시겠습니까? (y/n) :") == "y":
            print("pw 수정을 완료했습니다.")
            members[modify_user][1] = ad_pw
            save_members()

        else:
            print("pw 수정을 취소했습니다.")

    elif select == "3":
        ad_name = input("수정할 이름 :")
        if input(f"{members[modify_user][2]}님의 이름을 {ad_name}로 변경을 확정하시겠습니까? (y/n) :") == "y":
            print("이름 수정을 완료했습니다.")
            members[modify_user][3] = ad_name
            save_members()

        else:
            print("이름 수정을 취소했습니다.")

    elif select == "4":
        ad_role = input("수정할 권한 :")
        if ad_role != "admin" or ad_role != "manager" or ad_role != "user":
            print("올바른 권한을 입력하세요.")
            return

        if input(f"{members[modify_user][2]}님의 권한을 {ad_role}로 변경을 확정하시겠습니까? (y/n) :") == "y":
            print("권한 수정을 완료했습니다.")
            save_members()

    elif select == "5":
        selection = input("1. 휴면계정 전환\n2. 휴면계정 해제\n>>>")
        if selection == "1":
            if members[modify_user][4] is False :
                print("이미 휴면계정 상태입니다.")
                return

            if input(f"정말로 {members[modify_user][2]}님의 계정을 휴면 상태로 전환하시겠습니까? (y/n) :") == "y" :
                print("휴면계정 전환이 완료되었습니다.")
                members[modify_user][4] = False
                save_members()

            else:
                print("휴면계정 전환을 취소했습니다.")

        elif selection == "2":
            if members[modify_user][4] is True:
                print("휴면계정이 아닙니다.")
                return


            if input(f"정말로 {members[modify_user][2]}님의 휴면계정 상태를 해제 하시겠습니까? (y/n) :") == "y":
                print("휴면계정 해제가 완료되었습니다.")
                members[modify_user][4] = True
                save_members()


    # 블랙리스트로 변환 -> active를 False

    # 권한 부여 -> 사용자의 권한roles를 변경 (manage <-> user)

    print("member_admin 함수로 종료합니다.")


# 관리자가 사용자 변경사항 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 session을 None으로 변경
    global session

    if session == None:
        print("로그인이 필요한 서비스입니다.")
        return

    if input("정말 로그아웃 하시겠습니까? (y/n) :") == "y" :
        print("로그인이 완료되었습니다.")
        session = None
        return

    print("member_logout 함수를 종료합니다.")


# 로그아웃 함수를 종료

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자산의 정보를 확인하고 수정한다.
    if session == None:
        print("로그인이 필요한 서비스입니다.")
        return

    if members[session][3] == "admin" :
        member_admin()
        return


    member_modify_menu()
    select = input(">>>")
    if select == "1":
        modify_name = input("변경할 이름 :")

        if input(f"{modify_name}으로 이름 변경을 확정하시겠습니까? (y/n) :") == "y" :
            print("이름 변경이 완료되었습니다.")
            members[session][2] = modify_name
            save_members()

        else:
            print("이름 변경을 취소했습니다.")

    elif select == "2":
        modify_id = input("변경할 id :")

        if input(f"{modify_id}로 id 변경을 확정하시겠습니까? (y/n) :") == "y" :
            print("id 변경이 완료되었습니다.")
            members[session][0] = modify_id
            save_members()

        else:
            print("id 변경을 취소했습니다.")

    elif select == "3":
        modify_pw = input("변경할 pw :")

        if input("변경할 pw :") == "y" :
            print("pw 변경이 완료되었습니다.")
            members[session][1] = modify_pw
            save_members()

        else:
            print("pw 변경을 취소했습니다.")

    else:
        print("올바른 번호를 입력해주세요.")



    print("member_modify 함수를 종료합니다.")


# 회원정보 수정 종료

def member_delete():
    # 회원 탈퇴 또는 회원 유휴등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active=False)
    global session
    if session == None:
        print("로그인이 필요한 서비스입니다.")

    member_delete_menu()
    select = input(">>>")
    if select == "1":
        if input("정말로 회원 탈퇴를 진행하시겠습니까? (y/n) :") == "y" :
            print("회원 탈퇴를 완료했습니다.")
            members.pop(session)
            session = None
            save_members()

    elif select == "2":
        if input("정말로 휴면 계정으로 전환하시겠습니까? (y/n) :") == "y" :
            print("휴면 계정 전환이 완료되었습니다.")
            members[session][4] = False
            session = None
            save_members()

    print("member_delete 함수를 종료합니다.")


# 회원탈퇴 종료

# --------------------- 기능에 대한 함수 생성 끝----------------

def main_menu():
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입    2. 로그인     3. 로그아웃
    4. 회원정보수정      5. 회원탈퇴
    9. 프로그램 종료
    
    """)

# 메인메뉴용 함수 종료

def member_add_menu():  # 회원가입에서 사용할 메뉴
    print(f"""
    ----- 회원권한을 확인하세요.---------
    1. 관리자    2. 팀장    3. 일반사용자 
    
    """)


def member_list():

    for i in range(len(members)):
        print(f"{i+1} | {members[i][2]} | {members[i][0]} | {members[i][1]} | {members[i][3]} | {members[i][4]}")



def member_admin_modify_menu():
    print(dedent(f"""
    ---- 관리자용 회원 정보 수정 메뉴입니다----
    
    1. id   2. pw   3. 이름   4. 권한
    5. 휴면 계정 전환/해제
        
    """))



def member_modify_menu():
    print(dedent(f"""
    ---- 수정 내용 목록 ----

    1. 이름   2. id   3. pw

    """))

def member_delete_menu(): print(dedent(f"""
    -------- 회원 탈퇴 목록 --------
    
    1. 회원 탈퇴   2. 휴면 계정 등록

    """))

# ------------------ 메뉴 함수 끝 ------------------

# 프로그램 시작!!!!

load_members() #프로그램 시작 시 파일을 불러오기!!! -> 1번만! 2차원 배열로 불러옴!
while run:  # 메인 프로그램 실행 코드
    main_menu()  # 위에서 만든 메인 메뉴함수를 실행
    if session is None:
        print("현재 비로그인 상태입니다.")
        print("회원이 아니면 1번을 누르세요!")
    else:
        print(f"{members[session][2]}님 환영합니다.")

    select = input(">>>")  # 키보드로 메뉴 선택
    if select == "1":  # 회원가입 코드
        member_add()  # 회원가입용 함수 호출

    elif select == "2":  # 로그인 메뉴 선택
        member_login_menu()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출

    elif select == "4":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5":  # 회원탈퇴 선택
        member_delete()  # 회원정보 삭제 함수 호출

    elif select == "9":  # 프로그램 종료 선택
        run = False

    else:
        print("잘못 입력하셨습니다.")
# while문 종료