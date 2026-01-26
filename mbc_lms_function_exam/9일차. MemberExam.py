#회원관리 CRUD를 사용자 지정 함수로 만들어 보자.
#C : 회원가입
#R : 회원 리스트 (관리자)회원암호 변경, 블랙리스트 생성, 상위 등급 권한 부여
#R : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
#U : 회원정보 수정
#D : 회원탈퇴, 회원비활성화
from textwrap import dedent

#프로그램에서 사용될 변수들
#전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
#지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True #while에서 전체적으로 사용되는 변수(프로그램 구동)
session = None #로그인 상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용

#프로그램에서 사용될 리스트들(더미 데이터)
#sns = [1]   #sns는 삭제되고 다시 추가되거나 하는 경우마다 변동됨. 즉, 유일한 수가 아님.
#              ids :   0pws   1names  2roles 3active 4block   #비밀번호, 이름, 등급, 계정 상태, 블랙리스트 여부
user_infor = {"kkw" : ["1234","김기원","admin",True,False],
              "lhj" : ["5678","임효정","manager",True,False]}
role_passwords = {"admin" : "1234", "manager" : "2345"}
trash = {}
#차후에는 파일처리로 변환 할 예정

##=====================================프로그램에서 사용될 함수들============================================================

def member_add():
    #회원가입용 함수
    #print("member_add 함수로 진입합니다.")
    while True: #아예 처음으로 튕겨져나가게 하지 않기 위한 while문
        print("======회원가입 페이지입니다======\n")
        new_id = input("생성할 아이디 :")
        if new_id in user_infor.keys(): #딕셔너리기 때문에 .keys()함수로 key들을 가져온다
                                        #그리고 가져온 key들과 하나하나 new_id와 대조해서 참거짓을 가린다.
            print("이미 존재하는 아이디입니다.") #참일때 이미 존재하는 아이디이므로 생성되어선 안된다.
            continue

        else:
            new_password = input("생성할 비밀번호 :")
            new_name = input("가입자 이름 :")
            role = "user" #관리자만 등급을 변경할 수 있도록 처음 생성되는 등급은 반드시 일반 회원으로

            if input(dedent(f"""
            아래의 내용으로 회원가입을 완료하시겠습니까?
            
            이름 : {new_name}
            아이디 : {new_id}
            비밀번호 : {new_password}
            권한 : {role}
            
            (y/n)
            >>>""")) == "y":
                user_infor[new_id] = [new_password, new_name, role, True, False]
                #미리 설정해둔 순서대로 리스트가 딕셔너리로 들어간다.
                #key(이때는 new_id) : [위에 적은 리스트 내용들이 순서대로 들어간다]
                print("회원가입을 완료했습니다.")
                member_login()#member_login() 로그인 화면으로 바로 넘어갈 수 있다.
                return


            else:
                print("회원가입을 취소합니다.")
                break



        #회원가입에 필요한 기능을 넣음

#-----------------------------------------------------------------------------------------------------------------------

