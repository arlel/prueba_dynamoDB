from .application.user_bl import UserBL
from .framework.user_repository import UserRepository

user_repository: UserRepository = UserRepository()
user_bl: UserBL = UserBL(user_repository)

