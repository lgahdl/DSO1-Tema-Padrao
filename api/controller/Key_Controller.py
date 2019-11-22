# Models
from api.model.Key import Key

# Views
from api.screen.Key_Screen import KeyScreen

# Controllers
from ..controller.General_Controller import GeneralController


class KeyController(GeneralController):
    id_key = 1

    def __init__(self, main_controller, keys: [Key] = []):
        super().__init__()
        self.__keys = keys
        self.__main_controller = main_controller
        self.create_screen()

    def create_screen(self):
        self.__key_screen = KeyScreen(self)

    def create_dependencies_by_list(self, dependencies_list: []):
        for encapsulated_key in dependencies_list:
            key = Key(
                encapsulated_key['id_key'],
                self.__main_controller.car_controller.get_car_by_plate(encapsulated_key['car_plate'])
            )
            self.__keys.append(key)

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def keys(self):
        return self.__keys

    @property
    def key_screen(self):
        return self.__key_screen

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

    @keys.setter
    def keys(self, keys: [Key]):
        self.__keys = keys

    @key_screen.setter
    def key_screen(self, key_screen: KeyScreen):
        self.__key_screen = key_screen

    def add_key(self, car_plate: str):
        keys = self.__keys
        for KEY in keys:
            if KEY.car.car_plate != car_plate:
                car = self.__main_controller.car_controller.get_car_by_plate(car_plate)
                new_key = Key(int(self.__keys.__len__()), car)
                self.__keys.append(new_key)
                return 'Chave Cadastrada no Sistema'
            else:
                return 'Este carro ja possui chave cadastrada'

    def delete_key(self, car_plate: int):
        keys = self.__keys
        for KEY in keys:
            if KEY.car.car_plate == car_plate:
                self.__keys.remove(KEY)
                return 'Chave Removida Com Sucesso'
        return 'Não Foi Possivel Remover a chave'

    ##def edit_key(self, key: Key, id_key: int):
    ##    keys = self.__keys
    ##    for KEY in keys:
    ##        if KEY.id_key == id_key:
    ##            index = keys.index(KEY)
    ##            self.__keys[index] = key

    def get_key_by_car_plate(self, plate: str):
        keys = self.__keys
        for KEY in keys:
            if KEY.car.car_plate == plate:
                return KEY

    def open_key_screen(self):
        self.__key_screen.open_gui('menu')

    def open_main_screen(self):
        self.__key_screen.close_gui()
        self.__main_controller.open_main_screen(True)
