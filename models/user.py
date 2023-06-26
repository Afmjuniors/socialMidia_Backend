from datetime import date
from uteis.helper import date_para_str
from uteis.helper import str_para_date


class User:
    def __init__(self: object,
                 id_user: int,
                 type_user: str,
                 name: str,
                 email: str,
                 date_birth: str,
                 created_date: str,
                 password: str):
        self.__id: int = id_user
        self.__name: str = name
        self.__email: str = email
        self.__type_user: str = type_user
        self.__password: str = password
        self.__date_birth: date = date_birth
        self.__created_date: date = created_date

    def __str__(self: object) -> str:
        return f'ID: {self.id} \nNome: {self.name} \nEmail: {self.email} \nTipo de Usuario: {self.type_user} \nData ' \
               f'de Nascimento: {date_para_str(self.date_birth)}'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'type_user': self.type_user,
            'date_birth': str(self.date_birth),
            'created_date': str(self.created_date)
        }

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def password(self: object) -> str:
        return self.__password

    @password.setter
    def password(self: object, password: str) -> None:
        self.password = password

    @property
    def date_birth(self: object) -> date:
        return self.__date_birth

    @property
    def type_user(self: object) -> str:
        return self.__type_user

    @type_user.setter
    def password(self: object, type_user: str) -> None:
        self.type_user = type_user

    @property
    def created_date(self: object) -> date:
        return self.__created_date
