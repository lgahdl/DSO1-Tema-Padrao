# Views
from ..screen.General_Screen import GeneralScreen

#Controller
from api.controller.Main_Controller import MainController


class MainScreen(GeneralScreen):

    def __init__(self, main_controller: MainController):
        super().__init__(main_controller)

    def open(self):
        id_user = input('Olá, por favor, digite sua Matrícula')
        self.login(id_user)
