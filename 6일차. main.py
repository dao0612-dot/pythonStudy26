#대부분 프로그래밍에서 1번이 되는(start) 파일을 main으로 만듬
from textwrap import dedent

#목표 : MBC아카데미 LMS 프로그램을 만들어 보자.
#회원관리 : 시스템 담당자, 교수, 행정, 학생, 손님, 학부모
#성적관리 : 교수가 성적 등록,수정,
#          행정 담당자가 학기마다 백업(이전->삭제)
#          학생은 개인성적일람, 성적출력
#          손님은 학교소개페이지 열람
#          학부모는 자녀학사관리
#게시판 : 회원제, 비회원제, 문의사항, Q/A

#필요한 변수
run = True #메인 메뉴용 while
#subrun = True #보조 메뉴용 while
session = None #로그인한 사용자의 인덱스를 기억

# 필요한 리스트
#회원에 대한 리스트
sns = [1] #회원에 대한 리스트 (중복x)(숫자)
ids = ["kkw"] #아이디에 대한 리스트
names = ["김기원"] #이름에 대한 리스트
passwords = ["1234"] #비밀번호에 대한 리스트
gropes = ["professor"] #회원등급
gropePasswords = {'1234' : 'admin','2345' : 'stu','3456' : "parents",'4567' : "office",'5678' : 'professor'}
#admin (관리자), stu (학생), guest (손님) parents (학부모), office (행정), professor (교수)....
backups = {}

#성적에 대한 리스트
pythonScores = {} #파이썬 점수들
dataBaseScores = {} #데이터베이스 점수들
wwwScores = {} #프론트 점수 들
totalScores = {} #총점 들
avgScores = {} #평균 들
pythonGradeScores = {} #파이썬 등급
dataBaseGradeScores = {} #데이터베이스 등급
wwwGradeScores = {} #프론트 등급
stuIdxs = [1] #학생의 인덱스 (학번) <-> 회원의 sns

#게시판에 대한 리스트
board_nos = [] #게시물의 번호
board_titles = [] #게시물의 번호
board_contents = [] #게시물의 내용
board_writers = [] #게시물의 작성자 <-> 회원의 sns


#메뉴구성
mainMenu = """
==================================
엠비씨 아카데미 LMS에 오신걸 환영합니다.
==================================

1. 로그인(회원가입)
2. 성적관리
3. 게시판
4. 관리자 메뉴
9. 프로그램 종료

"""

memberMenu = """
----------------------------------
회원관리 메뉴입니다.

1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴
5. 로그아웃

9. 회원관리 메뉴 종료

"""

scoreMenu = """
----------------------------------
성적관리 메뉴입니다.

1. 성적 입력
2. 성적 보기
3. 성적 수정
4. 성적 백업

9. 성적관리 메뉴 종료

"""

boardMenu = """
----------------------------------
회원제 게시판입니다.

1.
2.
3.
4.
5.

9.

"""

adminMenu = """
===================================
관리자 메뉴입니다.
===================================

1. 






"""

