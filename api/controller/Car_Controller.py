# Models
from ..model.Car import Car

# Views
from ..screen.Car_Screen import CarScreen
from ..screen.Main_Screen import MainScreen

# Controllers
from ..controller.General_Controller import GeneralController
from ..controller.Main_Controller import  MainController


class CarController(GeneralController):

    def __init__(self, cars: [Car], car_screen: CarScreen, main_controller: MainController):
        self.__cars = cars
        self.__car_screen = car_screen
        self.__main_controller = main_controller

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
        cars = self.__cars
        for controllerCar in cars:
            if controllerCar.id != car.id and \
                    controllerCar.car_plate != car.car_plate:
                self.__cars.append(car)

    def delete_car(self, id_car: int):
        cars = self.__cars
        for controllerCar in cars:
            if controllerCar.id == id_car:
                self.__cars.remove(controllerCar)

    def edit_car(self, car: Car, id_car: int):
        cars = self.__cars
        for controllerCar in cars:
            if controllerCar.id == id_car:
                index = cars.index(controllerCar)
                self.__cars[index] = car

    def open_car_screen(self):
        self.__car_screen.open()

    @staticmethod
    def open_main_screen(self):
        self.__main_controller.open_main_screen()
