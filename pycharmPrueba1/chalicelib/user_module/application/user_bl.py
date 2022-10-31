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
        if "id" in data.keys():
            data.pop('id')
        user = self.userSchema.load(data)
        # here we can put some validations
        self.repository.put_user(self.userSchema.dump(user))
        return self.userSchema.dumps(user)

    def update(self, data: dict, key: str):
        user = self.userSchema.load(data)
        user.id = key
        user_dict = self.userSchema.dump(user)
        user_dict.pop("id")
        self.repository.update(key, user_dict)
        return self.userSchema.dumps(user)

    def get_users(self) -> list:
        users: list = self.userSchema.load(self.repository.get_all_users(), many=True)
        return self.userSchema.dumps(users, many=True)

    def get_user(self, key: str):
        # Cargar de bd, llega un documento que representa al usuario
        dict_user = self.repository.get_user(key)
        # print(dict_user)
        # Convierto el diccionario a usuario, con loads convierto json a user
        user = self.userSchema.load(dict_user)
        # print(user)
        # Convierto el usuario a dict
        return self.userSchema.dumps(user)

    def delete(self, key: str):
        deleted_user = self.userSchema.load(self.repository.delete(key))
        return self.userSchema.dumps(deleted_user)
