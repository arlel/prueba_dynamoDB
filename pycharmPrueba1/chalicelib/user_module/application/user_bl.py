from chalice import NotFoundError

from ..domain.user_entity import User
from ..framework.user_repository import UserRepository


class UserBL:
    repository: UserRepository

    def __init__(self, repo: UserRepository):
        self.repository = repo

    def get_users(self) -> list:
        return self.repository.get_all_users()

    def get_user(self, key: int):
        if key < 1 or key > 2:
            raise NotFoundError(f"not founded user with id {key}")
        return self.repository.get_user(key)
