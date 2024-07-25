from .User import User


class StudentUserType(User):
    def __init__(self, user_id: int, name: str, user_type: str) -> None:
        super().__init__(user_id, name, user_type)

    def borrow_limit(self) -> int:
        return 1
