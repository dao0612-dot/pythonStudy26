class Member:

    def __init__(self, uid, pw, name, role = "user", active = True):
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active


    def to_line(self):
        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}\n"




    @classmethod
    def from_line(cls, line):
        uid, pw, name, role, active = line.strip().split("|")
        return cls(uid, pw, name, role, active == "True")


