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
from ..controller.Main_Controller import MainController


class RequestController(GeneralController):
    id_request = 0

    def __init__(self, request_screen: RequestScreen, general_controller: GeneralController, main_controller: MainController):
        self.__request_screen = request_screen
        self.__general_controller = general_controller
        self.__main_controller = main_controller

        self.__requests = []
        self.__active_requests = []

    @property
    def request_screen(self):
        return self.__request_screen

    @property
    def general_controller(self):
        return self.__general_controller

    @property
    def requests(self):
        return self.__requests

    @property
    def main_controller(self):
      return self.__main_controller

    @main_controller.setter
    def main_controller(self, main_controller: MainController):
      self.__main_controller = main_controller

    @request_screen.setter
    def request_screen(self, request_screen: RequestScreen):
        self.__request_screen = request_screen

    @general_controller.setter
    def general_controller(self, general_controller: GeneralController):
        self.__general_controller = general_controller

    def add_request(self, car_plate: str):
        user_denied_requests = 0
        car = self.main_controller.car_controller.get_car(car_plate)
        is_blocked = False
        for request in self.requests:
            if(request.user == self.main_controller.user and request.accepted == False and request.car == car):
                user_denied_requests += 1
        if (user_denied_requests >= 3):
            is_blocked = True
        if (self.main_controller.user.check_car_permission(car_plate) and not is_blocked):
            self.__requests.append(Request(self.id_request, self.main_controller.user, car.key, Date.today(), None, True, ''))
        elif(not is_blocked):
            self.__requests.append(Request(self.id_request, self.main_controller.user, car.key,
                                           Date.today(), Date.today(), False,
                                           'O Usuário não tem permissão para esse veículo'))
        elif(is_blocked):
            self.request_screen.show_is_blocked_message()

    def open(self):
      self.__request_screen.open()

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
