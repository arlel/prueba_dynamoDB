import datetime
import json

from ..domain.user_entity import User, UserSchema


class UserDBMockup:
    temp = User("1999-1-1", "Juan", "Juarez", "juan@mail.com", "Hudston", 1)
    user1 = temp.__dict__
    temp = User("2000-2-22", "John", "Smith", "John@mail.com", "Texas", 2)
    user2 = temp.__dict__

    def scan(self):
        return {"Items": [self.user1, self.user2], "Count": 2,
                "ScannedCount": 2, "ConsumedCapacity": None}

    def get_item(self, Key, *args):
        if Key.get("id") == 1:
            return {"Item": self.user1}
        else:
            return {"Item": self.user2}
