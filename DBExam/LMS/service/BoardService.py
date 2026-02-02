from textwrap import dedent

from LMS.domain import Board
from LMS.common import Session

class BoardService:


    @classmethod
    def load(cls):
        conn = Session.get_connection()
        with conn.cursor() as cursor:
            sql = "SELECT count(*) as cnt FROM board"
            cursor.execute(sql)
            count = cursor.fetchone()['cnt']
            print(f"현재 존재하는 게시판은 {count}개입니다.")


    @classmethod
    def run(cls):
        cls.load()
        while True:
            pass


    @classmethod
    def board_list(cls):
        conn = Session.get_connection()
        with conn.cursor() as cursor:
            sql = """SELECT m.name, b.id, b.title, b.content FROM board"""
