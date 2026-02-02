class Board:
    def __init__(self, id, member_id, title, content, active = True, writer_name =None, writer_id = None):
        self.id = id
        self.member_id = member_id
        self.title = title
        self.content = content
        self.active = active
        self.writer_name = writer_name
        self.writer_id = writer_id


    @classmethod
    def from_db(cls,row:dict):
        if not row:
            return None
        return cls(
            id = row['id'],
            member_id = row['member_id'],
            title = row['title'],
            content = row['content'],
            active = row['active'], # 아직 미구현
            writer_name = row['writer_name'],
            writer_id = row['writer_id'],
        )

    def __str__(self):
        writer = self.writer_name if self.writer_name else f"ID:{self.member_id}"
        return f"{self.id:<4} | {self.title:<20} | {writer}"
