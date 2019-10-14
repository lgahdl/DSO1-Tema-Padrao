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

    @abstractmethod
    def open(self):
        pass

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
