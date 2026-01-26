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
5. 엠비씨 아카데미 성적처리 프로그램
6. 프로그램 종료
"""

menu2 = """
====================
엠비씨 아카데미 성적처리
====================
1. 성적입력
2. 성적보기
3. 성적수정
4. 성적삭제
5. 프로그램 종료
"""


#사용할 리스트 변수를 생성한다.
sns = [1,2]   #사용자 관리번호
ids = ["kkw","lhj"]   #로그인용 아이디
passwords = ["1234","4321"] #로그인용 패스워드
names = ["관리자","임효정"] #사용자명
emails = ["admin@mbc.com","lhj@mbc.com"] #이메일주소
admins = [True, False] #관리자 유무 관지라: True, 일반사용자: False

snss = [] #학번
namess = [] #이름
kors = [] #국어점수
engs = [] #영어점수
mats = [] #수학점수
tots = [] #총점 빈 배열
avgs = [] #평균 빈 배열
korgrades = [] #학점 빈 배열
enggrades = []
matgrades = []


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
                run = False
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










    elif select == "5":
        while True:  # run 변수가 False 처리 될 때까지 반복
            # : 아래는 들여쓰기 4칸 정도 처리
            # 들여쓰기를 진행하면 하위 실행문이다!!!
            print(menu2)  # 콘솔창에 메뉴를 출력
            select = input("1~5번중에서 원하는 메뉴의 번호를 입력해주세요 :")  # select 변수에 숫자(문자열)을 넣는다.
            # 키보드로 입력받는 곳 앞쪽에 출력 메세지
            if select == "1":  # 키보드로 입력한 숫자가 1이면?
                print("학생 성적을 입력합니다.")  # 1일때 처리되는 부분
                sn = input("성적을 입력할 학생의 학번을 입력해주세요 :")
                name = input("성적을 입력할 학생의 이름을 입력해주세요 :")
                kor = input("국어 점수를 입력하세요 :")
                eng = input("영어 점수를 입력하세요 :")
                mat = input("수학 점수를 입력하세요 :")
                tot = int(kor) + int(eng) + int(mat)
                avg = round(tot / 3, 0)
                korgrade = None
                enggrade = None
                matgrade = None

                if int(kor) >= 90:
                    korgrade = "A"
                elif int(kor) >= 80:
                    korgrade = "B"
                elif int(kor) >= 70:
                    korgrade = "C"
                else:
                    korgrade = "F"

                if int(eng) >= 90:
                    enggrade = "A"
                elif int(eng) >= 80:
                    enggrade = "B"
                elif int(eng) >= 70:
                    enggrade = "C"
                else:
                    enggrade = "F"

                if int(mat) >= 90:
                    matgrade = "A"
                elif int(mat) >= 80:
                    matgrade = "B"
                elif int(mat) >= 70:
                    matgrade = "C"
                else:
                    matgrade = "F"

                print("입력한 정보를 확인합니다.")
                print(f"""
학번 : {sn}
이름 : {name}
국어 : {kor} 등급 : {korgrade}
영어 : {eng} 등급 : {enggrade}
수학 : {mat} 등급 : {matgrade}
총점 : {tot}
평균 : {avg}
""")

                if input("저장하려면 y를 입력해주세요 :") == "y":  # 저장시 y 입력
                    snss.append(sn)
                    namess.append(name)
                    kors.append(kor)
                    engs.append(eng)
                    mats.append(mat)  # 변수뒤에 s는 배열(리스트)라고 생각
                    # 변수.append() 리스트 뒤에 값이 추가된다.
                    tots.append(tot)
                    avgs.append(avg)
                    korgrades.append(korgrade)
                    enggrades.append(enggrade)
                    matgrades.append(matgrade)
                    # 미션 평균이 : 90 이상이면 A, 80 이상이면 B, 70 이상이면 C, 나머지는 F = grades

                    print("저장을 완료했습니다.")


                else:
                    print("저장을 취소합니다.\n처음부터 다시 입력하세요.")








            elif select == "2":  # 키보드로 입력한 숫자가 2이면?
                print("학생의 성적을 출력합니다.")  # 2일때 처리되는 부분
                selc = input("전체 학생 성적 보기는 1번, 개인 학생 성적 보기는 2번을 입력해주세요 :")
                if selc == "1":
                    print("전체 학생 성적을 출력합니다.")
                    for i in range(len(snss)):  # 리스트의 처음부터 끝까지 반복용
                        #          len(ses) -> snss 리스트의 길이를 가져옴 -> 5
                        #    range(5) -> 0~5까지 증가
                        # i in 5 -> i값에 0 반복 1 반복 2 반복 3 반복 4 반복 5 끝!
                        # 결론 : i값이 인덱스로 사용함
                        # tot = kors[i] + engs[i] + mats[i] #주의, 애초에 비어있는 주소는 인지하지 못하니 tots[i]는 사용하면 안된다.
                        # avg = tot/3
                        print(f"""
