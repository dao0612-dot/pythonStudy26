class Score:
    def __init__(self, member_id, kor, eng, math):
        self.member_id = member_id
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)



    @property
    def total(self):
        return self.kor + self.eng + self.math


    @property
    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    @property
    def grade(self):
        avg = self.avg
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        else:
            return 'F'

    @classmethod
    def from_db(cls,row:dict):
        if not row:
            return None

        return cls(
            id = row.get('id'),
            member_id = row.get('member_id'),
            kor = row.get('kor'),
            eng = row.get('eng'),
            math = row.get('math')
        )
