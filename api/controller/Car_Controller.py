# Models
from api.model.Car import Car

# Views
from api.screen.Car_Screen import CarScreen
from api.screen.Main_Screen import MainScreen

# Controllers
from ..controller.General_Controller import GeneralController

# dao
from api.data.Car_DAO import CarDAO


class CarController(GeneralController):

    def __init__(self, main_controller, cars=None):
        super().__init__()
        if cars is None:
            cars = []
        self.__cars = cars
        self.__main_controller = main_controller
        self.__car_dao = CarDAO()
        self.create_screen()

    def create_dependencies_by_list(self, dependencies_list: []):
        for encapsulated_car in dependencies_list:
            self.add_car(
                encapsulated_car['id_car'],
                encapsulated_car['car_plate'],
                encapsulated_car['car_model'],
                encapsulated_car['car_brand'],
                encapsulated_car['car_year'],
                encapsulated_car['car_kilometer'],
                encapsulated_car['car_tier']
            )

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
        return self.__car_dao.get_all()

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
        car = Car(car_id, car_plate, car_model, car_brand,
                  car_year, car_kilometer, car_tier)
        cars = self.__car_dao.get_all()
        if cars is None or cars == [] or len(cars) == 0:
            self.__car_dao.add(car.id_car, car)
            cars = self.__car_dao.get_all()
        for controller_car in cars:
            if controller_car.id_car != car.id_car and controller_car.car_plate != car.car_plate:
                self.__car_dao.add(car.id_car, car)
        return car

    def add_car_with_array(self, car_array):
        try:
            int(car_array[0])
            int(car_array[5])
            int(car_array[6])
        except:
            return 'Algum dos dados está errado'
        car = Car(int(car_array[0]), car_array[1], car_array[2], car_array[3],
                  car_array[4], int(car_array[5]), int(car_array[6]))
        cars = self.__car_dao.get_all()
        if cars is None or cars == []:
            self.__car_dao.add(car.id_car, car)
            return 'O Carro Foi Adicionado'
        for controller_car in cars:
            if controller_car.id_car != car.id_car and controller_car.car_plate != car.car_plate:
                self.__car_dao.add(car.id_car, car)
                return 'O Carro Foi Adicionado'
        return 'Não foi possível adicionar o Carro'

    def delete_car(self, car_id: int):
        cars = self.__car_dao.get_all()
        for controller_car in cars:
            if controller_car.id_car == car_id:
                self.__car_dao.remove(controller_car.id_car)
                return True

    def edit_car(self, car: Car, car_id: int):
        cars = self.__car_dao.get_all()
        for controller_car in cars:
            if controller_car.id_car == car_id:
                self.delete_car(car_id)
                self.__car_dao.add(car_id, car)

    def get_car_by_plate(self, plate: str):
        cars = self.__car_dao.get_all()
        for controller_car in cars:
            if controller_car.car_plate == plate:
                return controller_car

    def get_car_by_id(self, car_id):
        return self.__car_dao.get(car_id)

    def open_car_screen(self):
        self.__car_screen.open_gui('menu')

    def open_main_screen(self):
        self.__car_screen.close_gui()
        self.__main_controller.open_main_screen(True)
