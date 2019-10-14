# Views
from api.screen.General_Screen import GeneralScreen


class MainScreen(GeneralScreen):

    def __init__(self, main_controller):
        super().__init__(main_controller)

    def open(self):
        id_user = input('Olá, por favor, digite sua Matrícula: ')
        user_phone = input('Agora digite seu número de Telefone: ')
        super().controller.login(id_user, user_phone)

    def add(self, element):
        pass

    def delete(self, id_element):
        pass

    def edit(self, element, id_element):
        pass
