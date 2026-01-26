import json
import os
from Member2 import Member2




class MemberService2:

    def __init__(self):
        self.file_name = "members2.txt"
        self.members = {}
        self.session = None
        self.load_member()


    def save_member(self):

        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.members, f, ensure_ascii=False)


    def load_member(self):

        if not os.path.exists(self.file_name):
            self.save_member()
            return

        with open(self.file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            for key in data.keys():
                self.members[key] = Member2.from_line(data[key])

    def add_member(self):
        print("회원가입")
        uid = input("아이디 :")
        member = self.find_member(uid)
    #
    # def find_member(self,uid):
    #     for member in self.members:
    #         for user in member:
    #





