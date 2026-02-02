

class Member:
    def __init__(self, id, uid, pw, name, role = 'user', active = True):
        self.id = id
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active


    @classmethod
    def from_db(cls, row): # row는 1개의 '딕셔너리 행'을 의미한다.
                           # Session.get_connection()에서 '딕셔너리'로 전부 가져오도록 설계함
        if not row: #row가 None이라면(False라면)
            return None

        return cls(
            id = row.get('id'),
            uid = row.get('uid'),
            pw = row.get('password'),
            name = row.get('name'),
            role = row.get('role'),
            active = bool(row.get('active'))

        )


    def is_admin(self):
        return self.role == 'admin'

    def __str__(self):
        return f'{self.name}({self.uid}:{self.pw})[{self.role}]'