class User:
    id: int
    name: str
    surname: str
    mail: str
    city: str

    def __init__(self, name: str, surname: str, mail: str, city: str):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.city = city