#주 실행문 구현
while run:
    print(mainMenu) #메인메뉴 출력용
    select = input("원하시는 메뉴의 번호를 입력해주세요 :") #사용자가 주메뉴선택 값을 select 넣는다.
    if select == "1":
        print("로그인(회원가입) 메뉴로 진입합니다.")

        subRun = True
        while subRun: #부메뉴 반복용
            print(memberMenu) #회원관리 메뉴가 출력
            subSelect = input("원하시는 메뉴의 번호를 입력해주세요 :") #회원 부메뉴 선택값을 subSelect에 넣음
            if subSelect == "1":
                print("로그인 메뉴로 진입합니다.")
                id = input("아이디를 입력하세요 :")
                if id in ids :
                    idx = ids.index(id) #입력한 id의 인덱스 주소
                    password = input("비밀번호를 입력해주세요 :")
                    if password == passwords[idx] :

                        if session is None: #중복 로그인 방지용
                            session = idx
                            print("로그인에 성공하셨습니다.")

                        else:
                            print("이미 다른 계정으로 로그인중입니다. 먼저 로그아웃을 해주세요.")

                    else:
                        print("비밀번호가 틀렸습니다.")

                else:
                    print("아이디가 틀렸습니다.")





            elif subSelect == "2":
                print("회원가입 메뉴로 진입합니다.")
                name = input("이름을 입력하세요 :")
                id = input("아이디를 입력하세요 :")
                password = input("비밀번호를 입력하세요 :")
                gropePw = input("그룹 비밀번호를 입력하세요 :")
                if gropePw in gropePasswords: #딕셔너리 활용 (위에 gropePasswords 참조)
                    grope = gropePasswords.get(gropePw)

                else:
                    grope = "guest"




                sn = len(sns) + 1
                if input(dedent(f"""\
                이름 = {name}
                학번 = {sn}
                아이디 = {id}
                비밀번호 = {password}
                소속 = {grope}
                
                해당 내용으로 확정하시겠습니까?
                (y/n)
                >>>""")) == "y" :
                    print("회원가입이 완료되었습니다.")
                    sns.append(sn)
                    stuIdxs.append(sn)
                    ids.append(id)
                    passwords.append(password)
                    names.append(name)
                    gropes.append(grope)

                    #print(sns)
                    #print(stuIdxs)


                else:
                    print("회원가입을 취소합니다.")





            elif subSelect == "3":
                if session is None: #로그인을 해야 세션이 바뀐다. 즉, 로그인을 안해서 None 상태면 if문 실행
                    print("로그인이 필요한 서비스입니다.")

                else:
                    print("회원 수정 메뉴로 진입합니다.")
                    id = input("수정할 계정의 아이디를 입력해주세요 :")
                    if id in ids :
                        idx = ids.index(id)
                        password = input("수정할 계정의 비밀번호를 입력해주세요 :")
                        if password == passwords[idx] :
                            print(dedent(f"""\
                            ---------------------
                            수정할 내용을 선택해주세요
                            
                            1. 이름
                            2. 아이디
                            3. 비밀번호
                            4. 회원등급
                            """))
                            select = input(">>>")
                            if select == "1":
                                name = input("수정할 이름을 입력해주세요 :")
                                if input(dedent(f"""\
                                {name}
                                해당 내용으로 확정하시겠습니까?
                                (y/n)
                                >>>""")) == "y" :
                                    names[idx] = name
                                    print("이름 수정을 완료했습니다.")
                                else:
                                    print("수정을 취소했습니다.")

                            elif select == "2":
                                id = input("수정할 아이디를 입력해주세요 :")
                                if input(dedent(f"""\
                                {id}
                                해당 내용으로 확정하시겠습니까?
                                (y/n)
                                >>>""")) == "y":
                                    ids[idx] = id
                                    print("아이디 수정을 완료했습니다.")
                                else:
                                    print("수정을 취소했습니다.")

                            elif select == "3":
                                password = input("수정할 비밀번호를 입력해주세요 :")
                                if input(dedent(f"""\
                                {password}
                                해당 내용으로 확정하시겠습니까?
                                (y/n)
                                >>>""")) == "y":
                                    passwords[idx] = password
                                    print("비밀번호 수정을 완료했습니다.")
                                else:
                                    print("수정을 취소했습니다.")

                            elif select == "4":
                                gropePw = input("원하시는 등급의 비밀번호를 입력해주세요 :")
                                if gropePw in gropePasswords:
                                    grope = gropePasswords.get(gropePw)
                                    if input(dedent(f"""\
                                    {grope}
                                    해당 내용으로 확정하시겠습니까?
                                    (y/n)
                                    >>>""")) == "y" :
                                        gropes[idx] = grope
                                        print("수정을 완료했습니다.")
                                    else:
                                        print("수정을 취소했습니다.")

                                else:
                                    print("비밀번호가 틀렸습니다.")












            elif subSelect == "4":
                if session is None: #로그인을 해야 세션이 바뀐다. 즉, 로그인을 안해서 None 상태면 if문 실행
                    print("로그인이 필요한 서비스입니다.")

                else:
                    print("회원 탈퇴 메뉴로 진입합니다.")
                    id = input("탈퇴할 계정의 아이디를 입력해주세요.")
                    if id in ids :
                        idx = ids.index(id)
                        password = input("탈퇴할 계정의 비밀번호를 입력해주세요.")
                        if password == passwords[idx] :
                            question = input(dedent(f"""\
                            정말로 해당 계정을 삭제하시겠습니까?
                            이름 = {names[idx]}
                            학번 = {stuIdxs[idx]}
                            아이디 = {ids[idx]}
                            비밀번호 = {passwords[idx]}
                            등급 = {gropes[idx]}
                            (y/n)
                            >>>"""))
                            if question == "y" :
                                sns.pop(idx)
                                stuIdxs.pop(idx)
                                names.pop(idx)
                                ids.pop(idx)
                                passwords.pop(idx)
                                gropes.pop(idx)
                                print("회원 탈퇴를 완료했습니다.")
                            else:
                                print("회원 탈퇴를 취소합니다.")

                        else:
                            print("비밀번호가 틀렸습니다.")

                    else:
                        print("아이디가 틀렸습니다.")



            elif subSelect == "5":
                if session is None: #로그인을 해야 세션이 바뀐다. 즉, 로그인을 안해서 None 상태면 if문 실행
                    print("로그인이 필요한 서비스입니다.")
                else:
                    question = input("정말로 로그아웃 하시겠습니까? (y/n) :")
                    if question == "y" :
                        session = None
                        print("로그아웃이 완료 되었습니다.")

            elif subSelect == "9":
                print("회원관리 메뉴를 종료합니다.")
                subRun = False

            else:
                print("올바른 메뉴의 번호를 입력해주세요.")





    elif select == "2":
        if session is None:
            print("로그인이 필요한 서비스입니다.")
            continue

        print("성적관리 메뉴로 진입합니다.")
        scoreRun = True
        while scoreRun:
            print(scoreMenu)
            scoreSelect = input("원하시는 메뉴의 번호를 입력해주세요 :")
            if scoreSelect == "1":
                if gropes[session] == "professor" :
                    print("성적입력 메뉴로 진입합니다.")
                    sn = int(input("성적을 입력할 학생의 학번 :"))
                    if sn in stuIdxs:
                        if sn in pythonScores :
                            print("이미 점수가 입력 되어있는 학생입니다. 점수 변동을 원하시면 수정 메뉴를 선택해주세요.")
                            continue

                        stuIdx = stuIdxs.index(sn)
                        python = int(input("파이썬 점수 :"))
                        dataBase = int(input("데이터베이스 점수 :"))
                        wwwScore = int(input("프론트 점수 :"))
                        totalScore = python + dataBase + wwwScore
                        avgScore = round(totalScore / 3,0)


                        if python >= 90:
                            pythonGradeScore = "A"
                        elif python >= 80:
                            pythonGradeScore = "B"
                        elif python >= 70:
                            pythonGradeScore = "C"
                        else:
                            pythonGradeScore = "F"

                        if dataBase >= 90:
                            dataBaseGradeScore = "A"
                        elif dataBase >= 80:
                            dataBaseGradeScore = "B"
                        elif dataBase >= 70:
                            dataBaseGradeScore = "C"
                        else:
                            dataBaseGradeScore = "F"

                        if wwwScore >= 90:
                            wwwGradeScore = "A"
                        elif wwwScore >= 80:
                            wwwGradeScore = "B"
                        elif wwwScore >= 70:
                            wwwGradeScore = "C"
                        else:
                            wwwGradeScore = "F"

                        if input(dedent(f"""\
                        아래의 내용으로 확정하시겠습니까?
                        이름 = {names[stuIdx]}
                        학번 = {stuIdxs[stuIdx]}
                        파이썬 점수 : {python} 등급 : {pythonGradeScore}
                        데이터 점수 : {dataBase} 등급 : {dataBaseGradeScore}
                        프론트 점수 : {wwwScore} 등급 : {wwwGradeScore}
                        총점 : {totalScore}
                        평균 : {avgScore}
                        (y/n)
                        >>>""")) == "y" :
                            pythonScores[sn] = python
                            dataBaseScores[sn] = dataBase
                            wwwScores[sn] = wwwScore
                            pythonGradeScores[sn] = pythonGradeScore
                            dataBaseGradeScores[sn] = dataBaseGradeScore
                            wwwGradeScores[sn] = wwwGradeScore
                            totalScores[sn] = totalScore
                            avgScores[sn] = avgScore
                            print("학생 성적 입력이 완료되었습니다.")
                            #print(pythonScores)

                        else:
                            print("학생 성적 입력을 취소했습니다.")
                    else:
                        print("학번을 찾을 수 없습니다.")

                else:
                    print("교수 등급만 입장가능합니다.")


            elif scoreSelect == "2":
                print("성적보기 메뉴로 진입합니다.")
                if gropes[session] == "professor" or "admin" or "office" :
                    select = input("전체 학생 성적 열람 : 1\n개별 학생 성적 열람 : 2\n>>>")
                    if select == "1":
                        for i in range(len(stuIdxs)):
                            if stuIdxs[i] :
                                print(dedent(f"""\
                                학번 : {stuIdxs[i]}
                                이름 : {names[i]} 
                                파이썬 점수 : {pythonScores.get(i+1,"입력된 점수가 없습니다.")} {pythonGradeScores.get(i+1,"입력된 등급이 없습니다.")}
                                데이터 점수 : {dataBaseScores.get(i+1,"입력된 점수가 없습니다.")} {dataBaseGradeScores.get(i+1,"입력된 등급이 없습니다.")}
                                프론트 점수 : {wwwScores.get(i+1,"입력된 점수가 없습니다.")} {wwwGradeScores.get(i+1,"입력된 등급이 없습니다.")}
                                """))



                    elif select == "2":
                        sn = int(input("학번을 입력해주세요 :"))
                        if sn in stuIdxs:  # sns와 stuIdxs는 같음
                            stuIdx = stuIdxs.index(sn)
                            print(dedent(f"""\
                            학번 = {stuIdxs[stuIdx]}
                            이름 = {names[stuIdx]}
                            파이썬 점수 : {pythonScores.get(stuIdx+1,"입력된 점수가 없습니다.")} {pythonGradeScores.get(stuIdx+1,"입력된 등급이 없습니다.")}
                            데이터 점수 : {dataBaseScores.get(stuIdx+1,"입력된 점수가 없습니다.")} {dataBaseGradeScores.get(stuIdx+1,"입력된 등급이 없습니다.")}
                            프론트 점수 : {wwwScores.get(stuIdx+1,"입력된 점수가 없습니다.")} {wwwGradeScores.get(stuIdx+1,"입력된 등급이 없습니다.")}          
                            총점 : {totalScores.get(stuIdx+1,"입력된 총점이 없습니다.")}
                            평균 : {avgScores.get(stuIdx+1,"입력된 평균이 없습니다.")}
                            """))
                        else:
                            print("입력한 학번에 해당하는 학생이 없습니다.")

                    else:
                        print("성적보기를 취소합니다.")


                elif gropes[session] == "stu" or "parents" or "guests" :
                    sn = int(input("학번을 입력해주세요 :"))
                    if sn in stuIdxs: #sns와 stuIdxs는 같음
                        stuIdx = stuIdxs.index(sn)
                        print(dedent(f"""\
                        학번 = {stuIdxs[stuIdx]}
                        이름 = {names[stuIdx]}
                        파이썬 점수 : {pythonScores[stuIdx]}점 {pythonGradeScores[stuIdx]}등급
                        데이터 점수 : {dataBaseScores[stuIdx]}점 {dataBaseGradeScores[stuIdx]}등급
                        프론트 점수 : {wwwScores[stuIdx]}점 {wwwGradeScores[stuIdx]}등급            
                        총점 : {totalScores[stuIdx]}점
                        평균 : {avgScores[stuIdx]}점
                        """))
                    else:
                        print("학번을 찾지 못했습니다.")







            elif scoreSelect == "3":
                if gropes[session] == "professor" or "admin" or "office" :

                    print("성적수정 메뉴로 진입합니다.")
                    sn = int(input("수정할 학생의 학번을 입력해주세요 :"))
                    if sn in pythonScores or dataBaseScores or wwwScores :


                        if sn in stuIdxs :
                            stuIdx = stuIdxs.index(sn)
                            python = int(input("수정할 파이썬 점수 :"))
                            dataBase = int(input("수정할 데이터 점수 :"))
                            wwwScore = int(input("수정할 프론트 점수 :"))
                            totalScore = python + dataBase + wwwScore
                            avgScore = round(totalScore / 3, 0)

                            if python >= 90:
                                pythonGradeScore = "A"
                            elif python >= 80:
                                pythonGradeScore = "B"
                            elif python >= 70:
                                pythonGradeScore = "C"
                            else:
                                pythonGradeScore = "F"

                            if dataBase >= 90:
                                dataBaseGradeScore = "A"
                            elif dataBase >= 80:
                                dataBaseGradeScore = "B"
                            elif dataBase >= 70:
                                dataBaseGradeScore = "C"
                            else:
                                dataBaseGradeScore = "F"

                            if wwwScore >= 90:
                               wwwGradeScore = "A"
                            elif wwwScore >= 80:
                                wwwGradeScore = "B"
                            elif wwwScore >= 70:
                                wwwGradeScore = "C"
                            else:
                                wwwGradeScore = "F"



                            if input(dedent(f"""\
                            해당 점수로 수정을 확정하시겠습니까?
                            학번 : {stuIdxs[stuIdx]}
                            이름 : {names[stuIdx]}
                            파이썬 점수 : {python}
                            데이터 점수 : {dataBase}
                            프론트 점수 : {wwwScore}
                            총점 : {totalScore}
                            평균 : {avgScore}
                            """)) == "y" :

                                pythonScores[sn] = python
                                dataBaseScores[sn] = dataBase
                                wwwScores[sn] = wwwScore
                                totalScores[sn] = totalScore
                                avgScores[sn] = avgScore
                                print(pythonScores)
                                print("수정이 완료되었습니다.")


                            else:
                                print("수정을 취소합니다.")


                        else:
                            print("학번을 찾을 수 없습니다.")

                    else:
                        print("수정할 성적이 없습니다.")

                else:
                    print("권한이 없습니다.")




            elif scoreSelect == "4":
                if not gropes[session] == "admin" or "office" :
                    print("권한이 없습니다.")
                    continue

                print("성적백업 메뉴로 진입합니다.")
                sn = int(input("백업할 학생의 학번을 입력해주세요 :"))
                if sn in stuIdxs :
                    stuIdx = stuIdxs.index(sn)





            elif scoreSelect == "9":
                print("성적관리 메뉴를 종료합니다.")
                scoreRun = False

            else: #1,2,3,4,9 말고 다른 키를 넣을 경우
                print("올바른 메뉴의 번호를 입력해주세요.")


    elif select == "3":
        if session is None:
            print("로그인이 필요한 메뉴입니다.")
            continue

        print("게시판 메뉴로 진입합니다.")
        boardRun = True
        while boardRun:
            print(boardMenu)
            boardSelect = input("원하시는 메뉴의 번호를 입력해주세요 :")
            if boardSelect == "1":
                print("")

            elif boardSelect == "2":
                print("")

            elif boardSelect == "3":
                print("")

            elif boardSelect == "4":
                print("")

            elif boardSelect == "5":
                print("")

            elif boardSelect == "9":
                print("게시판 메뉴를 종료합니다.")
                boardRun = False

            else:
                print("올바른 메뉴의 번호를 입력해주세요.")

    elif select == "4":
        if session is None:
            print("로그인이 필요한 서비스입니다.")
            continue

        elif gropes[session] == "admin" :
            print("관리자 메뉴로 진입합니다.")
        else:
            print("관리자만 입장 가능합니다.")
    elif select == "9":
        print("프로그램을 종료합니다.")
        run = False

    else:
        print("올바른 메뉴의 번호를 입력해주세요.")