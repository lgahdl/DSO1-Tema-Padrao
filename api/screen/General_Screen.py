from abc import ABC, abstractmethod
from ..controller import General_Controller as ABCController


class GeneralScreen(ABC):

    @abstractmethod
    def __init__(self, controller: ABCController):
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
