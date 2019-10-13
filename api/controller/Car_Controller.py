# Models
from ..model.Car import Car

# Views
from ..screen.Car_Screen import CarScreen

# Controllers
from ..controller.General_Controller import GeneralController


class CarController(GeneralController):

    def __init__(self, cars: [Car], car_screen: CarScreen):
        self.__cars = cars
        self.__car_screen = car_screen

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def cars(self):
        return self.__cars

    @property
    def car_screen(self):
        return self.__car_screen

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

    @cars.setter
    def cars(self, cars: [Car]):
        self.__cars = cars

    @car_screen.setter
    def car_screen(self, car_screen: CarScreen):
        self.__car_screen = car_screen

    def add_car(self, car: Car):
        pass

    def delete_car(self, car: Car):
        pass

    def edit_car(self, car: Car, id_car: int):
        pass

    def open_car_screen(self):
        self.__car_screen.open()

    def open_main_screen(self):
        pass
