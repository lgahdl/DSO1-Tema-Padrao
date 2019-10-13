# Views
from ..screen.General_Screen import GeneralScreen

# Models
from ..controller.Request_Controller import RequestController


class RequestScreen(GeneralScreen):

    def __init__(self, request_controller: RequestController):
        self.__request_controller = super().__init__(request_controller)

    @property
    def request_controller(self):
        return self.__request_controller

    @request_controller.setter
    def request_controller(self, request_controller):
        self.__request_controller = request_controller

    def add(self, user, car):
        self.__request_controller.add_request(user, car)

    def edit(self, request, id_request):
        self.__request_controller.edit_request(request, id_request)

    def delete(self, request):
        self.__request_controller.delete_request(request)

    def open_main_screen(self):
        self.__request_controller.open_main_screen()
