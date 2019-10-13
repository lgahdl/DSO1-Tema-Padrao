# Models
from ..model.Car import Car

# Views
from ..screen.General_Screen import GeneralScreen

# Controllers
from ..controller.Car_Controller import CarController


class CarScreen(GeneralScreen):

    def __init__(self, controller: CarController):
        self.__car_controller = controller

    def add_car(self, car: Car):
        return self.__car_controller.add_car(car)

    def delete_car(self, car: Car):
        return self.__car_controller.delete_car(car)

    def edit_car(self, car: Car, id_car: int):
        return self.__car_controller.edit_car(car, id_car)

    def open_main_screen(self):
        self.__car_controller.open_main_screen()
