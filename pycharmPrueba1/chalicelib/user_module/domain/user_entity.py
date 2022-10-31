import uuid
from datetime import date
from marshmallow import Schema, fields, post_load, validates, ValidationError


class User:
    id: int
    name: str
    surname: str
    mail: str
    city: str
    bDate: str

    def __init__(self, bDate: str, name: str, surname: str, mail: str, city: str, id: str = None):
        self.bDate = bDate
        self.id = id or uuid.uuid4().hex.upper().replace("-", "")
        self.name = name
        self.surname = surname
        self.mail = mail
        self.city = city


class UserSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    mail = fields.Email()
    city = fields.Str()
    bDate = fields.Date()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

    @validates("bDate")
    def validate_bdate(self, value: date):
        if value.year < 1990:
            raise ValidationError("year too lower to be real")
        if value.year > (date.today().year - 16):
            raise ValidationError("Too young")


