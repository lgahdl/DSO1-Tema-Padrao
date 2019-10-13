# Models
from api.model.Car import Car

# Views
from api.screen.Car_Screen import CarScreen
from api.screen.Main_Screen import MainScreen

# Controllers
from api.controller.Main_Controller import GeneralController
from api.controller.Main_Controller import MainController


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
        for controller_car in cars:
            if controller_car.id != car.id and \
                    controller_car.car_plate != car.car_plate:
                self.__cars.append(car)

    def delete_car(self, id_car: int):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.id == id_car:
                self.__cars.remove(controller_car)

    def edit_car(self, car: Car, id_car: int):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.id == id_car:
                index = cars.index(controller_car)
                self.__cars[index] = car

    def get_car_by_plate(self, plate: str):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.car_plate == plate:
                return controller_car

    def open_car_screen(self):
        self.__car_screen.open()

    def open_main_screen(self):
        self.__main_controller.open_screen()
