from api.data.DAO import DAO
from api.model.Car import Car


class CarDAO(DAO):
    def __init__(self):
        super().__init__('cars.pkl')

    def add(self, index, car: Car):
        if (isinstance(car.id_car, int)) and (car is not None) \
                and isinstance(car, Car) and (index == car.id_car):
            super().add(index, car)
            # ABCDE

    def get(self, index: int):
        if index is not None and isinstance(index, int):
            return super().get(index)

    def remove(self, index):
        if index is not None and isinstance(index, int):
            return super().remove(index)
