#회원관리용 코드를 만든다.
#c -> 회원추가
#r -> 관리자일경우 (전체회원보기). 일반회원(로그인)
#u -> 관리자일경우 (회원차단, 암호변경문의), 일반회원(내정보수정, 암호변경)
#d -> 회원 탈퇴

#메뉴구현
run = True #프로그램 동작중을 관리하는 변수
login_user = None #유저 고유번호 증정용 null변수
menu = """
==========================
mbc 아카데미 회원 관리 프로그램
==========================
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보수정
5. 프로그램 종료
"""

#사용할 리스트 변수를 생성한다.
sns = [1,2]   #사용자 관리번호
ids = ["kkw","lhj"]   #로그인용 아이디
passwords = ["1234","4321"] #로그인용 패스워드
names = ["관리자","임효정"] #사용자명
emails = ["admin@mbc.com","lhj@mbc.com"] #이메일주소
admins = [True, False] #관리자 유무 관지라: True, 일반사용자: False


while run:
    print(menu)
    select = input("1~5숫자를 입력하세요 : ")
    if select == "1":
        print("회원가입 메뉴에 진입하였습니다.")
        sn = input("사번을 임력하세요 :")
        if int(sn) in sns:
            print("이미 존재하는 사번입니다. 다시 입력해주세요")
            continue


        id = input("아이디를 입력하세요 :")
        pw = input("암호를 입력하세요 :")
        name = input("이름을 입력하세요 :")
        email = input("이메일 주소를 입력하세요 :")
        admin = False

        print("입력된 값을 확인하시고 y를 누르면 가입됩니다.")
        print("이름 :" + name)
        print("id :" + id)
        print("pw :" + pw)
        if input("y/n") == "y":
            sns.append(sn)
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(admin)
            print("입력이 완료되었습니다.")
        else:
            print("처음부터 다시 진행하세요!!!")

    elif select == "2":
        print("로그인 메뉴에 진입하였습니다.")
        wall = 3
        while True:
            id = input("아이디 :")
            pw = input("비밀번호 :")
            if id in ids :  #입력한 아이디 기반 인덱스 번호 지정 및 검증 (66라인까지)
                idx = ids.index(id) #이게 몇번째인지 알면 비번, 사용자 등등 같은 라인으로 전부 알 수 있다. 한 라인으로 오도록 만들었으니까.
                if passwords[idx] == pw:
                    login_user = idx
                    print(f"{names[idx]}님 로그인 성공")
                    if admins[idx] : # == True :  <-생략
                        print("관리자 계정입니다.")
                    else:
                        print("일반 회원 계정입니다.")
                else:
                    print("비밀번호가 틀렸습니다.")
                    wall = wall - 1
            else:
                print("존재하지 않는 아이디입니다.")
                wall = wall - 1

            if wall == 2:
                print("로그인에 3번 실패하면 강제로 프로그램이 종료됩니다.")

            if wall == 0:
                print("로그인을 3번 실패했습니다. 프로그램을 종료합니다.")
                break




    elif select == "3":

        if login_user is None :
            print("로그인 후 이용 가능합니다.")
            continue


        #관리자
        if admins[login_user] :
            print("\n[전체 회원 목록]")
            for i in range(len(ids)) :  #range의 기능
                print(f"{i+1}. {names[i]} / {ids[i]} / {emails[i]} / 관리자 : {admins[i]}")
        else:
            #일반 회원 정보
            print(f"""
            회원님의 정보는 다음과 같습니다.
            사용자 번호 : {sns[login_user]}
            아이디 : {ids[login_user]}
            비밀번호 : {passwords[login_user]}
            이름 : {names[login_user]}
            이메일 : {emails[login_user]}
            계정 등급 : {admins[login_user]}
            """)



    elif select == "4":
        if login_user is None :
            print("로그인 후 이용 가능합니다.")
            continue



        print("내 정보 수정 페이지입니다.")
        rep = input("""
변경하실 내용을 선택해 숫자를 입력해주세요.
1. 사용자 번호 
2. 아이디 
3. 비밀번호 
4. 이름 
5. 이메일 
>>>""")
        if rep == "1" :
            print("사용자 번호 변경을 선택하셨습니다.")
            sn = input("숫자만 사용해서 변경할 사용자 번호를 입력해주세요 :")
            if not sn.isdigit() :
                print("잘못된 입력입니다. 다시 실행해주세요.")
                continue


            elif int(sn) in sns :
                print("이미 존재하는 사용자 번호입니다.")
                continue


            else:
                sns[login_user] = sn
                print("사용자 번호가 변경되었습니다." + sns[login_user])



        elif rep == "2" :
            print("아이디 변경을 선택하셨습니다.")
            id = input("변경할 아이디를 입력해주세요 :")
            if id in ids :
                print("이미 존재하는 아이디입니다.")
            else:
                ids[login_user] = id
                print("아이디가 변경되었습니다." + ids[login_user])

        elif rep == "3" :
            print("비밀번호 변경을 선택하셨습니다.")
            pw = input("숫자만을 사용하여 4자리를 넘도록 변경할 비밀번호를 입력해주세요 :")
            if len(pw) >= 4 and pw.isdigit() :
                passwords[login_user] = pw
                print("비밀번호 변경이 완료되었습니다." + passwords[login_user])
            else:
                print("비밀번호가 적절하지 않습니다. 다시 실행해주세요.")
                continue

        elif rep == "4" :
            print("이름 변경을 선택하셨습니다 :")
            names[login_user] = input("변경할 이름을 입력해주세요.")
            print("이름 변경이 완료되었습니다." + names[login_user])


        elif rep == "5" :
            print("이메일 변경을 선택했습니다 :")
            emails[login_user] = input("변경할 이메일을 선택해주세요.")
            print("이메일 변경이 완료되었습니다." + emails[login_user])






    elif select == "5" :
        print("회원가입프로그램이 종료됩니다.")
        run = False
    else:
        print("1~5사이 값을 입력하세요!!!!")