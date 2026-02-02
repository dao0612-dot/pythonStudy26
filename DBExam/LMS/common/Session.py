import pymysql

class Session:
    login_member = None

    @classmethod
    def get_connection(cls):

        return  pymysql.connect(
            host = 'localhost',
            user = 'mbc',
            password = '1234',
            db = 'lms',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
            #딕셔너리 타입으로 가져온다.
        )

    @classmethod
    def login(cls, member):
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None

    @classmethod
    def is_login(cls):
        return cls.login_member is not None

    @classmethod
    def is_admin(cls):
        return cls.is_login() and cls.login_member.role == 'admin'

