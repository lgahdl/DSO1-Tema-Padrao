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
    def add(self, element):
        pass

    @abstractmethod
    def delete(self, id_element):
        pass

    @abstractmethod
    def edit(self, element, id_element):
        pass
