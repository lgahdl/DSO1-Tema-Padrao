# Utils
from datetime import date as Date

# Models
from ..model.Car import Car
from ..model.Request import Request
from ..model.User import User

# Views
from ..screen.Request_Screen import RequestScreen

# Controllers
from ..controller.General_Controller import GeneralController


class RequestController(GeneralController):
    id_request = 0

    def __init__(self, request_screen: RequestScreen, general_controller: GeneralController):
        self.__request_screen = request_screen
        self.__general_controller = general_controller
        self.__requests = []

    @property
    def request_screen(self):
        return self.__request_screen

    @property
    def general_controller(self):
        return self.__general_controller

    @property
    def requests(self):
        return self.__requests

    @request_screen.setter
    def request_screen(self, request_screen: RequestScreen):
        self.__request_screen = request_screen

    @general_controller.setter
    def general_controller(self, general_controller: GeneralController):
        self.__general_controller = general_controller

    def add_request(self, user: User, car: Car):
        if user.check_car_permission(car):
            self.__requests.append(Request(self.id_request, user, car.key, Date.today(), None, True, ''))
        else:
            self.__requests.append(Request(self.id_request, user, car.key,
                                           Date.today(), Date.today(), False,
                                           'O Usuário não tem permissão para esse veículo'))

    def delete_request(self, request: Request):
        for REQUEST in self.__requests:
            if (request == REQUEST):
                self.__requests.remove(REQUEST)

    def edit_request(self, request: Request, id_request: int):
        for REQUEST in self.__requests:
            if (REQUEST.id_request == id_request):
                REQUEST = request

    def open_main_screen(self):
        self.__main_controller.open_main_screen()

    def open_request_screen(self):
        self.__request_screen.open()
