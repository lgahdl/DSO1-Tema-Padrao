from abc import ABC, abstractmethod


class GeneralModel(ABC):

    __id = 0

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_model: int):
        self.__id = id_model
