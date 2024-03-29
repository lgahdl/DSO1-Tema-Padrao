# Utils
from datetime import date as Date

# Models
from api.model.Car import Car
from api.model.Request import Request
from api.model.User import User

# Views
from api.screen.Request_Screen import RequestScreen

# Controllers
from api.controller.General_Controller import GeneralController

# dao
from api.data.Request_DAO import RequestDAO


class RequestController(GeneralController):
    id_request = 0

    def __init__(self, main_controller):
        super().__init__()
        self.__main_controller = main_controller
        self.__requests = []
        self.__active_requests = []
        self.__request_dao = RequestDAO()
        self.create_screen()

    def create_screen(self):
        self.__request_screen = RequestScreen(self)

    def destroy_screen(self):
        if self.__request_screen is not None:
            del self.__request_screen

    def create_dependencies_by_list(self, dependencies_list: []):
        for encapsulated_request in dependencies_list:
            request = Request(
                encapsulated_request['id_request'],
                self.main_controller.get_user(encapsulated_request['user'], True),
                self.__main_controller.key_controller.get_key_by_car_plate(
                    encapsulated_request['key_car_plate']),
                encapsulated_request['created_date'],
                encapsulated_request['devolution_date'],
                encapsulated_request['accepted'],
                encapsulated_request['reason']
            )
            self.__requests.append(request)

    @property
    def request_screen(self):
        return self.__request_screen

    @property
    def requests(self):
        return self.__request_dao.get_all()

    @property
    def main_controller(self):
        return self.__main_controller

    @main_controller.setter
    def main_controller(self, main_controller):
        self.__main_controller = main_controller

    @request_screen.setter
    def request_screen(self, request_screen: RequestScreen):
        self.__request_screen = request_screen

    def add_request(self, car_plate: str):
        car = self.main_controller.car_controller.get_car_by_plate(car_plate)
        is_blocked = False
        key = self.main_controller.key_controller.get_key_by_car_plate(
            car_plate)
        if (self.main_controller.user.user_denied_requests >= 3):
            is_blocked = True
        if (self.main_controller.user.check_car_permission(car) and not is_blocked):
            print("Permissao Aceita")
            self.__request_dao.add(self.id_request,
                                   Request(self.id_request, self.main_controller.user, key, Date.today(), None, True,
                                           ''))
        elif (not is_blocked):
            self.main_controller.user.user_denied_requests += 1
            self.__request_dao.add(self.id_request,
                                   Request(self.id_request, self.main_controller.user, key,
                                           Date.today(), Date.today(), False,
                                           'O Usuário não tem permissão para esse veículo'))
            print("O Usuário não tem permissão para esse veiculo")
        elif (is_blocked):
            self.request_screen.show_is_blocked_message()
        self.id_request += 1

    def add_request_with_array(self, values):
        user = self.main_controller.get_user(int(values[0]), True)
        car = self.main_controller.car_controller.get_car_by_plate(
            values[1])
        is_blocked = False
        key = self.main_controller.key_controller.get_key_by_car_plate(
            values[1])
        if user.user_denied_requests >= 3:
            is_blocked = True
        if user.check_car_permission(car) and not is_blocked:
            print("Permissao Aceita")
            self.__request_dao.add(self.id_request,
                                   Request(self.id_request, user, key, Date.today(), None, True, ''))
        elif not is_blocked:
            user.user_denied_requests += 1
            self.__request_dao.add(self.id_request,
                                   Request(self.id_request, user, key,
                                           Date.today(), Date.today(), False,
                                           'O Usuário não tem permissão para esse veículo'))
            print("O Usuário não tem permissão para esse veiculo")
        elif is_blocked:
            print('here is_blocked')
            self.request_screen.show_is_blocked_message()
        self.id_request += 1

    def open(self):
        self.__request_screen.open_gui('menu')

    def delete_request(self, id_request: int):
        for REQUEST in self.__requests:
            if id_request == REQUEST.id_request:
                self.__request_dao.remove(REQUEST.id_request)
                return True
            else:
                return False

    def edit_request(self, request: Request, id_request: int):
        for REQUEST in self.__requests:
            if REQUEST.id_request == id_request:
                self.__request_dao.remove(REQUEST.id_request)
                self.__request_dao.add(REQUEST.id_request, REQUEST)

    def open_main_screen(self):
        self.__request_screen.close_gui()
        self.__main_controller.open_main_screen(True)

    def open_request_screen(self):
        self.__request_screen.open()

    def return_key(self, request: Request):
        for REQUEST in self.__requests:
            if request.id_request == REQUEST.id_request:
                new_request = Request(request.id_request, request.user,
                                      request.key, request.created_date, Date.today(), True, '')
                self.edit_request(new_request, request.id_request)
            else:
                return "ERROR 404 - Request not found"

    def get_unfinished_request_by_user(self, user: User):
        for REQUEST in self.__requests:
            if user == REQUEST.user and REQUEST.devolution_date == None:
                return REQUEST

    def get_request_by_id(self, id_request: int):
        for REQUEST in self.__requests:
            if id_request == REQUEST.id_request:
                return REQUEST
