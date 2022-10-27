class User:
    id: int
    name: str
    surname: str
    mail: str
    city: str

    def __init__(self, id:int,  name: str, surname: str, mail: str, city: str):
        self.id =id
        self.name = name
        self.surname = surname
        self.mail = mail
        self.city = city
