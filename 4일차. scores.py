#성적 처리용 프로그램을 개발해보자!!!!

#CREATE : 성적입력
#READ : 성적보기
#UPDATE : 성적수정
#DELETE : 성적삭제

#필요한 변수는?
sns = [] #학번
names = [] #이름
kors = [] #국어점수
engs = [] #영어점수
mats = [] #수학점수
tots = [] #총점 빈 배열
avgs = [] #평균 빈 배열
korgrades = [] #학점 빈 배열
enggrades = []
matgrades = []

menu = """
====================
엠비씨 아카데미 성적처리
====================
1. 성적입력
2. 성적보기
3. 성적수정
4. 성적삭제
5. 프로그램 종료"""

run = True #프로그램 실행중!!!

while run : #run 변수가 False 처리 될 때까지 반복
    # : 아래는 들여쓰기 4칸 정도 처리
    #들여쓰기를 진행하면 하위 실행문이다!!!
    print(menu) #콘솔창에 메뉴를 출력
    select = input("1~5번중에서 원하는 메뉴의 번호를 입력해주세요 :") #select 변수에 숫자(문자열)을 넣는다.
                   #키보드로 입력받는 곳 앞쪽에 출력 메세지
    if select == "1" : #키보드로 입력한 숫자가 1이면?
        print("학생 성적을 입력합니다.") #1일때 처리되는 부분
        sn = input("성적을 입력할 학생의 학번을 입력해주세요 :")
        name = input("성적을 입력할 학생의 이름을 입력해주세요 :")
        kor = input("국어 점수를 입력하세요 :")
        eng = input("영어 점수를 입력하세요 :")
        mat = input("수학 점수를 입력하세요 :")
        tot = int(kor) + int(eng) + int(mat)
        avg = round(tot/3,0)
        korgrade = None
        enggrade = None
        matgrade = None

        if int(kor) >= 90 :
            korgrade = "A"
        elif int(kor) >= 80 :
            korgrade = "B"
        elif int(kor) >= 70 :
            korgrade = "C"
        else:
            korgrade = "F"

        if int(eng) >= 90 :
            enggrade = "A"
        elif int(eng) >= 80 :
            enggrade = "B"
        elif int(eng) >= 70 :
            enggrade = "C"
        else:
            enggrade = "F"

        if int(mat) >= 90 :
            matgrade = "A"
        elif int(mat) >= 80 :
            matgrade = "B"
        elif int(mat) >= 70 :
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

        if input("저장하려면 y를 입력해주세요 :") == "y" : #저장시 y 입력
            sns.append(sn)
            names.append(name)
            kors.append(kor)
            engs.append(eng)
            mats.append(mat) #변수뒤에 s는 배열(리스트)라고 생각
                             #변수.append() 리스트 뒤에 값이 추가된다.
            tots.append(tot)
            avgs.append(avg)
            korgrades.append(korgrade)
            enggrades.append(enggrade)
            matgrades.append(matgrade)
            #미션 평균이 : 90 이상이면 A, 80 이상이면 B, 70 이상이면 C, 나머지는 F = grades


            print("저장을 완료했습니다.")


        else:
            print("저장을 취소합니다.\n처음부터 다시 입력하세요.")








    elif select == "2" : #키보드로 입력한 숫자가 2이면?
        print("학생의 성적을 출력합니다.") #2일때 처리되는 부분
        selc = input("전체 학생 성적 보기는 1번, 개인 학생 성적 보기는 2번을 입력해주세요 :")
        if selc == "1" :
            print("전체 학생 성적을 출력합니다.")
            for i in range(len(sns)) : #리스트의 처음부터 끝까지 반복용
                #          len(ses) -> sns 리스트의 길이를 가져옴 -> 5
                #    range(5) -> 0~5까지 증가
                #i in 5 -> i값에 0 반복 1 반복 2 반복 3 반복 4 반복 5 끝!
                #결론 : i값이 인덱스로 사용함
                #tot = kors[i] + engs[i] + mats[i] #주의, 애초에 비어있는 주소는 인지하지 못하니 tots[i]는 사용하면 안된다.
                #avg = tot/3
                print(f"""
===========================================
학번 : {sns[i]} 이름 : {names[i]}
국어 점수: {kors[i]:>3}점 등급 : {korgrades[i]}
영어 점수: {engs[i]:>3}점 등급 : {enggrades[i]}
수학 점수: {mats[i]:>3}점 등급 : {matgrades[i]}
총점: {tots[i]:>3}점  평균: {avgs[i]:2.0f}점
===========================================""")




        elif selc == "2" :
            print("개인 학생 성적을 출력합니다.")
            sn = input("학번을 입력해주세요 :")
            name = input("이름을 입력해주세요 :")
            if sn in sns :
                idx = sns.index(sn)
                if name == names[idx] :
                    print("해당 학생의 성적을 출력합니다.")
                    print(f"""
===========================================
학번 : {sns[idx]:}
이름 : {names[idx]}

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









    elif select == "3" : #키보드로 입력한 숫자가 3이면?
        print("학생 성적을 수정합니다.")

        #등록한 학생의 점수를 가져온다.
        #학번을 이용하여 학생을 찾는다.
        sn = input("수정할 학번 :")
        if sn in sns : #sns학번이 들어있는 리스트 in 안에 있는지 확인
            print("학번이 있습니다.")
            idx = sns.index(sn) #찾은 학번의 주소를 가져옴
            print(f"""
이름 : {names[idx]}
국어 : {kors[idx]}점 등급 : {korgrades[idx]}
영어 : {engs[idx]}점 등급 : {enggrades[idx]}
수학 : {mats[idx]}점 등급 : {matgrades[idx]}
""")
            kor = input("수정할 국어 점수 :")
            eng = input("수정할 영어 점수 :")
            mat = input("수정할 수학 점수 :")
            #미션 수정된 내용으로 총점, 평균을 다시 등록하기
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
이름 : {names[idx]}
국어 : {kor} 등급 : {korgrade}
영어 : {eng} 등급 : {enggrade}
수학 : {mat} 등급 : {matgrade}
총점 : {tot}
평균 : {avg}
""")

            if input("정말로 수정하시겠습니까? (y/n) :") == "y" :
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

        #등록된 학생의 점수를 수정한다.

        #수정된 값을 기준으로 총점과 평균과 등급을 다시 등록한다.


    elif select == "4" : #키보드로 입력한 숫자가 4이면?
        print("학생 성적을 삭제합니다.")
        sn = input("삭제할 학번 :")

        if sn in sns :
            idx = sns.index(sn)
            print(f"{names[idx]} 학생의 정보를 삭제합니다.")

            if input("정말로 삭제할까요? (y/n") == "Y" :
                sns.pop(idx)
                names.pop(idx)
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


    elif select == "5" : #키보드로 입력한 숫자가 5이면?
        print("프로그램을 종료합니다.")
        run = False #while문을 종료하여 프로그램이 꺼진다.


    else: #1~5까지 값 이외의 문자가 들어오면 처리용
         print("1~5값만 허용합니다.")