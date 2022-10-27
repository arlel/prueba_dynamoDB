from .user_db_mockup import UserDBMockup
from ...global_dependencies import baseDb
from chalice import NotFoundError


class UserRepository:
    # table = baseDb.get_table("user")
    table = UserDBMockup()

    def get_all_users(self):
        try:
            response = self.table.scan()
            return response.get("Items", None)
        except:
            raise NotFoundError
