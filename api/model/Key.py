# Models
from ..model.Car import Car
from ..model.General_Model import GeneralModel


class Key():
    def __init__(self, id_key: int, car: Car):
        self.__id_key = id_key
        self.__car = car

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def id_key(self):
        return self.__id_key

    @property
    def car(self):
        return self.__car

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

    @id_key.setter
    def id_key(self, id_key: int):
        self.__id_key = id_key

    @car.setter
    def car(self, car: Car):
        self.__car = car

    def to_array(self):
        to_array = {
            'Id': self.id_key,
            'Placa do Carro': self.car.car_plate,
            'Modelo': self.car.car_model,
            'Marca': self.car.car_brand,
            'Ano': self.car.car_year,
        }
        return to_array
