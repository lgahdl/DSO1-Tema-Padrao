# Views
from ..screen.General_Screen import GeneralScreen


# Controller


class MainScreen(GeneralScreen):

    def __init__(self, main_controller):
        super().__init__(main_controller)

    def open(self):
        if super().controller.id_user_logged != 0:
            self.run()
        else:
            while True:
                super().controller.id_user_logged = int(input(' Olá, por favor, digite sua Matrícula '))
                id_user = super().controller.id_user_logged
                if self.login(id_user):
                    self.run()
                else:
                    print("Matricula Invalida".center(60, "-"))

    def run(self):
        print(" Menu Inicial ".center(60, "-"))
        print(" | Você Deseja ir para a página de:  | ".center(60))
        print(" | Usuarios[1]  | ".center(60))
        print(" | Requisicoes [2]  | ".center(60))
        print(" | Chaves [3]  | ".center(60))
        print(" | Carros [4]  | ".center(60))
        print(" |  | ".center(60))
        print(" |  | ".center(60))
        print(" | SAIR[-1] | ".center(60))
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
            elif option == -1:
                super().controller.exit()
            else:
                print("Opção Inválida".center(60, "-"))

    def login(self, id_user: int):
        return super().controller.get_user(id_user)

    def open_add_menu(self):
        pass

    def open_delete_menu(self):
        pass

    def open_edit_menu(self):
        pass

    def open_list_menu(self):
        pass

    def add(self, **elements):
        pass

    def delete(self, id_element):
        pass

    def edit(self, element, id_element):
        pass