def member_login():
    #가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    #print("member_login 함수로 진입합니다.")
    # 로그인에 필요한 기능을 넣음
    global session  # 전역 변수를 지정하게 할 수 있도록 하겠다. #로그인을 하면 session의 값을 바꿔야하므로.
    if session is not None : #session에 이미 값이 있으면??
    # is not None 싱글톤이라는 객체가 있는지 비교하는 용
    # != 은 is not과 같은 의미이나, 숫자 비교형 이퀄이나는 값으로 사용
        print("이미 로그인한 상태입니다.")
        print(f"로그인한 사용자는 {user_infor.get(session)[1]}입니다.")
                              #딕셔너리.get(로그인한 유저의 key)
                                    #.get()함수는 그 키의 벨류를 불러온다.
                                    #이 때는 뒤에 리스트 인덱스를 넣었으니 그 위치의 값
        return

    else: # if문이 False 일 때
        wall = 3
        while True:
            print("=============로그인 페이지입니다=============\n")
            user_id = input("아이디 :")
            if user_id in user_infor.keys():
                user_pw = input("비밀번호 :")
                if user_pw == user_infor[user_id][0]:
                    if user_infor[user_id][3] == False or user_infor[user_id][4] == True:
                        # 로그인 한 유저가 휴면계정인지, 블랙당한 상태인지 판별하는 용도
                        print("비활성화 또는 차단된 계정입니다.")
                        continue

                    else:
                        session = user_id #글로벌 영역의 session값(로그인한 사용자의 주소)이 들어간다.
                        print(dedent(f"""
                        ====================================                                     
                        {user_infor[session][1]}님 환영합니다.
                        {user_infor[session][2]}
                        ====================================
                        """))
                        return

                else:
                    print("비밀번호가 틀렸습니다.")
                    wall -= 1 #틀릴 시 wall 즉, 남은 횟수가 1회 까인다
                    if wall == 2:
                        print("아이디 또는 비밀번호를 3회 이상 틀릴 시 강제로 로그인 페이지를 종료합니다.")
                        continue
                    elif wall == 0:
                        print("아이디 또는 비밀번호를 3회 이상 틀렸습니다. 로그인 페이지를 종료합니다.")
                        return #3회 전부 틀리면 강제로 돌아간다.
                    else:
                        continue
            else:
                print("아이디가 틀렸습니다.")
                wall -= 1 #틀릴 시 wall 즉, 남은 횟수가 1회 까인다
                if wall == 2:
                    print("아이디 또는 비밀번호를 3회 이상 틀릴 시 강제로 로그인 페이지를 종료합니다.")
                    continue
                elif wall == 0:
                    print("아이디 또는 비밀번호를 3회 이상 틀렸습니다. 로그인 페이지를 종료합니다.")
                    return #3회 전부 틀리면 강제로 돌아간다.
                else:
                    continue


#-----------------------------------------------------------------------------------------------------------------------

def member_list():
    #관리자의 수정 메뉴에서 사용할 전체 맴버 리스트 확인용
    #print("member_list 함수로 진입합니다.")
    for i in user_infor.keys(): #딕셔너리.keys()함수는 딕셔너리에 존재하는 모든 key목록 리스트를 생성하는 것이다.
                                #생성된 리스트는 차례대로 i에 대입된다.
        if user_infor[i][3] == True: #i키의 벨류 리스트의 3번 인덱스의 값이 True 일 때
            active = "활성"
        else:
            active = "비활성"


        if user_infor[i][4] == False: #i키의 벨류 리스트의 4번 인덱스의 값이 False 일 때
            block = "X"
        else:
            block = "O"

        print(f"이름:{user_infor[i][1]} | id:{i} pw:{user_infor[i][0]} | 권한:{user_infor[i][2]} | 상태:{active} | 블랙:{block}")

#-----------------------------------------------------------------------------------------------------------------------

