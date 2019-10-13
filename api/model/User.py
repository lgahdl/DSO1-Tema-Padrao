# Utils
from datetime import date as Date

# Models
from ..model.General_Model import GeneralModel
from ..model.Car import Car


class User(GeneralModel):

    permission_role = {
        3: 'CEO',
        2: 'Manager',
        1: 'Employee',
        0: 'Trainee'
    }

    def __init__(self, \
                 id_user: int, \
                 user_name: str, \
                 user_birthday: Date, \
                 user_role: int, \
                 user_phone: int, \
                 cars: []):
        super().__init__()
        self.__id_user = id_user
        self.__user_name = user_name
        self.__user_birthday = user_birthday
        self.__user_role = self.permission_role[user_role]
        self.__user_phone = user_phone
        self.__cars = cars

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

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

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

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
        if self.__user_role == self.permission_role[0]:
            return True
        else:
            tier = car.car_tier
            if tier >= 0:
                return True
            else:
                able_to_request = False
                for key in self.permission_role:
                    permission = self.permission_role[key]
                    if permission == self.user_role:
                        able_to_request = tier > key
                return not able_to_request
