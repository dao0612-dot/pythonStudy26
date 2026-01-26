#상품에 대한 CRUD를 구현해보자!
#C -> 새상품 등록
#R -> 전체 상품 목록
#R -> 단일 상품 자세히 보기
#U -> 상품 수정
#D -> 상품 품절(매진)
from textwrap import dedent

#사용할 변수 (전역변수)
run = True

sns = [1,2] #물품 끌어오기용 시리얼 넘버
item_names = ["노트북","모니터"] #상품명
unit_prices = [1200000,400000] #단가
quantitys = [40,25] #수량
product_infors = ["AI용 삼성노트북","LG24인치 LED"] #상품 정보
categorys = ["잡화","잡화"] #상품 분류
shopping_cart = {}

#사용할 함수(메서드)
def item_add():
    print("item_add() 함수 호출 완료")
    print("새상품 추가용 함수로 진입합니다.")
    #새상품 추가용 실행문....

    select = input("원하시는 메뉴의 숫자를 눌러주세요.")
    if select == "1":
        print("교재 상품을 등록합니다.")
        name = input("상품 이름 :")
        price = int(input("상품 가격 :"))
        quantity = int(input("상품 수량 :"))
        product = input("상품 정보 :")
        category = "교재"
        sn = len(sns) + 1 #중복되지 않도록 등록될 때마다 1씩 올라감

        if input(dedent(f"""
        아래 내용으로 등록 확정하시겠습니까?
        이름 = {name}
        가격 = {price}원
        수량 = {quantity}개
        정보 = {product}
        분류 = {category}
        (y/n)
        """)) == "y" : #y를 눌러야 등록이 완료
            sns.append(sn)
            item_names.append(name)
            unit_prices.append(price)
            quantitys.append(quantity)
            product_infors.append(product)
            categorys.append(category)
            print("물품 등록을 완료했습니다.")

    elif select == "2":
        print("잡화 상품을 등록합니다.")
        name = input("상품 이름 :")
        price = int(input("상품 가격 :"))
        quantity = int(input("상품 수량 :"))
        product = input("상품 정보 :")
        category = "잡화"
        sn = len(sns) + 1 #중복되지 않도록 등록될 때마다 1씩 올라감

        if input(dedent(f"""
        아래 내용으로 등록 확정하시겠습니까?
        이름 = {name}
        가격 = {price}원
        수량 = {quantity}개
        정보 = {product}
        분류 = {category}
        (y/n)
        """)) == "y" :
            sns.append(sn)
            item_names.append(name)
            unit_prices.append(price)
            quantitys.append(quantity)
            product_infors.append(product)
            categorys.append(category)
            print("물품 등록을 완료했습니다.")


    elif select == "3":
        print("음식 상품을 등록합니다.")
        name = input("상품 이름 :")
        price = int(input("상품 가격 :"))
        quantity = int(input("상품 수량 :"))
        product = input("상품 정보 :")
        category = "음식"
        sn = len(sns) + 1 #중복되지 않도록 등록될 때마다 1씩 올라감

        if input(dedent(f"""
        아래 내용으로 등록 확정하시겠습니까?
        이름 = {name}
        가격 = {price}원
        수량 = {quantity}개
        정보 = {product}
        분류 = {category}
        (y/n)
        """)) == "y" :
            sns.append(sn)
            item_names.append(name)
            unit_prices.append(price)
            quantitys.append(quantity)
            product_infors.append(product)
            categorys.append(category)
            print("물품 등록을 완료했습니다.")


    elif select == "4":
        print("패션 상품을 등록합니다.")
        name = input("상품 이름 :")
        price = int(input("상품 가격 :"))
        quantity = int(input("상품 수량 :"))
        product = input("상품 정보 :")
        category = "패션"
        sn = len(sns) + 1 #중복되지 않도록 등록될 때마다 1씩 올라감

        if input(dedent(f"""
        아래 내용으로 등록 확정하시겠습니까?
        이름 = {name}
        가격 = {price}원
        수량 = {quantity}개
        정보 = {product}
        분류 = {category}
        (y/n)
        """)) == "y" :
            sns.append(sn)
            item_names.append(name)
            unit_prices.append(price)
            quantitys.append(quantity)
            product_infors.append(product)
            categorys.append(category)
            print("물품 등록을 완료했습니다.")

    elif select == "9":
        print("등록 프로그램을 종료합니다.")


    else:
        print("잘못된 메뉴 번호입니다.\n다시 입력해주세요.")









