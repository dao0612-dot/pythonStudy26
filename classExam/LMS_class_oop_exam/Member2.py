


class Member2:
    def __init__(self, uid, pw, name, role = "user", active = True):
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active



    @classmethod
    def from_line(cls, line):
        uid, pw, name, role, active = line
        return cls(uid, pw, name, role, active == "True")
