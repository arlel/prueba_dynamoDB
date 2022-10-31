from datetime import date

from marshmallow import Schema, fields, post_load, validates, ValidationError
import random


class User:
    _id: int
    name: str
    surname: str
    mail: str
    city: str
    bDate: str

    def __init__(self, bDate: str, name: str, surname: str, mail: str, city: str, _id: int = None):
        self.bDate = bDate
        # TODO: UUID
        self._id = _id or int(random.randint(1, 10))
        self.name = name
        self.surname = surname
        self.mail = mail
        self.city = city


class UserSchema(Schema):
    _id = fields.Integer()
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


