#while run subRun
#if 메뉴 선택이나 분기 판단용
#for 리스트에 있는 전체내용 출력용
#for in 리스트에 있는 내용 인덱스 찾는 용
from textwrap import dedent

run = True #구동용
session = None #로그인 상태 판단용


sns = [1] #계정 딕셔너리에 넣을 시리얼 넘버 값 계산용(중복 방지)
ssns = [] #상품 딕셔너리에 넣을 시리얼 넘버 값 계산용(중복 방지)
# 계정정보 id키의 벨류값 리스트 인덱스의 0은 비번, 1은 sn, 2는 이름인거 기억하기.
#                               비번   sn   이름    등급
#                                0     1    2      3
accountInformations = {'psh' : ['1234',1,'박승호','admin']} #아이디 : 비번+중복 방지용 sn+이름+등급(계정정보) 딕셔너리
gropePasswords = {'1234' : 'admin','2345' : 'seller','3456' : 'customer'} #등급 판단용 비번
trash = {}
goods = {} #상품 변수 (상품의 이름을 통해 상품의 번호, 종류, 등급 등등을 알 수 있게 딕셔너리에 리스트[]로 넣기)
# !!! 아이디가 절대 똑같아선 안됨. 딕셔너리 특성 회원가입과 회원정보수정에서 안전장치 걸기


















mainMenu = """
======================
메인 페이지로 진입하였습니다.
======================

1. 로그인 페이지
2. 상점 페이지

9. 프로그램 종료
"""



loginMenu =  """
=========================
로그인 페이지에 진입하였습니다.
=========================

1. 회원가입
2. 로그인
3. 회원정보수정
4. 회원탈퇴
5. 로그아웃

9. 회원가입 페이지 종료
"""

shopMenu = """
==============================
음료수 상점 페이지에 진입하셨습니다.
==============================

1. 상품 등록
2. 상품 리스트 보기
3. 상품 세부내용 수정
4. 상품 삭제

9. 상점 페이지 종료
"""







