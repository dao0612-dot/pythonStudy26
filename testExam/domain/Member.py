class Member:



    def __init__(self, uid, pw, name, role = "user", active = True):
        """
        __init__() 메서드로 초기값 변수 세팅

        매게변수 중 role, active는 인수가 없어도 세팅될 수 있도록
        미리 초기값을 지정해둔다.
        """
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active



    def to_line(self):
        """
        인스턴스 객체명.to_line() 으로 메서드 호출 시 등장

        인스턴스 객체에 지정된 변수들(uid,pw,name,role,active)
        을 규격화된 문자열로 만들고 그 값을 챙겨서 메서드를 빠져나간다.
        """

        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}\n"



    @classmethod
    def from_line(cls, line):
        """
        클래스명.from_line(인수) 으로 메서드 호출 시 등장

        클래스 객체를 생성하는 매서드로, line 매게변수에 담기는 인수는
        각각 uid, pw, name, role, active의 위치에 해당되도록 들어오기 때문에
        튜플을 한번에 변수 여러개에 넣는 것 처럼 똑같이 할 수 있다.
        그리고 그 변수들을 cls()로 묶어서 클래스 객체로 생성 후
        그 값을 가지고 메서드를 빠져나간다.

        active == "True"의 경우, 텍스트 파일에서 읽어내 가져온 것은 문자열이기 떼문에
        active가 문자열 "True"일 경우 불타입 True가 들어가도록 배치한 것이다.
        """
        uid, pw, name, role, active = line.strip().split("|")
        return cls(uid, pw, name, role, active == "True")


