from api.data.DAO import DAO
from api.model.Car import Car


class CarDAO(DAO):
    def __init__(self):
        super().__init__('cars.pkl')

    def add(self, key, car: Car):
        if (isinstance(car.id_car, int)) and (car is not None) \
                and isinstance(car, Car) and (key == car.id_car):
            super().add(key, car)

    def get(self, key: int):
        if key is not None and isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if key is not None and isinstance(key, int):
            return super().remove(key)
