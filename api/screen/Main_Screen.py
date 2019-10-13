# Views
from ..screen.General_Screen import GeneralScreen

# Controllers
from ..controller.General_Controller import GeneralController


class MainScreen(GeneralScreen):

    def __init__(self, general_controller: GeneralController):
        super.__init__()
        self.__general_controller = general_controller

    def open(self):
        id_user = raw_input('Olá, por favor, digite sua Matrícula')
        user_phone = raw_input('Agora digite seu número de Telefone')
        self.login()
