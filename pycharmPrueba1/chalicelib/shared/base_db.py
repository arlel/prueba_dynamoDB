import boto3


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
        self.dynamoDB_cli = boto3.client("dynamodb", endpoint_url="http://localhost:8000")
        self.dynamoDB_res = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
        # response = dynamoDB.list_tables()
        # print(response)

    def get_table(self, tableName: str):
        return self.dynamoDB_res.Table(tableName)