def member_admin():
    #관리자가 로그인 했을 경우 할 수 있는 기능을 작성
    #print("member_admin 함수로 진입합니다.")
    #다른 사용자 암호 변경 코드
    #블랙 리스트로 변환 -> block을 True처리
    #권한 부여 -> 사용자의 roles를 변경 (manage <-> user)
    #while True: # 다시 되돌아올 경우, 완전 초기 화면으로 가면 불편하기에 while을 함수 내에서 돌린다.
    member_list() # 전체 회원 리스트 함수 불러오기
    select = input("정보를 변경할 회원의 id :")
    if select in user_infor.keys(): # 위 인풋 사항이 id를 담당하는 딕셔너리의 keys 리스트에 있을 시
        member_admin_menu() # 관리자 설정 메뉴 함수 불러오기
        selection = input(">>>")
        if selection == "1" :
            admin_name = input("변경할 이름 :")
            if input(f"{user_infor[select][1]}님의 이름을 {admin_name}으로 변경하시겠습니까?\n(y/n)\n") == "y":
                user_infor[select][1] = admin_name #딕셔너리[키][벨류 리스트의 인덱스] = 입력한 input 변수
                                                   #즉, 이 경우엔 이름의 자리
                print("이름 변경이 완료되었습니다.")
                #break

            else:
                print("이름 변경을 취소했습니다.")
                #break

        elif selection == "2" :
            admin_id = input("변경할 id :")
            if admin_id in user_infor.keys(): # id는 중복되면 안되므로 중복방지문구
                print("이미 존재하는 id입니다.")
                #continue

            else:
                if input(f"{user_infor[select][1]}님의 id를 {admin_id}로 변경하시겠습니까?\n(y/n)\n") == "y":
                    user_infor[admin_id] = user_infor[select]
                    # key가 id이므로 id를 변경하고 싶으면 새로운 id(이 경우엔 admin_id)에 기존 벨류 리스트를 전부 넣어줘야한다.
                    del user_infor[select] # 기존에 남아있는 계정 정보는 삭제(key를 기준으로)
                    print("id 변경이 완료되었습니다.")
                    #break

                else:
                    print("id 변경을 취소했습니다.")
                    #break

        elif selection == "3" :
            admin_pw = input("변경할 pw :")
            if input(f"{user_infor[select][1]}님의 pw를 {admin_pw}로 변경하시겠습니까?\n(y/n)\n") == "y":
                user_infor[select][0] = admin_pw
                print("pw 변경을 완료했습니다.")
                #break

            else:
                print("pw 변경을 취소했습니다.")
                #break

        elif selection == "4" :
            admin_role = input("변경할 권한 :")
            if admin_role == "admin" or admin_role == "manager1" or admin_role == "user":
                if input(f"{user_infor[select][1]}님의 권한을 {admin_role}로 변경하시겠습니까?\n(y/n)\n") == "y":
                    user_infor[select][2] = admin_role
                    print("권한 변경을 완료했습니다.")
                    #break

                else:
                    print("권한 변경을 취소했습니다.")
                    #break

            else:
                print("올바른 권한명이 아닙니다.")
                #continue

        elif selection == "5" :
            if input(f"{user_infor[select][1]}님을 블랙하시겠습니까?\n(y/n)\n") == "y":
                user_infor[select][4] = True
                print(f"{user_infor[select][1]}님을 블랙했습니다.")
                #break

            else:
                print(f"{user_infor[select][1]}님의 블랙을 취소했습니다.")
                #break

        elif selection == "6" :
            if input(f"{user_infor[select][1]}님의 휴면 계정을 해제하시겠습니까?\n(y/n)\n") == "y":
                user_infor[select][3] = True
                print(f"{user_infor[select][1]}님의 휴면 계정을 해제했습니다.")
                #break

            else:
                print(f"{user_infor[select][1]}님의 휴면 계정 해제를 취소했습니다.")
                #break

        elif selection == "9" :
            print("상위 메뉴로 돌아갑니다.")
            return


        else:
            print("올바른 번호를 입력해주세요.")
            #continue

    else:
        print("올바른 id가 아닙니다.")
        #return

#-----------------------------------------------------------------------------------------------------------------------

def member_logout():
    #회원 로그아웃으로 상태 변경 -> session의 값을 None으로 변경
    #print("member_logout 함수에 진입합니다.")
    #로그인 상태인지를 확인하고 session을 Non으로 변경
    global session
    if session is not None :
        if input("정말로 로그아웃 하시겠습니까? (y/n) :") == "y":
            session = None
            print("로그아웃을 완료했습니다.")

        else:
            print("로그아웃을 취소했습니다.")

    else:
        print("로그인이 필요한 서비스입니다.")

#-----------------------------------------------------------------------------------------------------------------------

def member_modify():
    #회원정보 수정
    global session
    #print("member_modify 함수로 진입합니다.")
    if session is not None :

        if user_infor[session][2] == "admin":
            member_admin()
            return



        while True:
            print("로그인 된 회원의 정보를 수정합니다.")
            member_modify_menu()
            select = input(">>>")
            if select == "1":
                modify_name = input("변경할 이름 :")
                if input(f"해당 이름으로 변경을 확정하시겠습니까?\n{modify_name}\n(y/n)\n") == "y":
                    user_infor[session][1] = modify_name
                    print(f"이름 변경이 완료되었습니다.\n변경된 이름 = {user_infor[session][1]}입니다.")
                    break

                else:
                    print("이름 변경을 취소했습니다.")
                    break

            elif select == "2":
                modify_id = input("변경할 id :")
                if modify_id in user_infor.keys():
                    print("이미 존재하는 id입니다.")
                    continue

                if input(f"해당 id로 변경을 확정하시겠습니까?\n{modify_id}\n(y/n)\n") == "y":
                    user_infor[modify_id] = user_infor[session]
                    print(f"id 변경이 완료되었습니다.\n변경된 id = {modify_id}입니다.")
                    del user_infor[session]
                    session = modify_id
                    break

                else:
                    print("id 변경을 취소했습니다.")
                    break

            elif select == "3":
                modify_pw = input("변경할 pw :")
                if input(f"해당 pw로 변경을 확정하시겠습니까?\n 변경된 pw = {modify_pw}\n(y/n)\n") == "y":
                    user_infor[session][0] = modify_pw
                    print(f"pw 변경이 완료되었습니다.\n변경된 pw = {user_infor[session][0]}입니다.")
                    break

                else:
                    print("pw 변경을 취소했습니다.")
                    break

            elif select == "9":
                print("상위 메뉴로 돌아갑니다.")
                return

            else:
                print("올바른 숫자를 입력해주세요.")


    else:
        print("로그인이 필요한 서비스입니다.")
        return


    #로그인 상태인지를 확인하고 자신의 정보를 확인하고 수정한다.

