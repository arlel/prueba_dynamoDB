from ..domain.user_entity import User
from ..framework.user_repository import UserRepository


class UserBL:
    repository: UserRepository

    def __init__(self, repo: UserRepository):
        self.repository = repo

    def get_users(self) -> list:
        return self.repository.get_all_users()
