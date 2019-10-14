from abc import ABC, abstractmethod


class GeneralModel(ABC):

    __id = 0

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def id(self) -> int:
        pass

    @id.setter
    @abstractmethod
    def id(self, id_model: int) -> int:
        pass

    @abstractmethod
    def to_array(self):
        pass
