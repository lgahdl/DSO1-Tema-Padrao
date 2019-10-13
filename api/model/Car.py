from ..model import General_Model


class Car(General_Model):

    def __init__(self, id: int, car_plate: str, model: str, brand: str):
        self.__id_car = id
        self.__car_plate = car_plate,
        self.__car_model = model
        self.__car_brand = brand

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def id(self):
        return self.__id_car

    @property
    def car_plate(self):
        return self.__car_plate

    @property
    def car_model(self):
        return self.__car_model

    @property
    def car_brand(self):
        return self.__car_brand

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

    @id.setter
    def id(self, id: int):
        self.__id_car = id

    @car_plate.setter
    def car_plate(self, plate: str):
        self.__car_plate = plate

    @car_model.setter
    def car_model(self, model: str):
        self.__car_model = model

    @car_brand.setter
    def car_brand(self, brand: str):
        self.__car_brand = brand

