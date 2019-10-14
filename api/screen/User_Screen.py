# Models
from ..model import User

# Views
from ..screen.General_Screen import GeneralScreen
from ..screen.Main_Screen import MainScreen

# Controllers
from ..controller.User_Controller import UserController


class UserScreen(GeneralScreen):

    def __init__(self, user_controller: UserController):
        self.__user_controller = user_controller

    def add(self, user: User):
        return self.__user_controller.add_user(user)

    def delete(self, id_user: int):
        return self.__user_controller.delete_user(id_user)

    def edit(self, user: User, id_user: int):
        return self.__user_controller.edit_user(user, id_user)

    @staticmethod
    def open_main_screen():
        MainScreen.open()

    def open(self):
        print("------------- User Screen -------------")
        print("\n------------- Você Deseja -------------")
        print("\n----------- Inserir User [1] -----------")
        print("\n----------- Deletar User [2] -----------")
        print("\n----------- Editar User [3] -----------")
        print("\n----------- Listar Users [4] -----------")
        while True:
            option = int(input("Insira a opção desejada: "))
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                pass
            else:
                print("Opção Inválida")