def item_list():
    print("item_list() 함수 호출 완료")
    print("현재 판매중인 상품 리스트입니다.")
    #리스트 출력용 for item in item_names:
    for i in range (len(item_names)): #등록된 물품을 이름(중복되어도 어차피 갯수만 알면 되기에)을
                                      #기준으로 갯수를 측정(len)후 range에 삽입. 0부터 len까지의 숫자를 i에 넣는다
        print(f"{i+1} | {item_names[i]} | {unit_prices[i]}원 | {quantitys[i]}개 | {product_infors[i]} | {categorys[i]}")







def item_view():
    print("item_view() 함수 호출 완료")
    print("상품 자세히 보기")
    #상품의 대한 상세 정보 표시
    item_list()
    select = int(input("자세히 볼 상품의 번호를 입력해주세요 :"))
    if select > len(item_names) or select < 0: #sns를 안넣고 하려던 온몸비틀기
        print("존재하지 않는 품번입니다.")

    else:

        idx = select - 1 #sns를 안넣고 하려던 온몸비틀기
        print(dedent(f"""
        이름 = {item_names[idx]}
        가격 = {unit_prices[idx]}원
        수량 = {quantitys[idx]}개
        정보 = {product_infors[idx]}
        분류 = {categorys[idx]}
        """))

        if input("쇼핑 화면으로 넘어가시겠습니까?") == "y":
            item_shopping() #자세히보기 메뉴에서 바로 결제 또는 장바구니에 담을 수 있게.
        else:
            print("구입을 취소합니다.")