#-----------------------------------------------------------------------------------------------------------------------

def member_delete():
    #회원 탈퇴 또는 회원 유휴(비활성)등 처리
    #print("member_delete 함수로 진입합니다.")
    #로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active = False).
    while True:
        global trash
        global session
        if session is not None :
            select = input("==회원탈퇴 및 휴면계정 전환==\n\n1. 회원탈퇴\n2. 휴면계정 전환\n9. 상위 메뉴로 가기\n>>>")
            if select == "1":
                if input(dedent(f"""
                이름 = {user_infor[session][1]}
                id = {session}
                pw = {user_infor[session][0]}
                권한 = {user_infor[session][1]}
                
                정말 회원탈퇴를 하시겠습니까?
                (y/n)
                >>>""")) == "y":
                    trash = user_infor.pop(session)
                    print("회원 탈퇴를 완료했습니다.")
                    session = None
                    break
                else:
                    print("회원 탈퇴를 취소했습니다.")
                    break

            elif select == "2":
                if input(dedent(f"""
                이름 = {user_infor[session][1]}
                id = {session}
                pw = {user_infor[session][0]}
                권한 = {user_infor[session][1]}
                
                정말 휴면계정으로 전환 하시겠습니까?
                (y/n)
                >>>""")) == "y":
                    user_infor[session][3] = False
                    print("휴면 계정으로 전환했습니다.")
                    session = None
                    break
                else:
                    print("휴면 계정으로 전환을 취소했습니다.")
                    break

            elif select == "9":
                print("상위 메뉴로 돌아갑니다.")
                break

            else:
                print("올바른 번호를 입력해주세요.")


        else:
            print("로그인이 필요한 서비스입니다.")
            break


#==========================================##메뉴에 대한 함수##============================================================

##메뉴에 대한 함수##

def main_menu():
    print(dedent(f"""
    ====엠비씨 아카데미 회원관리 프로그램입니다====
    
    1. 회원가입   2. 로그인   3. 로그아웃
    4. 회원정보 수정   5. 회원탈퇴
    
    9. 프로그램 종료
    """))

def member_modify_menu():
    print(dedent(f"""
    ------- 변경할 정보를 선택하세요 --------
    
    1. 이름   2. id   3. pw
    
    9. 상위 메뉴로
    """))

def member_admin_menu():
    print(dedent(f"""
    ------- 변경할 정보를 선택하세요 --------
    
    1. 이름   2. id   3. pw   4.등급
    
    5. 블랙리스트 추가   6. 휴면계정 해제
    
    9. 상위 메뉴로
    """))

#=======================================================================================================================

#프로그램 시작!

while run:
    main_menu() #위에서 만든 메인 메뉴 함수를 호출
    select = input(">>>") #키보드로 메뉴 선택
    if select == "1": #회원가입 코드
        member_add()

    elif select == "2": #로그인 코드
        member_login()

    elif select == "3": #로그아웃 코드
        member_logout()

    elif select == "4": #회원 정보 수정 코드
        member_modify()

    elif select == "5": #회원 탈퇴 코드
        member_delete()

    elif select == "9": #프로그램 종료
        print("프로그램을 종료합니다.")
        run = False # while문 종료

    else: #메뉴로 지정된 숫자가 아닌 모든 것을 입력 시
        print("지정된 숫자를 입력해주세요.")





