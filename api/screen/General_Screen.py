from abc import ABC, abstractmethod
from api.controller.General_Controller import GeneralController as ABCController


class GeneralScreen(ABC):

    @abstractmethod
    def __init__(self, controller: ABCController):
        self.__controller = controller

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller: ABCController):
        self.__controller = controller

    def open(self):
        print(" {} ".format(self.__class__.__name__).center(60, "-"))
        print(" | Você Deseja:  | ".center(60))
        print(" | Inserir [1]  | ".center(60))
        print(" | Deletar [2]  | ".center(60))
        print(" | Editar [3]  | ".center(60))
        print(" | Listar [4]  | ".center(60))
        print(" | Voltar Para o Menu[5] | ".center(60))
        while True:
            option = int(input(" Insira a opção desejada: ".center(60)))
            if option == 1:
                self.open_add_menu()
            elif option == 2:
                self.open_delete_menu()
            elif option == 3:
                self.open_edit_menu()
            elif option == 4:
                self.open_list_menu()
            elif option == 5:
                self.open_main_screen()
            else:
                print("Opção Inválida".center(60, "-"))

    @abstractmethod
    def open_add_menu(self):
        pass

    @abstractmethod
    def open_delete_menu(self):
        pass

    @abstractmethod
    def open_edit_menu(self):
        pass

    @abstractmethod
    def open_list_menu(self):
        pass

    def open_main_screen(self):
        self.controller.open_main_screen()

    @abstractmethod
    def add(self, **elements):
        pass

    @abstractmethod
    def delete(self, id_element):
        pass

    @abstractmethod
    def edit(self, element, id_element):
        pass
