from datetime import date

from marshmallow import Schema, fields, post_load, validates, ValidationError
import random


class User:
    _id: int
    name: str
    surname: str
    mail: str
    city: str
    bDate: date

    def __init__(self, bdate: date, name: str, surname: str, mail: str, city: str, _id: int =None):
        self.bDate=bdate
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
    def validate_bDate(self,value: date):
        if value.year < date.year(1900):
            raise ValidationError("year too lower to be real")
        if value.year > date.year((date.today()).year - date.year(16)):
            raise ValidationError("Too young")


