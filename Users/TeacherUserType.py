from .User import User


class TeacherUserType(User):
    def __init__(self, user_id: int, name: str) -> None:
        super().__init__(user_id, name)

    def borrow_limit(self) -> int:
        return 5
