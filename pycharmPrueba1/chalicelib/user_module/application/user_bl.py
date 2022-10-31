from chalice import NotFoundError, BadRequestError

from ..domain.user_entity import User, UserSchema
from ..framework.user_repository import UserRepository


class UserBL:
    repository: UserRepository
    UserSchema: UserSchema

    def __init__(self, repo: UserRepository, userSchema: UserSchema):
        self.repository = repo
        self.userSchema = userSchema

    def create(self, data: dict):
        if "_id" in data.keys():
            data.pop('_id')
        user = self.userSchema.load(data)
        return self.userSchema.dump(user)

    def update(self, data: dict, _id: int):
        if "_id" in data.keys():
            data.pop('_id')
        if _id == 1 or _id == 2:
            user = self.userSchema.load(data)
            user._id = _id
            return self.userSchema.dump(user)
        raise NotFoundError

    def get_users(self) -> list:
        users: list = self.userSchema.load(self.repository.get_all_users(), many=True)
        return self.userSchema.dump(users, many=True)

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

    def delete(self, key: int):
        # self.repository.remove(key)
        return self.get_user(key)
