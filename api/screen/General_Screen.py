from abc import ABC, abstractmethod
from ..controller import General_Controller as ABCController


class General_Screen(ABC):

    @abstractmethod
    def __init__(self, controller: ABCController):
        self.__controller = controller
    
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def edit(self, element):
        pass
