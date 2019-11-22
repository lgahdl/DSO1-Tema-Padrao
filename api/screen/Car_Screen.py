# Models
from api.model.Car import Car

# Views
from api.screen.General_Screen import GeneralScreen

# Controllers

# Utils
from PySimpleGUI import PySimpleGUI as sg


class CarScreen(GeneralScreen):

    def __init__(self, car_controller):
        super().__init__(car_controller)
        self.init_menu_components()

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

    def add_car_with_array(self, car_array):
        print(car_array)
        message = super().controller.add_car_with_array(car_array)
        sg.Popup(message)
        self.close_gui()
        self.init_menu_components()
        self.open_gui('menu')

    def delete(self, car_id: int):
        return super().controller.delete_car(car_id)

    def edit(self, car: Car, id_car: int):
        super().controller.edit_car(car, id_car)

    def open(self):
        super().open()

    def init_menu_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Carros')],
            [sg.Text('Você deseja:')],
            [sg.Button('Inserir', key='INSERT_BUTTON')],
            [sg.Button('Deletar', key='DELETE_BUTTON')],
            [sg.Button('Editar', key='EDIT_BUTTON')],
            [sg.Button('Listar', key='LIST_BUTTON')],
            [],
            [sg.Button('Sair', key='EXIT_BUTTON')],
        ]
        self.__window = sg.Window('Carros').Layout(layout)

    def init_insert_components(self):
        self.close_gui()
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Adição de Carro', size=[30, 1])],
            [sg.Text(
                'Digite os dados do Carro que você deseja adicionar:', size=[30, 1])],
            [sg.Text('Matricula', size=[15, 1]),
             sg.InputText('10', size=[30, 1])],
            [sg.Text('Placa', size=[15, 1]), sg.InputText('POO9990', size=[30, 1])],
            [sg.Text('Modelo', size=[15, 1]),
             sg.InputText('Monza', size=[30, 1])],
            [sg.Text('Marca', size=[15, 1]),
             sg.InputText('Chevrolet', size=[30, 1])],
            [sg.Text('Ano', size=[15, 1]),
             sg.InputText('1982', size=[30, 1])],
            [sg.Text('Quilometragem', size=[15, 1]),
             sg.InputText('10000', size=[30, 1])],
            [sg.Text('Categoria', size=[15, 1]),
             sg.InputCombo(('0', '1', '2', '3'), size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Adição de Carros').Layout(layout)

        self.open_gui('insert')

    def init_delete_components(self):
        self.close_gui()
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Remoção de Carro')],
            [sg.Text(
                'Digite a Matricula do Carro que você deseja remover:', size=[30, 1])],
            [sg.Text('Matricula:', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Carros').Layout(layout)

        self.open_gui('delete')

    def init_edit_components(self):
        self.close_gui()
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Edição de Carro', size=[30, 1])],
            [sg.Text(
                'Digite a matrícula do Carro que você deseja editar:', size=[30, 1])],
            [sg.Text('Matricula(não pode ser editada)', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text(
                'Digite os novos dados do carro:'
            )],
            [sg.Text('Placa', size=[15, 1]), sg.InputText('', size=[30, 1])],
            [sg.Text('Modelo', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Marca', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Ano', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Quilometragem', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Categoria', size=[15, 1]),
             sg.InputCombo(('0', '1', '2', '3'), size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Edição de Carros').Layout(layout)

        self.open_gui('edit')

    def init_list_components(self):
        self.close_gui()
        cars = super().controller.cars
        car_layout_array = []
        index = 0
        for car in cars:
            print(car.car_plate)
            car_layout_array.append(
                [sg.Text('Carro nº', size=[15, 1]),
                 sg.Text(index, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Matricula', size=[15, 1]),
                 sg.Text(car.id_car, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Placa', size=[15, 1]),
                 sg.Text(car.car_plate, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Modelo', size=[15, 1]),
                 sg.Text(car.car_model, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Marca', size=[15, 1]),
                 sg.Text(car.car_brand, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Ano', size=[15, 1]),
                 sg.Text(car.car_year, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Quilometragem', size=[15, 1]),
                 sg.Text(car.car_kilometer, size=[30, 1])])
            car_layout_array.append(
                [sg.Text('Categoria', size=[15, 1]),
                 sg.Text(car.car_tier, size=[30, 1])])
            car_layout_array.append([])
            index += 1
        car_layout_array.append(
            [sg.OK()]
        )

        sg.ChangeLookAndFeel('Reddit')

        layout = car_layout_array

        self.__window = sg.Window('Carros').Layout(layout)

        self.open_gui('list')

    def open_gui(self, screen_type='menu'):
        print(screen_type)
        if(screen_type == 'menu'):
            event = self.__window.Read()
            values = [0]
            if(event[0] == 'INSERT_BUTTON'):
                values[0] = -2
            elif(event[0] == 'DELETE_BUTTON'):
                values[0] = -3
            elif(event[0] == 'EDIT_BUTTON'):
                values[0] = -4
            elif(event[0] == 'LIST_BUTTON'):
                values[0] = -5
            elif(event[0] == 'EXIT_BUTTON'):
                values[0] = -1

        elif(screen_type == 'insert'):
            button, values = self.__window.Read()
            print(values)
            return self.add_car_with_array(values)

        elif(screen_type == 'delete'):
            button, values = self.__window.Read()
            print(values)
            deleted = self.delete(int(values[0]))
            print(deleted)
            if deleted:
                sg.Popup("Carro Apagado do Sistema")
                self.init_menu_components()
                self.open_gui('menu')
            else:
                sg.Popup("Não foi possível apagar o carro !!!")
                self.init_menu_components()
                self.open_gui('menu')

        elif(screen_type == 'edit'):
            button, values = self.__window.Read()
            print(values)
            super().controller.edit_car(values)

            self.init_menu_components()
            self.open_gui('menu')

        elif(screen_type == 'list'):
            button, values = self.__window.Read()
            print(values)
            self.init_menu_components()
            self.open_gui('menu')

        if(isinstance(values[0], int) and values[0] <= -1 and values[0] >= -5):
            if(values[0] == -1):
                sg.Popup('Você Fechou o Programa')
                self.close_gui()
            elif(values[0] == -2):
                self.init_insert_components()
            elif(values[0] == -3):
                self.init_delete_components()
            elif(values[0] == -4):
                self.init_edit_components()
            elif(values[0] == -5):
                self.init_list_components()
        else:
            sg.Popup('Comando Invalido')
            self.close_gui()

    def close_gui(self):
        self.__window.Close()

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
                car_kilometer = input(
                    " Nova Quilometragem ".center(60)) or car.car_kilometer
                car.car_kilometer = car_kilometer
            elif key == 'Categoria':
                string = (" | %s => %s | " % (key, car_array[key]))
                print(string.center(60))
                print(" | Insira a Categoria | ".center(60))
                print(
                    " | | Funcional[1] Completo[2] Executivo[3] | |".center(60))
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
