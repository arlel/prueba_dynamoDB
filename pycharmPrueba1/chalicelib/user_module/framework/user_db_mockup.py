import json

from ..domain.user_entity import User


class UserDBMockup:
    temp = User(1, "Juan", "Juarez", "juan@mail.com", "Hudston")
    user1 = temp.__dict__
    temp = User(2, "John", "Smith", "John@mail.com", "Texas")
    user2 = temp.__dict__

    def scan(self):
        return {"Items": [self.user1, self.user2], "Count": 2,
                "ScannedCount": 2, "ConsumedCapacity": None}

    def get_item(self, Key, *args):
        if Key.get("id") == 1:
            return {"Item": self.user1}
        else:
            return {"Item": self.user2}
