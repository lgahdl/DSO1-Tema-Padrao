from api.model.General_Model import GeneralModel


class Car(GeneralModel):

    def __init__(self, id: int, car_plate: str, model: str, brand: str,
                 year: int, kilometer: float, tier: int):
        super().__init__()
        self.__id_car = id
        self.__car_plate = car_plate
        self.__car_model = model
        self.__car_brand = brand
        self.__car_year = year
        self.__car_kilometer = kilometer
        self.__car_tier = tier

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

    @property
    def car_year(self):
        return self.__car_year

    @property
    def car_kilometer(self):
        return self.__car_kilometer

    @property
    def car_tier(self):
        return self.__car_tier

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

    @car_year.setter
    def car_year(self, year: str):
        self.__car_year = year

    @car_kilometer.setter
    def car_kilometer(self, kilometer: str):
        self.__car_kilometer = kilometer

    @car_tier.setter
    def car_tier(self, tier: str):
        self.__car_tier = tier
