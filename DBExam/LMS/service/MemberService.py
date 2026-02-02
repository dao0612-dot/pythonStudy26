from textwrap import dedent


from LMS.common import *
from LMS.domain import *

class MemberService:

    @classmethod
    def load(cls): # 이전과 다르게 처음에 몇명인지 알려주는 용도기에 정보를 갱신할 순 없다.
                   # 즉, 수정사항이 있으면 Session.login_member에도 따로 적용해줘야한다.

        conn = Session.get_connection() # 메서드가 db를 딕셔너리로 가져오게끔 만들었었음.
        try:
            with conn.cursor() as cursor:
                cursor.execute('select count(*) as cnt from members')
                count = cursor.fetchone()['cnt'] #fetchone는 다음 행 '1개'를 가져온다
                                                 #fetchall은 행 전부를 가져온다.
                                                 #fetchmany는 최대치를 정해서 가져온다.

                print(f"시스템에 등록된 회원의 수는 {count}명 입니다.")

        except:
            print("MemberService.load()에 오류가 발생했습니다.")

        finally:
            conn.close()



    @classmethod
    def login(cls):

        if Session.is_login():
            print("이미 로그인 되어있습니다.")
            return

        uid = input("아이디 :")
        pw = input("비밀번호 :")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "select * from members where uid = %s and password = %s"
                cursor.execute(sql, (uid,pw))
                row = cursor.fetchone() # 아이디와 비번이 동일한 계정은 딱 하나. 즉, row에 들어갈 값이 sql에서
                                        # 통과된 1개의 행이므로 fetchone이 자연스럽다.
                                        # 만약 통과된 답이 없다면 None을 반환

                if row : #그래서 row가 값이 있다면, 통과했다는 True이니 이 문구를 사용.
                    member = Member.from_db(row) # row는 위 엑스큐트문구를 통과한 1개의 행.
                                                 # 그걸 from_db에 넣고 돌려 객체로 만든다.
                                                 # member 변수에 넣어서 주소 연결(cls)

                    if not member.active:
                        print("비활성화 계정입니다.")
                        return

                    Session.login(member)
                    print(f"로그인 성공\n{member.name}님 환영합니다.\n[{member.role}]")


        except:
            print("MemberService.login()에서 오류가 발생했습니다.")

        finally:
            conn.close()


    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인이 필요한 서비스입니다.")
            return

        if input("정말로 로그아웃 하시겠습니까? (y/n) :") == "y" :

            Session.logout()
            print("로그아웃을 완료했습니다. 안녕히가세요.")

        else:
            print("로그아웃을 취소합니다.")


    @classmethod
    def signup(cls):

        new_uid = input("아이디 :")


        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "select * from members where uid = %s"
                cursor.execute(sql, (new_uid,)) # execute에 들어갈 땐 무조건 튜플로!!!!!!
                row = cursor.fetchone()
                if row:
                    print("이미 존재하는 회원입니다.")
                    return

                new_pw = input("비밀번호 :")
                new_name = input("이름 :")

                if input(dedent(f"""
                해당 내용으로 회원가입을 완료하시겠습니까?
                이름 : {new_name}
                아이디 : {new_uid}
                비밀번호 : {new_pw}
                권한 : user
                
                """)) == "y":
                    add = "insert into members (uid, password, name) values (%s, %s, %s)"
                    cursor.execute(add, (new_uid, new_pw, new_name))
                    conn.commit() # 추가, 수정 정보가 발생하면 반드시 commit()
                    print("회원가입이 완료되었습니다.")

                else:
                    print("회원가입을 취소했습니다.")

        except:
            print("MemberService.signup()에서 오류가 발생했습니다.")
            conn.rollback()

        finally:
            conn.close()




    @classmethod
    def modify(cls):

        # print(dedent(f"""
        # ------ 내 정보 ------
        # 이름 : {Session.login_member.name}
        # 아이디 : {Session.login_member.uid}
        # 비밀번호 : {Session.login_member.pw}
        # 권한 : {Session.login_member.role}
        # """))
        print("[내 정보 확인]")
        print(Session.login_member)

        member = Session.login_member

        modify_name = member.name
        modify_pw = member.pw

        sel = input("변경하실 정보를 선택해주세요\n1. 이름\n2. 비밀번호\n3. 회원탈퇴 또는 비활성화\n>>>")


        if sel == "1":
            modify_name = input("변경할 이름 :")

        elif sel == "2":
            modify_pw = input("변경할 pw :")

        elif sel == "3":
            cls.delete()

        else:
            print("잘못된 번호를 입력하셨습니다.")


        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if input(dedent(f"""
                    아래 내용으로 정보 변환을 완료하시겠습니까? 
                    이름 : {modify_name}
                    비밀번호 : {modify_pw}                                                    
                    (y/n)
                    """)) == "y" :
                    modify_result = "update members set name = %s, password = %s where uid = %s"
                    cursor.execute(modify_result, (modify_name, modify_pw,member.uid))
                    conn.commit()  # 수정, 추가 정보가 발생하면 반드시 commit()
                    print("회원정보 수정을 완료했습니다.")

                else:
                    print("회원정보 수정을 취소했습니다.")

        except:
            print("MemberService.modify()에서 오류가 발생했습니다.")
            conn.rollback()

        finally:
            conn.close()




    @classmethod
    def delete(cls):
        member = Session.login_member.name
        conn = Session.get_connection()

        sel = input("1. 회원탈퇴 / 2. 계정 비활성화")
        try:
            if sel == "1":
                if input(f"{member.name}님 정말로 회원탈퇴하시겠습니까? (y/n) :") == "y" :

                    with conn.cursor() as cursor:
                        sql = "delete from members where uid = %s"
                        cursor.execute(sql, (member.uid,))
                        conn.commit()
                        print("회원탈퇴를 완료했습니다. 다음에 다시 방문하시길 기대하겠습니다.")

                else:
                    print("회원 탈퇴를 취소했습니다.")

            elif sel == "2":
                if input(f"{member.name}님 정말로 계정을 비활성화 하시겠습니까? (y/n) :") == "y" :
                    with conn.cursor() as cursor:
                        sql = "update members set active where uid = %s"
                        cursor.execute(sql, (member.uid,))
                        conn.commit()
                        print("비활성화를 완료했습니다. 다음에 다시 방문하시길 기대하겠습니다.")

                else:
                    print("비활성화를 취소했습니다.")

        except:
            print("MemberService.delete()에서 오류가 발생했습니다.")

        finally:
            conn.close()







    @classmethod
    def admin_list(cls):
        conn = Session.get_connection()

        try:
            with conn.cursor() as cursor:
                sql = "select * from members"
                cursor.execute(sql)

                print("-" * 60)
                print("회원 정보 리스트")
                print("-" * 60)

                for row in cursor.fetchall() :
                    member = Member.from_db(row)
                    if member.active:
                        active = "활성"
                    else:
                        active = "비활성"
                    print(f"{member.id}. {member.name} | {member.uid} | {member.role} | {active}")


        except Exception as e:
            print("MemberService.admin_list()에서 오류가 발생했습니다.")
            print(f"{e}")
            conn.rollback()

        finally:
            conn.close()


    @classmethod
    def admin_modify(cls):

        conn = Session.get_connection()

        cls.admin_list()
        member_select = input("변경할 회원 번호 :")

        try:
            with conn.cursor() as cursor:
                sql = "select * from members where id = %s"
                cursor.execute(sql, (member_select,))
                row = cursor.fetchone()

                member = Member.from_db(row)
                admin_name = member.name
                admin_role = member.role

                if row:

                    sel = input("[변경할 정보]\n1. 이름\n2. 권한\n3. 활성/비활성\n>>>")

                    if sel == "1":
                        admin_name = input("변경할 이름 :")

                    elif sel == "2":
                        admin_role = input("변경할 권한 (admin / manager / user) :")
                        if not admin_role in ("admin", "manager", "user"):
                            print("지정된 권한명이 아닙니다.")
                            return

                    elif sel == "3":
                        active_sel = input("1. 활성화   2. 비활성화\n>>>")
                        if active_sel == "1":
                            active = "update members set active = true where uid = %s"
                            cursor.execute(active, (member.uid,))
                            conn.commit()

                        elif active_sel == "2":
                            active = "update members set active = false where uid = %s"
                            cursor.execute(active, (member.uid,))
                            conn.commit()

                        else:
                            print("잘못된 번호를 입력하셨습니다.")

                    else:
                        print("잘못된 번호를 입력하셨습니다.")


                    admin = "update members set name = %s, role = %s where uid = %s"

                    cursor.execute(admin, (admin_name, admin_role, member.uid))
                    conn.commit()
                    print("지정하신 회원의 정보 수정이 완료되었습니다.")

                else:
                    print("지정하신 회원이 존재하지 않습니다.")

        except Exception as e:
            print("MemberService.admin_modify()에서 오류가 발생했습니다.")
            print(f"{e}")

        finally:
            conn.close()