while run:
    print(mainMenu) #메인 메뉴
    select = input("원하시는 메뉴의 버튼을 눌러주세요 :")
    if select == "1" :
        loginrun = True
        while loginrun:
            print(loginMenu)
            select = input("원하시는 메뉴의 버튼을 눌러주세요 :")
            if select == "1" :
                subrun = True #회원가입 메뉴 while문 구동용
                while subrun:

                    print("회원가입 메뉴로 진입합니다.")


                    name = input("이름을 입력해주세요 :")
                    id = input("아이디를 입력해주세요 :")
                    if id in accountInformations :
                        print("중복되는 아이디입니다.")
                        continue

                    else:
                        password = input("비밀번호를 입력해주세요 :")
                        grope = gropePasswords.get(input("그룹 비밀번호를 입력해주세요 :"),'guest')
                        #gropePasswords에 인풋한 내용이
                        # 있으면 = grope에 인풋한 내용(키값)의 벨류값이 들어감
                        # 없으면 = grope에 디폴트값이 들어감 즉 게스트로 분류





                    print(dedent(f"""\
                    이름 : {name}
                    아이디 : {id}
                    비밀번호 : {password}
                    등급 : {grope}
                    
                    """))
                    if input("위 내용으로 회원가입을 완료하시겠습니까? (y/n) :") =="y" :

                        sn = len(sns)+1 #시리얼 넘버 삽입용 단일 변수 연계못함
                        sns.append(sn)
                        accountInformations[id] = [password,sn,name,grope]



                        print("회원가입을 완료했습니다.")
                        subrun = False

                    else:
                        print("회원가입을 취소했습니다.")
                        subrun = False






            elif select == "2" :
                print("로그인 메뉴로 진입합니다.")
                if session != None :
                    print("이미 로그인 되어있습니다.")
                    continue

                wallrun = True #방화벽 while문용
                wall = 3
                while wallrun:

                    id = input("아이디를 입력해주세요 :")
                    password = input("비밀번호를 입력해주세요 :")
                    # 딕셔너리 활용, 키가 아이디기 때문에 키(아이디)에 맞는 벨류(비밀번호)가 입력됐는지 검증 가능
                    if accountInformations.get(id,"없음")[0] == password :
                        session = id
                        print("로그인에 성공했습니다.")
                        wallrun = False
                    else:
                        print("아이디 또는 비밀번호가 틀렸습니다.")
                        wall -= 1

                    if wall == 2:
                        print("3회 이상 틀릴 시 강제로 로그인 화면이 종료됩니다.")

                    if wall == 0:
                        print("비밀번호를 3회 이상 틀렸습니다. 로그인 메뉴를 종료합니다.")
                        wallrun = False


            elif select == "3" :
                if session == None :
                    print("로그인이 필요한 서비스입니다.")
                    continue

                print("회원정보수정 메뉴로 진입합니다.")
                subrun = True
                while subrun :
                    name = input("수정할 이름 :")
                    id = input("수정할 아이디 :")
                    if id in accountInformations :
                        print("중복되는 아이디입니다.")
                        continue

                    else:
                        password = input("수정할 비밀번호 :")
                        gropePassword = input("수정할 등급의 비밀번호 :")
                        if gropePassword not in gropePasswords :
                            print("등급 비밀번호가 잘못되었습니다. 자동으로 게스트로 조정됩니다.")
                            grope = "guest"
                        else:
                            grope = gropePasswords.get(gropePassword)


                        if input(dedent(f"""\
                        해당 내용으로 확정하시겠습니까?
                        변경될 이름 : {name}
                        변경될 아이디 : {id}
                        변경될 비밀번호 : {password}
                        변경될 그룹 : {grope}
                        (y/n)
                        >>>""")) == "y":

                            sn = accountInformations.get(session)[1]
                            accountInformations[id] = [password,sn,name,grope]
                            print("회원정보 변경을 완료했습니다.")
                            subrun = False

                        else:
                            print("회원정보 변경을 취소했습니다.")
                            subrun = False








            elif select == "4" :
                if session == None :
                    print("로그인이 필요한 서비스입니다.")
                    continue

                print("회원탈퇴 메뉴로 진입합니다.")
                print("")
                if input("정말로 회원을 탈퇴하시겠습니까? (y/n) :") =="y" :

                    trash = accountInformations.pop(session) #pop구문은 변수에 pop된 내용을 삽입해야 동작가능
                    print("회원탈퇴를 완료했습니다.")









            elif select == "5" :
                if  session == None :
                    print("로그인이 필요한 서비스입니다.")
                    continue

                if input("정말로 로그아웃 하시겠습니까? (y/n) :") == "y" :
                    print("로그아웃을 완료했습니다.")
                    session = None
                else:
                    print("로그아웃을 취소했습니다.")






            elif select == "9" :
                print("로그인 페이지를 종료합니다.")
                loginrun = False

            else:
                print("올바른 번호를 입력해주세요.")
















    elif select == "2": #상점 페이지 입장
        if session == None :
            print("로그인이 필요한 서비스입니다.")
            continue
        shopRun = True #상점 페이지 while문 구동용
        while shopRun :
            print(shopMenu)
            select = input("원하시는 메뉴의 버튼을 눌러주세요 :")
            if select == "1" :
                if accountInformations.get(session,"입력없음")[3] == "seller" or "admin" : #계정정보 딕셔너리의 키에 대응되는 벨류 리스트의 3번자리
                    print("상품 등록 메뉴에 진입합니다.")


                    #등록될 시 인풋한 내용 말고도 로그인한 사람의 이름도 함께 찍혀야한다.
                    name = input("등록할 상품의 이름 :")
                    manufacturingData = input("제조일자 :")
                    expirationData = input("소비기한 :")
                    ingredientsList = input("성분표 :")
                    pay = int(input("가격 : ")) #가격
                    day = input("등록 날짜 :") #자동으로 넣고싶지만 아직 자동화 날짜 계산 방법을 모른다.
                    inventory = int(input("재고 :"))


                    sn = len(ssns)+1


                    if input(dedent(f"""\
                    품번 : {sn}
                    상품명 : {name}
                    제조일자 : {manufacturingData}
                    소비기한 : {expirationData}
                    성분표 : {ingredientsList}
                    가격 : {pay}원
                    
                    등록 날짜 : {day}
                    등록자 명 : {accountInformations.get(session)[2]}
                    재고 : {inventory}개
                    해당 내용으로 확정하시겠습니까?
                    (y/n)
                    """)) == "y" :
                        print("상품 등록을 완료했습니다.")
                        goods[sn] = [name,manufacturingData,expirationData,ingredientsList,pay,day,accountInformations.get(session)[2],inventory]
                        #print(goods)

                    else:
                        print("상품 등록을 취소했습니다.")

                else:
                    print("seller(판매자)만 사용 가능한 메뉴입니다.")















            elif select == "2" :
                print("상품 리스트 보기 메뉴에 진입합니다.")
                shopSelect = input("원하시는 메뉴의 번호를 눌러주세요\n\n1. 전체 물품 보기\n2. 물품 이름 검색\n")
                if shopSelect == "1" :
                    print("전체 물품 리스트를 출력합니다.")

                    a = 0
                    for i in goods.keys() :
                        print(dedent(f"""\
                        ------------------------------------------------------------
                        {a+1}. {goods.get(i)[0]} | {goods.get(i)[4]}원 | {goods.get(i)[5]} | {goods.get(i)[6]} | {goods.get(i)[7]}개"""))
                        print("------------------------------------------------------------")
                        sn = int(input("열람하실 상품의 품번을 입력해주세요 :"))
                        if sn in goods :
                            search = input("열람하실 상품의 품명을 입력해주세요 :")
                            if search == goods.get(sn)[0] :
                                print(dedent(f"""\
                                        품번 : {goods.get(sn)[0]}
                                        상품명 : {search}
                                        제조일자 : {goods.get(sn)[1]}
                                        소비기한 : {goods.get(sn)[2]}
                                        성분표 : {goods.get(sn)[3]}
                                        가격 : {goods.get(sn)[4]}원

                                        등록 날짜 : {goods.get(sn)[5]}
                                        등록자 명 : {goods.get(sn)[6]}     
                                        재고 : {goods.get(sn)[7]}개                   
                                        """))
                                if input("해당 상품을 구입하시겠습니까? (y/n) :") == "y":
                                    if goods.get(sn)[7] == 0:
                                        print("해당 상품의 재고가 없습니다.")
                                        continue

                                    pay = input("결제 수단을 선택해주세요.\n\n1. 현금\n2. 카드\n>>>")
                                    if pay == "1" or "현금":
                                        money = int(input("지불하실 현금의 액수를 입력해주세요 :"))
                                        if goods.get(sn)[4] > money:
                                            print("액수가 부족하므로 현금을 반환합니다.")
                                        elif goods.get(sn)[4] == money:
                                            if input(dedent(f"""\
                                                    정말로 결제하시겠습니까? (y/n) :""")) == "y":
                                                goods.get(sn)[7] -= 1
                                                print("결제가 완료되었습니다.")

                                            else:
                                                print("결제를 취소했습니다.")

                                        elif goods.get(sn)[4] < money:
                                            penny = money - goods.get(sn)[4]
                                            if input(dedent(f"""\
                                                    정말로 결제하시겠습니까? 

                                                    상품 금액 : {goods.get(sn)[4]}원
                                                    결제 금액 : {money}원
                                                    잔액 : {penny}원
                                                    (y/n)
                                                    """)) == "y":
                                                penny = money - goods.get(sn)[4]
                                                goods.get(sn)[7] -= 1
                                                print(f"결제가 완료되었습니다.")
                                            else:
                                                print("결제를 취소했습니다.")

                                    elif pay == "2" or "카드":  # 원래는 자동화를 하고싶었으나 능력부족
                                        if input("정말로 결제하시겠습니까? (y/n) :") == "y":
                                            print("결제가 완료되었습니다.")

                                        else:
                                            print("결제를 취소했습니다.")

                            else:
                                print("등록되지 않은 품번입니다.")

                        else:
                            print("등록되지 않은 품명입니다.")



                elif shopSelect == "2" :
                    print("물품 이름을 검색합니다.")

                    sn = int(input("검색할 상품의 품번 :"))
                    if sn in goods :
                        search = input("검색할 상품의 품명 :")
                        if search == goods.get(sn)[0] :
                            print(dedent(f"""\
                                            품번 : {goods.get(sn)[0]}
                                            상품명 : {sn}
                                            제조일자 : {goods.get(sn)[1]}
                                            소비기한 : {goods.get(sn)[2]}
                                            성분표 : {goods.get(sn)[3]}
                                            가격 : {goods.get(sn)[4]}원

                                            등록 날짜 : {goods.get(sn)[5]}
                                            등록자 명 : {goods.get(sn)[6]}     
                                            재고 : {goods.get(sn)[7]}개                   
                                            """))
                            if input("해당 상품을 구입하시겠습니까? (y/n) :") == "y":
                                if goods.get(sn)[7] == 0:
                                    print("해당 상품의 재고가 없습니다.")
                                    continue

                                pay = input("결제 수단을 선택해주세요.\n\n1. 현금\n2. 카드\n>>>")
                                if pay == "1" or "현금":
                                    money = int(input("지불하실 현금의 액수를 입력해주세요 :"))
                                    if goods.get(sn)[4] > money:
                                        print("액수가 부족하므로 현금을 반환합니다.")
                                    elif goods.get(sn)[4] == money:
                                        if input(dedent(f"""\
                                                        정말로 결제하시겠습니까? (y/n) :""")) == "y":
                                            goods.get(sn)[7] -= 1
                                            print("결제가 완료되었습니다.")

                                        else:
                                            print("결제를 취소했습니다.")

                                    elif goods.get(sn)[4] < money:
                                        penny = money - goods.get(sn)[4]
                                        if input(dedent(f"""\
                                                        정말로 결제하시겠습니까? 

                                                        상품 금액 : {goods.get(sn)[4]}원
                                                        결제 금액 : {money}원
                                                        잔액 : {penny}원
                                                        (y/n)
                                                        """)) == "y":
                                            penny = money - goods.get(sn)[4]
                                            goods.get(sn)[7] -= 1
                                            print(f"결제가 완료되었습니다.")
                                        else:
                                            print("결제를 취소했습니다.")

                                elif pay == "2" or "카드":  # 원래는 자동화를 하고싶었으나 능력부족
                                    if input("정말로 결제하시겠습니까? (y/n) :") == "y":
                                        goods.get(sn)[7] -= 1
                                        print("결제가 완료되었습니다.")

                                    else:
                                        print("결제를 취소했습니다.")

                        else:
                            print("등록되지 않은 품번입니다.")

                    else:
                        print("등록되지 않은 품명입니다.")







                else:
                    print("올바른 번호를 입력해주세요.")


            elif select == "3" :
                print("상품 세부내용 수정 메뉴에 진입합니다.")

                sn = int(input("수정하실 상품의 품번 :"))
                if sn in goods :
                    if input("수정하실 상품의 이름 :") == goods.get(sn)[0] :
                        print("수정할 내용을 입력합니다.")
                        name = input("상품 이름 :")
                        manufacturingData = input("제조일자 :")
                        expirationData = input("소비기한 :")
                        ingredientsList = input("성분표 :")
                        pay = int(input("가격 : "))
                        day = input("수정 날짜 :")
                        inventory = int(input("재고 :"))


                        if input(dedent(f"""\
                        품번 : {sn}
                        상품명 : {name}
                        제조일자 : {manufacturingData}
                        소비기한 : {expirationData}
                        성분표 : {ingredientsList}
                        가격 : {pay}원
                        
                        수정 날짜 : {day}
                        등록자 명 : {accountInformations.get(session)[2]}
                        재고 : {inventory}개
                        
                        해당 내용으로 수정하시겠습니까?
                        (y/n)
                        """)) == "y":
                            print("수정이 완료되었습니다.")

                            goods[sn] = [name,manufacturingData,expirationData,ingredientsList,pay,day,accountInformations.get(session)[2],inventory]
                            #print(goods)

                        else:
                            print("상품 정보 수정을 취소했습니다.")

                    else:
                        print("해당되는 품번이 없습니다.")

                else:
                    print("해당되는 상품명이 없습니다.")







            elif select == "4" :
                print("상품 삭제 메뉴에 진입합니다.")

                sn = int(input("삭제할 상품의 품번 :"))
                if sn in goods :
                    name = input("삭제할 상품의 품명 :")
                    if name == goods.get(sn)[0] :
                        if input(dedent(f"""\
                        품번 : {sn}
                        상품명 : {name}
                        제조일자 : {goods.get(sn)[1]}
                        소비기한 : {goods.get(sn)[2]}
                        성분표 : {goods.get(sn)[3]}
                        가격 : {goods.get(sn)[4]}원
                        
                        등록 날짜 : {goods.get(sn)[5]}
                        등록자 명 : {goods.get(sn)[6]}
                        재고 : {goods.get(sn)[7]}개
                        해당 상품을 정말로 삭제할까요?
                        (y/n)
                        """)) == "y" :
                            print("상품 정보 삭제를 완료했습니다.")

                            trash = goods.pop(sn)

                        else:
                            print("상품 정보 삭제를 취소했습니다.")

                    else:
                        print("해당되는 품명이 없습니다.")

                else:
                    print("해당되는 품번이 없습니다.")

                            #print(goods)

            elif select == "9" :
                print("상점 페이지를 종료합니다.")
                shopRun = False


            else:
                print("올바른 번호를 입력해주세요.")












    elif select == "9":
        print("프로그램을 종료합니다.")
        run = False

    else:
        print("올바른 번호를 입력해주세요.")