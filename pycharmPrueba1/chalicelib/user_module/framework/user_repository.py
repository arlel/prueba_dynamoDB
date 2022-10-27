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

    # Get with partition key (only created with this key)
    def get_user(self, key):
        response = self.table.get_item(Key={"id": 1},)
        return response.get("Item")

    """
    to get_item on a table created with sort and partition key
    resp = table.get_item(
    Key={
        'id': 1  #Partition Key
        'name': "XYZ" #Sort Key
    },)
    """