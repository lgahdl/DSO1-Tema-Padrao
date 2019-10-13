# Models
from ..model.Car import Car
from ..model.General_Model import GeneralModel


class Key(GeneralModel):
    def __init__(self, id_key: int, car: Car):
        self.__id_key = id_key
        self.__car = car

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def id(self):
        return self.__id_key

    @property
    def car(self):
        return self.__car

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

    @id.setter
    def id(self, id_key: int):
        self.__id_key = id_key

    @car.setter
    def car(self, car: Car):
        self.__car = car
