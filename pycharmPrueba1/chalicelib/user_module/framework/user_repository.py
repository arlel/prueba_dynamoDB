from .user_db_mockup import UserDBMockup
from ...global_dependencies import baseDb
from chalice import NotFoundError
from boto3.dynamodb.types import TypeSerializer
from botocore.exceptions import ClientError


class UserRepository:
    table = baseDb.get_table("User")
    # table = UserDBMockup()

    def get_all_users(self):
        try:
            response = self.table.scan()
            return response.get("Items", None)
        except:
            raise NotFoundError("Empty table")

    # Get with partition key (only created with this key)
    def get_user(self, key):
        response = self.table.get_item(Key={"id": key})
        if "Item" in response.keys():
            return response.get("Item")
        raise NotFoundError("Not found")

    """
    to get_item on a table created with sort and partition key
    resp = table.get_item(
    Key={
        'id': 1  #Partition Key
        'name': "XYZ" #Sort Key
    },)
    """

    def put_user(self, item):
        try:
            response = self.table.put_item(Item=item)
        except ClientError as err:
            raise err
        else:
            return response

    def delete(self, key):
        response = self.table.delete_item(
            Key={"id": key},
            ReturnValues="ALL_OLD",
            ReturnConsumedCapacity="NONE",
            ReturnItemCollectionMetrics='NONE'
        )
        if "Attributes" in response.keys():
            return response.get("Attributes")
        raise NotFoundError("Not found")

    def update(self, key, user_dict):
        update_expression = 'SET {}'.format(','.join(f'#{k}=:{k}' for k in user_dict))
        expression_attribute_values = {f':{k}': v for k, v in user_dict.items()}
        expression_attribute_names = {f'#{k}': k for k in user_dict}
        if self.get_user(key):
            response = self.table.update_item(
                Key={"id": key},
                ReturnValues="ALL_NEW",
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ExpressionAttributeNames=expression_attribute_names
            )
            if "Attributes" in response.keys():
                return response.get("Attributes")
        raise NotFoundError("Not found")
