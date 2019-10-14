from api.screen.Main_Screen import MainScreen
from api.controller.User_Controller import UserController
from api.controller.Request_Controller import RequestController
from api.controller.Car_Controller import CarController
from api.controller.General_Controller import GeneralController
from api.data import data


class MainController(GeneralController):

    def __init__(self):
        super().__init__()
        self.__user = None
        self.create_screen()
        self.__user_controller = UserController(self)
        self.__request_controller = RequestController(self)
        self.__car_controller = CarController(self)
        self.create_data()

    def create_data(self):
        users = data.users
        self.user_controller.create_dependencies_by_list(users)
        cars = data.cars
        self.car_controller.create_dependencies_by_list(cars)
        keys = data.keys
        requests = data.requests

    def create_dependencies_by_list(self, dependencies_list: []):
        pass

    def create_screen(self):
        self.__main_screen = MainScreen(self)

    def destroy_screen(self):
        if self.__main_screen is not None:
            del self.__main_screen

    @property
    def main_screen(self):
        return self.__main_screen

    @property
    def user_controller(self):
        return self.__user_controller

    @property
    def request_controller(self):
        return self.__request_controller

    @property
    def car_controller(self):
        return self.__car_controller

    @property
    def user(self):
        return self.__user

    @main_screen.setter
    def main_screen(self, main_screen: MainScreen):
        self.__main_screen = main_screen

    @user_controller.setter
    def user_controller(self, user_controller: UserController):
        self.__user_controller = user_controller

    @request_controller.setter
    def request_controller(self, request_controller: RequestController):
        self.__request_controller = request_controller

    @car_controller.setter
    def car_controller(self, car_controller):
        self.__car_controller = car_controller

    @user.setter
    def user(self, user):
        self.__user = user

    def open_main_screen(self):
        self.main_screen.open()

    def open_request_controller(self):
        self.request_controller.open()

    def open_user_controller(self):
        self.user_controller.open_user_screen()

    def open_key_controller(self):
        self.key_controller.open()

    def open_car_controller(self):
        self.car_controller.open()

    def get_user(self, id_user: int):
        self.__user = self.user_controller.get_user_by_id(id_user)
        if(self.__user):
            return True
        else:
            return False
