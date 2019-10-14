# Models
from api.model.Key import Key

# Views
from api.screen.Key_Screen import KeyScreen
from api.screen.Main_Screen import MainScreen

# Controllers
from ..controller.General_Controller import GeneralController
from ..controller.Main_Controller import  MainController


class KeyController(GeneralController):

    id_key = 1

    def __init__(self, keys: [Key], key_screen: KeyScreen, main_controller: MainController):
        self.__keys = keys
        self.__key_screen = key_screen
        self.__main_controller = main_controller

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
            if KEY.car_plate != car_plate:
                car = self.__main_controller.car_controller.get_car_by_plate(car_plate)
                new_key = Key(int(self.__keys.__len__()), car)
                self.__keys.append(new_key)
            else:
                print("Este carro ja possui chave cadastrada".center(60, "-"))

    def delete_key(self, car_plate: int):
        keys = self.__keys
        for KEY in keys:
            if KEY.car.car_plate == car_plate:
                self.__keys.remove(KEY)
                print("Chave Removida com sucesso".center(60))
            else:
                print("Nao Foi Possivel remover a chave".center(60))

    ##def edit_key(self, key: Key, id_key: int):
    ##    keys = self.__keys
    ##    for KEY in keys:
    ##        if KEY.id == id_key:
    ##            index = keys.index(KEY)
    ##            self.__keys[index] = key

    def get_key_by_car_plate(self, plate: str):
        keys = self.__keys
        for KEY in keys:
            if KEY.car.car_plate == plate:
                return KEY

    def open_key_screen(self):
        self.__key_screen.open()

    def open_main_screen(self):
        self.__main_controller.open_main_screen()