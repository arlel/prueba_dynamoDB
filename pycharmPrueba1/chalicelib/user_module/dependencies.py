from .application.user_bl import UserBL
from .domain.user_entity import UserSchema
from .framework.user_repository import UserRepository

user_schema: UserSchema = UserSchema()
user_repository: UserRepository = UserRepository()
user_bl: UserBL = UserBL(user_repository,user_schema)


