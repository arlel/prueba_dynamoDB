from chalice import NotFoundError

from ..domain.user_entity import User, UserSchema
from ..framework.user_repository import UserRepository


class UserBL:
    repository: UserRepository
    UserSchema: UserSchema

    def __init__(self, repo: UserRepository, userSchema: UserSchema):
        self.repository = repo
        self.userSchema = userSchema

    def create(self, data: dict):
        try:
            data.pop('_id')
        finally:
            user = self.userSchema.load(data)
            print(user)
            return self.userSchema.dump(user)

    def get_users(self) -> list:
        return self.repository.get_all_users()

    def get_user(self, key: int):
        if key < 1 or key > 2:
            raise NotFoundError(f"not founded user with id {key}")
        # Cargar de bd, llega un documento que representa al usuario
        dict_user = self.repository.get_user(key)
        # print(dict_user)
        # Convierto el diccionario a usuario, con loads convierto json a user
        user = self.userSchema.load(dict_user)
        # print(user)
        # Convierto el usuario a dict
        return self.userSchema.dump(user)
