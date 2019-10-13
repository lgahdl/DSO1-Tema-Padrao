from ..model import General_Model
from datetime import date as Date


class User(General_Model):

    def __init__(self, \
                 id_user: int, \
                 user_name: str, \
                 user_birthday: Date, \
                 user_role: str, \
                 user_phone: int, \
                 cars: []):
        self.__id_user = id_user
        self.__user_name = user_name
        self.__user_birthday = user_birthday
        self.__user_role = user_role
        self.__user_phone = user_phone
        self.__cars = cars

    @property
    def id(self):
        return self.__id_user

    @property
    def user_name(self):
        return self.__user_name

    @property
    def user_birthday(self):
        return self.__user_birthday

    @property
    def user_role(self):
        return self.__user_role

    @property
    def user_phone(self):
        return self.__user_phone

    @property
    def cars(self):
        return self.__cars

    @id.setter
    def id(self, id_user: int):
        self.__id_user = id_user

    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name

    @user_birthday.setter
    def user_birthday(self, user_birthday: str):
        self.__user_birthday = user_birthday

    @user_role.setter
    def user_role(self, user_role: str):
        self.__user_role = user_role

    @user_phone.setter
    def user_phone(self, user_phone: str):
        self.__user_phone = user_phone

    @cars.setter
    def cars(self, cars: str):
        self.__cars = cars

    def check_car_permission(self, car: Car):
        pass
