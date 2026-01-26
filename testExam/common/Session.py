class Session:

    login_member = None


    @classmethod
    def login(cls,member):
        """
        MemberService()의 member_add() 메서드가 완료되는 시점에 호출된다.
        클래스 객체를 생성 -> cls.login_member
        """
        cls.login_member = member

    @classmethod
    def is_login(cls):
        """
        현재 로그인된 상태인지 검증하는 메서드
        비로그인 > False
        로그인 > 로그인 한 유저의 객체
        """
        if cls.login_member == None:
            return False

        else:
            return cls.login_member

    @classmethod
    def logout(cls):
        """
        로그아웃 전용 메서드. None값이 로그아웃 상태이다
        """
        cls.login_member = None

    @classmethod
    def is_admin(cls):
        """
        로그인 한 유저의 role (등급)이 admin인지 검증하는 메서드
        admin일 시 True
        아닐 시 False
        """
        if cls.login_member.role == "admin":
            return True
        else:
            return False