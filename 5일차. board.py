#비회원용 게시판을 만들어 보자.
from textwrap import dedent


#프로젝트 목표
#C : 게시글 등록
#R : 게시글 전체 보기(리스트)
#R : 게시글 자세히 보기
#U : 게시글 수정
#D : 게시글 삭제

#사용할 변수 리스트 (전역 변수 : 프로그램 전반적으로 사용가능)
run = True #while문 프로그램 구동중!!
board_nos = [] #중복되지 않는 유일한 값, not null
board_titles = [] #게시글의 제목
board_contents = [] #게시글의 내용
board_writers = [] #글쓴이
board_passwords = [] #게시글의 비밀번호(수정, 삭제용)
board_hits = [] #좋아요!!!
board_visitcounts = [] #조회수!!!




#주메뉴
menu = """
==============================
엠비씨 아카데미 비회원 게시판입니다.
==============================

1. 게시글 작성
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정하기
5. 게시글 삭제하기
6. 게시판 프로그램 종료

"""

#프로그램 실행문



while run:
    print(menu)
    #select는 while문 안쪽에서만 활용되는 1회용 변수 : 지역변수
    select = input("원하시는 메뉴의 숫자를 눌러주세요 :")
    #        input은 키보드로 입력한 값을 문자열로 전달함

#----------------------------------------------------------------------------------------------------------------------#
#                                                       1번
#----------------------------------------------------------------------------------------------------------------------#

    if select == "1" : #키보드로 입력한 값이 1이면?
        print("게시글을 등록합니다.")
        #게시글 등록용 코드 추가

        #게시글의 번호는 프로세스가 자동처리
        #키보드로 게시글을 받아 변수에 넣음
        title = input("제목 :")
        content = input("내용 :")
        writer = input("작성자 :")
        password = input("비밀번호 :")

        #넣은 정보를 확인한다.
        print(dedent(f"""\
        제목    : {title}
        내용    : {content}
        작성자  : {writer}
        비밀번호 : {password}
        """))
        choose = input("저장하려면 y를 누르세요 :")

        if choose == "y" :
            board_titles.append(title)
            board_contents.append(content)
            board_writers.append(writer)
            board_passwords.append(password)

            #제목에 리스트에서 인덱스를 추출하여 +1한 값이 no
            #for idx in range(len(board_titles)):
            #    board_nos.append(idx+1)
            #아래는 리스트의 제목 중복 문제를 대비해서 준비한 코드(지금 코드 뿐만아니라 나중에서의 가능성에서도 확실하게 nos로 하는게 맞다.)
            no = len(board_nos) + 1
            board_nos.append(no)
            #no = len(board_titles)
            #board_nos.append(no)


            board_hits.append(0) #좋아요
            board_visitcounts.append(0) #조회수
            print(f"{no}번의 게시글이 등록 되었습니다.")


        else:
            print("저장이 취소되었습니다.")

#----------------------------------------------------------------------------------------------------------------------#
#                                                       2번
#----------------------------------------------------------------------------------------------------------------------#

    elif select == "2" :
        print("[게시글 전체 목록 출력]")
        #게시글 리스트 보기용 코드 추가
        no = "번호"
        title = "제목"
        writer = "작성자"
        view = "조회수"
        hit = "좋아요"
        print("---------------------------------------------")
        print(f"{no:^5}|{title:^10}|{writer:^10}|{view:^5}|{hit:^5}")
        print("---------------------------------------------")

        if len(board_nos) == 0 :
            print("등록된 게시물이 없습니다.")

        else:
            for i in range(len(board_nos)): #게시글의 개수만큼 반복 (0부터 게시물 수까지)
                print(f"{board_nos[i]:^5}{board_titles[i]:^12}{board_writers[i]:^10}{board_visitcounts[i]:^11}{board_hits[i]:^6}")
                #           번호                제목                 작성자                 조회수                  좋아요

#----------------------------------------------------------------------------------------------------------------------#
#                                                      3번
#----------------------------------------------------------------------------------------------------------------------#

    elif select == "3" :
        print("[게시글 자세히 보기]")
        bno = int(input("열람하실 게시글의 번호를 입력해주세요 :"))
        if bno in board_nos : #등록된 게시물의 유무 확인
            idx = board_nos.index(bno) #리스트에서 게시물의 인덱스 값을 찾아옴
            board_visitcounts[idx] += 1 #조회수 1 증가
            print(dedent(f"""\
            ----------------------------------------
            번호 : {board_nos[idx]}
            제목 : {board_titles[idx]}
            내용 : {board_contents[idx]}
            글쓴이 : {board_writers[idx]}
            조회수 : {board_visitcounts[idx]}
            좋아요 : {board_hits[idx]}
            ----------------------------------------"""))

            if input("좋아요를 누르시겠습니까? (y/n) :") == "y" :
                board_hits[idx] += 1
                print(f"좋아요 +1")
            else:
                print("아쉽습니다. 다음에 더 좋은 게시글이 될겁니다.")


        else:
            print("해당번호에 게시글이 없습니다.")

