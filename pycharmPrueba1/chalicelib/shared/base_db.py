class BaseDbMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BaseDb(metaclass=BaseDbMeta):

    def __init__(self) -> None:
        # Aqui iria la config de boto3
        # dynamodb = boto3.resource("dynamodb")
        pass

    def get_table(self, tableName: str):
        # return self.dynamodb.Table("{tablename}")
        pass



