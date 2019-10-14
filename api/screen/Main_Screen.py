# Views
from ..screen.General_Screen import GeneralScreen

#Controller
from api.controller.Main_Controller import MainController


class MainScreen(GeneralScreen):

    def __init__(self, main_controller: MainController):
        super().__init__(main_controller)

    def open(self):
        while True:
        id_user = input('Olá, por favor, digite sua Matrícula')
        self.login(id_user)
        if(self.login(id_user)):
            print(" | Você Deseja ir para a página de:  | ".center(60))
            print(" | Usuarios[1]  | ".center(60))
            print(" | Requisicoes [2]  | ".center(60))
            print(" | Chaves [3]  | ".center(60))
            print(" | Carros [4]  | ".center(60))
            while True:
                option = int(input(" Insira a opção desejada: ".center(60)))
                if option == 1:
                    super().controller.open_user_controller()
                elif option == 2:
                    super().controller.open_request_controller()
                elif option == 3:
                    super().controller.open_key_controller()
                elif option == 4:
                    super().controller.open_car_controller()
                else:
                    print("Opção Inválida".center(60, "-"))
        elif:
            print("Matricula Invalida".center(60,"-"))

    def login(self, id_user: int):
        return super().controller.get_user(id_user)

