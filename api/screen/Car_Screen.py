# Models
from api.model.Car import Car

# Views
from api.screen.General_Screen import GeneralScreen

# Controllers


class CarScreen(GeneralScreen):

    def __init__(self, car_controller):
        super().__init__(car_controller)

    def add(self,
            id_car: int,
            car_plate: str,
            model: str,
            brand: str,
            year: int,
            kilometer: float,
            tier: int):
        super().controller.add_car(
            id_car,
            car_plate,
            model,
            brand,
            year,
            kilometer,
            tier
        )

    def delete(self, car_id: int):
        super().controller.delete_car(car_id)

    def edit(self, car: Car, id_car: int):
        super().controller.edit_car(car, id_car)

    def open(self):
        super().open()

    def open_add_menu(self):
        print(" Cadastro de Carro ".center(60, "-"))

        car_id = int(input(" | Código de Identificação | ".center(60)))
        car_plate = input(" | Placa | ".center(60))
        car_model = input(" | Modelo | ".center(60))
        car_brand = input(" | Marca | ".center(60))
        car_year = int(input(" | Ano | ".center(60)))
        car_kilometer = float(input(" | Quilometragem | ".center(60)))

        print(" | Insira a Categoria | ".center(60))
        print(" | | Funcional[1] Completo[2] Executivo[3] | |".center(60))
        car_tier = None
        while car_tier is None:
            input_tier = int(input(" | Código | ".center(60)))
            if 1 <= input_tier <= 3:
                car_tier = input_tier
            else:
                print(" !!!Opção Inválida!!! ".center(60))
        return self.add(car_id, car_plate, car_model, car_brand, car_year, car_kilometer, car_tier)

    def open_delete_menu(self):
        print(" Remoção de Carro ".center(60))
        car_id = int(input(" | Insira o Código do Carro | "))
        deleted = self.delete(car_id)
        if deleted:
            print(" | Carro Apagado do Sistema | ".center(60))
        else:
            print(" !!! Não foi possível apagar o carro !!!".center(60))


    def open_edit_menu(self):
        print(" Edição de Carro ".center(60, "-"))
        car_id = int(input(" | Insira o Código do Carro | "))
        car = super().controller.get_car_by_id(car_id)
        car_array = car.to_array()
        for key in car_array:
            if key == 'Placa':
                string = (" | %s => %s | " % (key, car_array[key]))
                print(string.center(60))
                car_plate = input(" Nova Placa ".center(60)) or car.car_plate
                car.car_plate = car_plate
            elif key == 'Quilometragem':
                string = (" | %s => %s | " % (key, car_array[key]))
                print(string.center(60))
                car_kilometer = input(" Nova Quilometragem ".center(60)) or car.car_kilometer
                car.car_kilometer = car_kilometer
            elif key == 'Categoria':
                string = (" | %s => %s | " % (key, car_array[key]))
                print(string.center(60))
                print(" | Insira a Categoria | ".center(60))
                print(" | | Funcional[1] Completo[2] Executivo[3] | |".center(60))
                car_tier = None
                while car_tier is None:
                    input_tier = int(input(" | Código | ".center(60)))
                    if 1 <= input_tier <= 3 and input_tier is not None:
                        car_tier = input_tier
                    else:
                        print(" !!!Opção Inválida!!! ".center(60))
                    if car_tier is None:
                        car_tier = car.car_tier
                car.car_tier = car_tier
            else:
                string = (" | %s => %s | " % (key, car_array[key]))
                print(string.center(60))
        return super().controller.edit_car(car, car_id)

    def open_list_menu(self):
        print(" Listagem de Carros ".center(60, "-"))
        cars = super().controller.cars
        if cars is not None:
            car_number = 1
            for car in cars:
                car_array = car.to_array()
                print((" *** Carro "+str(car_number)+" *** ").center(60))
                for key in car_array:
                    string = (" | %s => %s | " % (key, car_array[key]))
                    print(string.center(60))
                car_number = car_number + 1

    def open_main_screen(self):
        super().open_main_screen()
