
from itertools import count

from LMS.common import Session
from LMS.domain import Score

class ScoreService:


    @classmethod
    def load(cls):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute('select count(*) as cnt from scores')
                count = cursor.fetchone()['cnt']
                print(f"현재 생성된 성적의 갯수는 {count}개 입니다.")

        except:
            print("ScoreService.load() 오류 발생")

        finally:
            conn.close()


    @classmethod
    def run(cls):

        cls.load()
        while True:
            print("====== 학생 성적관리 시스템 ======")


            number_count = count(1)
            for number, menu in enumerate(("성적 입력/수정", "내 성적 보기", "전체 성적 보기")):
                if Session.login_member.role == "admin":
                    print(f"{number+1}. {menu}")
                else:
                    if not number in (0,2):
                        print(f"{next(number_count)}. {menu}")

            print("0. 성적관리 시스템 종료")

            sel = input(">>>")

            if sel == "1" and Session.login_member.role == "admin":
                ScoreService.add_score()

            elif sel == "1" :
                ScoreService.view_my_score()

            elif sel == "2" and Session.login_member.role == "admin":
                ScoreService.view_my_score()

            elif sel == "3" and Session.login_member.role == "admin":
                ScoreService.view_all()

            elif sel == "0":
                break

            else:
                print("잘못된 숫자를 입력하셨습니다.")

    @classmethod
    def add_score(cls):
        conn = Session.get_connection()
        sel = input("성적 입력/처리할 학생 uid :")
        try:
            with conn.cursor() as cursor:
                cursor.execute("""select m.id, s.korean 
                                from members m left join scores s on s.member_id = m.id
                                where m.uid = %s""",(sel,))
                member = cursor.fetchone()


                if not member:
                    print("존재하지 않는 학생입니다.")
                    return

                kor = input("국어 :")
                eng = input("영어 :")
                math = input("수학 :")

                temp_score = Score(member['id'], kor = kor, eng = eng, math = math)
                if not member['korean']:
                    print("성적을 입력합니다.")
                    sql = """
                    insert into scores
                    (member_id, korean, english, math, total,average,grade)
                    values (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql,(
                    member['id'],kor,eng,math,
                    temp_score.total,temp_score.avg,temp_score.grade))

                else:
                    print("성적을 수정합니다.")
                    sql = """
                    update scores set
                    korean = %s, english = %s, math = %s,
                    total = %s, average = %s, grade = %s
                    where member_id = %s
                    """
                    cursor.execute(sql,(
                    kor,eng,math,
                    temp_score.total,temp_score.avg,temp_score.grade, member['id']))

        finally:
            conn.commit()
            conn.close()




    @classmethod
    def view_my_score(cls):
        conn = Session.get_connection()
        member = Session.login_member
        try:
            with conn.cursor() as cursor:
                cursor.execute("""select m.name, s.*
                                from scores s join members m on s.member_id = m.id
                                where s.member_id = %s
                                """,(member.id,))
                data = cursor.fetchone()
                cls.print_score(data,data['name'])

        finally:
            conn.close()

    @classmethod
    def view_all(cls):
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""select s.*,m.name
                               from scores s
                               join members m on s.member_id = m.id
                               order by s.id desc
                               """)

                datas = cursor.fetchall()
                print("=" * 60)
                for data in datas :
                    cls.print_score(data,data['name'])


                print("=" * 60)

        finally:
            conn.close()


    @staticmethod
    def print_score(s, display_uid):
        if not s:
            print("등록된 성적이 없습니다.")
            return

        print("-" * 60)
        print(f"{s['id']} | {display_uid:5} | 국어: {s['korean']:<5} | 영어: {s['english']:<5} | 수학: {s['math']:<5}")
        print(f"총점: {s['total']:<5} 평균: {s['average']:<5} 등급: {s['grade']:<5}")