===========================================
학번 : {snss[i]} 이름 : {namess[i]}
국어 점수: {kors[i]:>3}점 등급 : {korgrades[i]}
영어 점수: {engs[i]:>3}점 등급 : {enggrades[i]}
수학 점수: {mats[i]:>3}점 등급 : {matgrades[i]}
총점: {tots[i]:>3}점  평균: {avgs[i]:2.0f}점
===========================================""")




                elif selc == "2":
                    print("개인 학생 성적을 출력합니다.")
                    sn = input("학번을 입력해주세요 :")
                    name = input("이름을 입력해주세요 :")
                    if sn in snss:
                        idx = snss.index(sn)
                        if name == namess[idx]:
                            print("해당 학생의 성적을 출력합니다.")
                            print(f"""
===========================================
학번 : {snss[idx]:}
이름 : {namess[idx]}

국어 점수 : {kors[idx]:>3}점 등급 : {korgrades[idx]}
영어 점수 : {engs[idx]:>3}점 등급 : {enggrades[idx]}
수학 점수 : {mats[idx]:>3}점 등급 : {matgrades[idx]}
총점     : {tots[idx]:>3}점
평균     :  {avgs[idx]:2.0f}점
===========================================""")

                        else:
                            print("학생의 이름이 잘못 되었습니다.")
                    else:
                        print("학번이 잘못 되었습니다.")









            elif select == "3":  # 키보드로 입력한 숫자가 3이면?
                print("학생 성적을 수정합니다.")

                # 등록한 학생의 점수를 가져온다.
                # 학번을 이용하여 학생을 찾는다.
                sn = input("수정할 학번 :")
                if sn in snss:  # snss학번이 들어있는 리스트 in 안에 있는지 확인
                    print("학번이 있습니다.")
                    idx = snss.index(sn)  # 찾은 학번의 주소를 가져옴
                    print(f"""
이름 : {namess[idx]}
국어 : {kors[idx]}점 등급 : {korgrades[idx]}
영어 : {engs[idx]}점 등급 : {enggrades[idx]}
수학 : {mats[idx]}점 등급 : {matgrades[idx]}
""")
                    kor = input("수정할 국어 점수 :")
                    eng = input("수정할 영어 점수 :")
                    mat = input("수정할 수학 점수 :")
                    # 미션 수정된 내용으로 총점, 평균을 다시 등록하기
                    korgrade = None
                    enggrade = None
                    matgrade = None
                    tot = int(kor) + int(eng) + int(mat)
                    avg = round(tot / 3, 0)

                    if int(kor) >= 90:
                        korgrade = "A"
                    elif int(kor) >= 80:
                        korgrade = "B"
                    elif int(kor) >= 70:
                        korgrade = "C"
                    else:
                        korgrade = "F"

                    if int(eng) >= 90:
                        enggrade = "A"
                    elif int(eng) >= 80:
                        enggrade = "B"
                    elif int(eng) >= 70:
                        enggrade = "C"
                    else:
                        enggrade = "F"

                    if int(mat) >= 90:
                        matgrade = "A"
                    elif int(mat) >= 80:
                        matgrade = "B"
                    elif int(mat) >= 70:
                        matgrade = "C"
                    else:
                        matgrade = "F"

                    print(f"""
수정된 학생 성적입니다.
이름 : {namess[idx]}
국어 : {kor} 등급 : {korgrade}
영어 : {eng} 등급 : {enggrade}
수학 : {mat} 등급 : {matgrade}
총점 : {tot}
평균 : {avg}
""")

                    if input("정말로 수정하시겠습니까? (y/n) :") == "y":
                        kors[idx] = kor
                        engs[idx] = eng
                        mats[idx] = mat
                        tots[idx] = tot
                        avgs[idx] = avg
                        korgrades[idx] = korgrade
                        enggrades[idx] = enggrade
                        matgrades[idx] = matgrade
                        print("수정을 완료했습니다.")
                    else:
                        print("수정을 취소합니다.")
                        print("처음으로 돌아갑니다.")
                else:
                    print("학번이 없습니다.")
                    print("처음으로 돌아갑니다.")

                # 등록된 학생의 점수를 수정한다.

                # 수정된 값을 기준으로 총점과 평균과 등급을 다시 등록한다.


            elif select == "4":  # 키보드로 입력한 숫자가 4이면?
                print("학생 성적을 삭제합니다.")
                sn = input("삭제할 학번 :")

                if sn in snss:
                    idx = snss.index(sn)
                    print(f"{namess[idx]} 학생의 정보를 삭제합니다.")

                    if input("정말로 삭제할까요? (y/n) :") == "y":
                        snss.pop(idx)
                        namess.pop(idx)
                        kors.pop(idx)
                        engs.pop(idx)
                        mats.pop(idx)
                        tots.pop(idx)
                        avgs.pop(idx)
                        print("삭제가 완료되었습니다.")

                    else:
                        print("삭제가 취소되었습니다.")
                else:
                    print("잘못된 학번입니다.")


            elif select == "5":  # 키보드로 입력한 숫자가 5이면?
                print("프로그램을 종료합니다.")
                break


            else:  # 1~5까지 값 이외의 문자가 들어오면 처리용
                print("1~5값만 허용합니다.")



    elif select == "6" :
        print("회원가입프로그램이 종료됩니다.")
        run = False

    else:
        print("1~5사이 값을 입력하세요!!!!")