#----------------------------------------------------------------------------------------------------------------------#
#                                                     4번
#----------------------------------------------------------------------------------------------------------------------#

    elif select == "4" :
        print("[게시글 수정하기]")
        bno = int(input("수정할 게시글의 번호를 입력해주세요 :"))
        wall = 3
        while bno in board_nos :
            idx = board_nos.index(bno)
            password = input("비밀번호를 입력해주세요 :")
            if password == board_passwords[idx] :
                print("해당 게시글 내용을 출력합니다.")
                print(dedent(f"""\
                번호 : {board_nos[idx]}
                제목 : {board_titles[idx]}
                내용 : {board_contents[idx]}
                글쓴이 : {board_writers[idx]}
                """))

                selec = input(dedent("""\
                수정할 내용의 번호를 입력하세요.
                1. 제목
                2. 내용
                3. 비밀번호
                4. 글쓴이
                >>>"""))
                if selec == "1" :
                    title = input("제목을 수정합니다 :")
                    if input(dedent(f"""
                    ====================================================
                    {title}
                    ====================================================
                    해당 내용으로 확정하시겠습니까?
                    (y/n) :""")) == "y" :
                        board_titles[idx] = title
                        print("수정을 완료했습니다.")
                        break
                    else:
                        print("수정을 취소합니다.")
                        break

                elif selec == "2" :
                    content = input("내용을 수정합니다 :")

                    if input(dedent(f"""\
                    ====================================================
                    {content}
                    ====================================================
                    해당 내용으로 확정하시겠습니까 (y/n) :""")) == "y" :

                        board_contents[idx] = content
                        print("수정을 완료했습니다.")
                        break
                    else:
                        print("수정을 취소합니다.")
                        break

                elif selec == "3" :
                    password = input("비밀번호를 수정합니다 :")
                    print(password)
                    if input("해당 내용으로 확정하시겠습니까? (y/n) :") == "y" :
                        board_passwords[idx] = password
                        print("수정을 완료했습니다.")
                        break
                    else:
                        print("수정을 취소했습니다.")
                        break

                elif selec == "4" :
                    writer = input("글쓴이를 수정합니다 :")
                    print(writer)
                    if input("해당 내용으로 확정하시겠습니까? (y/n) :") == "y" :
                        board_writers[idx] = writer
                        print("수정을 완료했습니다.")
                        break

                    else:
                        print("수정을 취소했습니다.")
                        break

                else:
                    print("수정을 취소합니다.")
                    break

            else:

                print("비밀번호가 틀렸습니다.")
                wall -= 1

            if wall == 2 :
                print("비밀번호가 3회 틀릴 시, 수정하기 메뉴가 강제 종료됩니다.")

            if wall == 0 :
                print("비밀번호가 3회 틀렸습니다. 수정하기 메뉴를 종료합니다.")
                break


        else:
            print("해당번호에 게시글이 없습니다.")
            break

#----------------------------------------------------------------------------------------------------------------------#
#                                                    5번
#----------------------------------------------------------------------------------------------------------------------#

    elif select == "5" :
        print("[게시글 삭제하기]")
        bno = int(input("삭제할 게시글의 번호를 입력해주세요 :"))
        wall = 3
        while bno in board_nos :
            idx = board_nos.index(bno)
            password = input("비밀번호를 입력해주세요 :")
            if password == board_passwords[idx] :
                if input(dedent(f"""\
                정말로 게시글을 삭제하시겠습니까?
                번호 : {board_nos[idx]}
                제목 : {board_titles[idx]}
                내용 : {board_contents[idx]}
                비밀번호 : {board_passwords[idx]}
                글쓴이 : {board_writers[idx]}
                조회수 : {board_visitcounts[idx]}
                좋아요 : {board_hits[idx]}

                *주의* 삭제된 게시물은 복구할 수 없습니다.
                (y/n)
                """)) == "y" :
                    board_nos.pop(idx)
                    board_titles.pop(idx)
                    board_contents.pop(idx)
                    board_passwords.pop(idx)
                    board_writers.pop(idx)
                    board_visitcounts.pop(idx)
                    board_hits.pop(idx)
                    print("게시글 삭제가 완료되었습니다.")
                    break

                else:
                    print("게시글 삭제를 취소합니다.")
                    break
            else:
                print("비밀번호가 틀렸습니다.")
                wall -= 1

            if wall == 2 :
                print("비밀번호가 3회 이상 틀리면 삭제 메뉴가 강제 종료됩니다.")

            if wall == 0 :
                print("비밀번호가 3회 이상 틀렸습니다. 삭제 메뉴를 종료합니다.")
                break


        else:
            print("해당되는 게시글 번호가 없습니다.")
            break

#----------------------------------------------------------------------------------------------------------------------#
#                                                    6번
#----------------------------------------------------------------------------------------------------------------------#

    elif select == "6" :
        print("[비회원 게시판 프로그램을 종료합니다]")
        run = False

    else:
        #1~6까지 잘못 입력된 값 처리용
        print("잘못 입력하셨습니다.")
