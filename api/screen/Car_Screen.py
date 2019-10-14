# Models
from ..model.Car import Car
# Controllers
from ..controller.Car_Controller import CarController
# Views
from ..screen.General_Screen import GeneralScreen


class CarScreen(GeneralScreen):

    def __init__(self, controller: CarController):
        self.__car_controller = controller

    def add(self, car: Car):
        return self.__car_controller.add_car(car)

    def delete(self, car: Car):
        return self.__car_controller.delete_car(car)

    def edit(self, car: Car, id_car: int):
        return self.__car_controller.edit_car(car, id_car)

    def open_main_screen(self):
        self.__car_controller.open_main_screen()