def item_shopping():
    #전체 리스트 보기중에 쇼핑으로 넘어갈 때 사용

    selction = input("원하시는 상품의 번호를 입력해주세요 :")
    if selction.isdigit(): #인풋을 우선 받고, 거기에 숫자로 된 문자만이 있는지 걸러내는 isdigit
                           #이후에 int를 감아서 숫자열로 만든다.

        select = int(selction)
        if select > len(item_names) or select < 0:
            print("존재하지 않는 품번입니다.")

        else:

            idx = select - 1 #sns를 안넣고 하려던 온몸비틀기
            shopping = input(dedent(f"""
            이름 = {item_names[idx]}
            가격 = {unit_prices[idx]}원
            수량 = {quantitys[idx]}개
            정보 = {product_infors[idx]}
            분류 = {categorys[idx]}
            
            즉시 구매는 1번, 장바구니에 담기는 2번을 눌러주세요.
            """))

            if shopping == "1": #위의 input내용(shopping)이 "1"로 입력됐을 때
                quantity = int(input("구입하실 상품의 갯수를 입력해주세요 :"))
                allprice = unit_prices[idx] * quantity #선택한 물품의 인덱스 번호의 가격 * 구입하고자 한 상품의 갯수 = 총액
                select = input("결제하실 방법을 선택해주세요.\n1. 현금\n2. 카드\n") #결제 수단 선택용
                if select == "1" or "현금": # "1" 또는(or) "현금"이기에 둘중 아무거나 넣어도 True값이 나옴
                    money = int(input("지불하실 액수를 입력해주세요."))
                    if money > allprice: #지불한 액수가 상품 가격보다 커서 잔돈이 발생할 때
                        penny = money - allprice
                        if input(dedent(f"""
                        지불된 금액 = {money}원
                        상품의 금액 = {allprice}원
                        잔액 = {penny}원
                        결제를 확정하시겠습니까?
                        (y/n)
                        """)) == "y":
                            print(f"결제가 완료되었습니다. 거스름돈 {penny}원을 받아가시길 바랍니다.")
                            quantitys[idx] = quantitys[idx] - quantity #지금 구매하는 물품의 갯수의 idx위치에 새로 대입
                                                                       #단순하게 '기존 갯수 - 방금 구입한 갯수'를 한 것

                        else:
                            print("결제가 취소되었습니다.")
                    elif money == allprice: #지불한 액수가 상품 가격과 동일할 때
                        if input(dedent(f"""
                        지불된 금액 = {money}원
                        상품의 금액 = {allprice}원
                        잔액 = 0원
                        결제를 확정하시겠습니까?
                        (y/n)
                        """)) == "y":
                            print(f"결제가 완료되었습니다.")
                            quantitys[idx] = quantitys[idx] - quantity #idx위치의 갯수 - 구입한 갯수

                        else:
                            print("결제를 취소했습니다.")

                    else:
                        print("지불하신 금액이 충분하지 않습니다. 현금을 반환합니다.")

                elif select == "2" or "카드":
                    print("카드로 결제합니다.")


            elif shopping == "2":
                quantity = int(input("상품을 담을 갯수를 입력해주세요 :"))
                if quantity > quantitys[idx]:
                    print("구입 가능한 상품의 갯수보다 많습니다.")
                    return

                price = unit_prices[idx] * quantity
                sn = sns[idx]
                shopping_cart[sn] = [item_names[idx],quantity,price] #장바구니에 담을 때 key로 sn를 넣고
                                                                     #나머지 이름, 갯수, 가격은 각각 value리스트에 넣는다.
                                                                     #즉, 키만 안다면 나머지 정보를 전부 가져올 수 있다.
                print("장바구니에 성공적으로 담았습니다.")


            else:
                print("올바른 번호를 입력해주세요.")
    else:
        print("숫자를 입력해주세요.")


def item_calculate():
    if shopping_cart == {}: # 쇼핑카트 딕셔너리에 아무것도 없으면 함수를 빠져나간다(return)
        print("장바구니에 상품이 없습니다.")
        return

    for i in shopping_cart.keys(): #구입 전 내 장바구니 목록 보기용도
                                   #keys리스트를 i에 넣고(in) for문으로 반복하면
                                   #각각 i key값에 맞는 value의 인덱스 위치에 존재하는 값이 들어난다.
                                   #미리 세팅해준 value인덱스 순서는 0=이름 1=갯수 2=가격 으로 고정해둠
        print(f"{shopping_cart[i][0]} | {shopping_cart[i][1]}개 | {shopping_cart[i][2]}원")

    allprice = 0 #장바구니에 담긴 상품의 총액
    for i in shopping_cart.keys(): #그것을 계산해주는 for문
        allprice += shopping_cart[i][1] * shopping_cart[i][2]

    print("현재 물품 목록입니다.")
    if input("장바구니의 상품에 대한 결제를 진행하시겠습니까? (y/n)") == "y":
        select = input("결제하실 방법을 선택해주세요.\n1. 현금\n2. 카드\n")
        if select == "1" or "현금":
            money = int(input("지불하실 금액을 입력해주세요 :"))
            if money > allprice:
                penny = money - allprice
                if input(dedent(f"""
                        지불된 금액 = {money}원
                        상품의 금액 = {allprice}원
                        잔액 = {penny}원
                        결제를 확정하시겠습니까?
                        (y/n)
                        """)) == "y":
                    print(f"결제가 완료되었습니다. 거스름돈 {penny}원을 받아가시길 바랍니다.")
                    #미완성=======
                    for i in shopping_cart.keys() :
                        quantitys[i-1] -= shopping_cart[i][1]
                    shopping_cart.clear()

                else:
                    print("결제가 취소되었습니다.")
            elif money == allprice:
                if input(dedent(f"""
                        지불된 금액 = {money}원
                        상품의 금액 = {allprice}원
                        잔액 = 0원
                        결제를 확정하시겠습니까?
                        (y/n)
                        """)) == "y":
                    print(f"결제가 완료되었습니다.")
                    for i in shopping_cart.keys():
                        quantitys[i - 1] = quantitys[i - 1] - shopping_cart[i][1]
                    shopping_cart.clear()
                else:
                    print("결제를 취소했습니다.")

            else:
                print("지불하신 금액이 충분하지 않습니다. 현금을 반환합니다.")

        elif select == "2" or "카드":
            print("카드로 결제합니다.")


