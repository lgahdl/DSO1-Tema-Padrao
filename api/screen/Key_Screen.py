#models
from api.model.Key import Key

#controllers
from api.controller.Key_Controller import KeyController

#screens
from api.screen.General_Screen import GeneralScreen

class KeyScreen(GeneralScreen):
    def __init__(self, key_controller: KeyController):
        super().__init__(key_controller)

    def open(self):
        super().open()

    def add(self):
        super().controller.add_key()

    def edit(self, key: Key, id_key: int):
        super().controller.edit_key(key, id_key)

    def delete(self, car_plate: int):
        super().controller.delete_key(car_plate)

    def open_add_menu(self):
        print(" Cadastro de Chave ".center(60, "-"))
        car_plate = input(" | Placa do Carro | ".center(60))
        return self.add(car_plate)

    def open_edit_menu(self):
        print("Desculpe, mas essa Opcao nao esta disponivel para chaves".center(60, "-"))
        super().open()

    def open_delete_menu(self):
        print("Deletar Chave". center(60, "-"))
        car_plate = input(" | Qual a placa do carro a qual a chave pertence? |".center(60))
        return self.delete(car_plate)

    def open_list_menu(self):
        print(" Listagem de Chaves ".center(60, "-"))
        keys = super().controller.keys
        if keys is not None:
            key_number = 1
            for key in keys:
                key_array = key.to_array()
                print((" *** Requisicao " + str(key_number) + " *** ").center(60))
                for KEY in key_array:
                    string = (" | %s => %s | " % (KEY, key_array[KEY]))
                    print(string.center(60))
                key_number = key_number + 1