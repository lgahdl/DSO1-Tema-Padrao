# Models
from api.model.Car import Car

# Views
from api.screen.Car_Screen import CarScreen
from api.screen.Main_Screen import MainScreen

# Controllers
from ..controller.General_Controller import GeneralController
from ..controller.Main_Controller import MainController


class CarController(GeneralController):

    def __init__(self, main_controller: MainController, cars=None):
        super().__init__()
        if cars is None:
            cars = []
        self.__cars = cars
        self.__main_controller = main_controller
        self.create_screen()

    def create_screen(self):
        self.__car_screen = CarScreen(self)

    def destroy_screen(self):
        if self.__car_screen is not None:
            del self.__car_screen

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

    def add_car(self,
                car_id: int,
                car_plate: str,
                car_model: str,
                car_brand: str,
                car_year: int,
                car_kilometer: float,
                car_tier: int
                ) -> Car:
        car = Car(car_id, car_plate, car_model, car_brand, car_year, car_kilometer, car_tier)
        cars = self.__cars
        for controller_car in cars:
            if controller_car.id != car.id and \
                    controller_car.car_plate != car.car_plate:
                self.__cars.append(car)

    def delete_car(self, car_id: int):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.id == car_id:
                self.__cars.remove(controller_car)

    def edit_car(self, car: Car, car_id: int):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.id == car_id:
                index = cars.index(controller_car)
                self.__cars[index] = car

    def get_car_by_plate(self, plate: str):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.car_plate == plate:
                return controller_car

    def get_car_by_id(self, car_id):
        cars = self.__cars
        for controller_car in cars:
            if controller_car.id == car_id:
                return controller_car

    def open_car_screen(self):
        self.__car_screen.open()

    def open_main_screen(self):
        self.__main_controller.open_main_screen()