def item_update():
    print("item_update() 함수 호출 완료")
    print("상품 수정 하기")
    #상품에 대한 내용 수정하기
    item_list()
    select = int(input("수정할 물품의 품번 :"))
    if select > len(item_names) or select < 0:
        print("존재하지 않는 품번입니다.")

    else:
        idx = select - 1
        name = input("수정할 이름 :")
        price = int(input("수정할 가격 :"))
        quantity = int(input("수정할 수량 :"))
        product = input("수정할 정보 :")
        category = input("수정할 분류 :")

        if input(dedent(f"""
        아래의 내용으로 확정하시겠습니까?
        이름 = {name}
        가격 = {price}
        수량 = {quantity}
        정보 = {product}
        분류 = {category}
        (y/n)
        """)) == "y" :
            item_names[idx] = name
            unit_prices[idx] = price
            quantitys[idx] = quantity
            product_infors[idx] = product
            categorys[idx] = category
            print("수정이 완료되었습니다.")



def item_delete():
    print("item_delete() 함수 호출 완료")
    print("상품 삭제 하기")
    #상품 품절, 삭제하기
    item_list()
    select = int(input("삭제할 상품의 품번을 입력해주세요."))
    if select > len(item_names) or select < 0:
        print("존재하지 않는 품번입니다.")

    idx = select - 1
    if input(dedent(f"""
    해당 상품을 정말로 품절 처리 하시겠습니까?
    이름 = {item_names[idx]}
    가격 = {unit_prices[idx]}원
    수량 = {quantitys[idx]}개
    정보 = {product_infors[idx]}
    분류 = {categorys[idx]}
    (y/n)    
    """)) == "y":
        item_names.pop(idx)
        unit_prices.pop(idx)
        quantitys.pop(idx)
        product_infors.pop(idx)
        categorys.pop(idx)
        print("상품의 품절처리가 완료되었습니다.")


def main_menu():
    print("""
=========================
엠비씨 아카데미 쇼핑몰 입니다.

1. 상품등록
2. 상품리스트
3. 상품자세히보기
4. 상품수정하기
5. 상품삭제하기
6. 장바구니정산

9. 프로그램 종료

""")

def item_add_menu():
    print("""
==== 상품 추가용 메뉴에 진입 ====
1. 교재
2. 잡화
3. 음식
4. 패션

9. 종료

""")



#프로그램 주실행 코드 시작!!!
while run:
    main_menu() #메인메뉴 함수 호출하여 출력

    select = input("숫자 입력 :")
    if select == "1":
        item_add_menu() #아이템 추가용 메뉴 함수
        item_add() #아이템 추가용 코드



    elif select == "2":
        item_list()
        if input("쇼핑으로 넘아가시겠습니까? (y/n)") == "y":
            item_shopping()

        else:
            print("취소합니다.")

    elif select == "3":
        item_view()



    elif select == "4":
        item_update()

    elif select == "5":
        item_delete()

    elif select == "6":
        item_calculate()

    elif select == "9":
        print("프로그램을 종료합니다.")
        run = False

    else:
        print("잘못된 숫자를 입력하셨습니다.")
        print("다시 입력하세요.")