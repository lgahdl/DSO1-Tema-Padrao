# screens
from api.screen.General_Screen import GeneralScreen

# Utils
from PySimpleGUI import PySimpleGUI as sg


class KeyScreen(GeneralScreen):
    def __init__(self, key_controller):
        super().__init__(key_controller)
        self.init_menu_components()

    def open(self):
        super().open()

    def add(self, car_plate):
        return super().controller.add_key(car_plate)

    def edit(self, key, id_key: int):
        return super().controller.edit_key(key, id_key)

    def delete(self, car_plate: int):
        return super().controller.delete_key(car_plate)

    def init_menu_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Chaves')],
            [sg.Text('Você deseja:')],
            [sg.Button('Inserir', key='INSERT_BUTTON')],
            [sg.Button('Deletar', key='DELETE_BUTTON')],
            [sg.Button('Editar', key='EDIT_BUTTON')],
            [sg.Button('Listar', key='LIST_BUTTON')],
            [],
            [sg.Button('Sair', key='EXIT_BUTTON')],
        ]
        self.__window = sg.Window('Chaves').Layout(layout)

    def init_insert_components(self):
        self.close_gui()
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Adição de Chave', size=[30, 1])],
            [sg.Text(
                'Digite A Placa do Carro ao qual pertence a Chave que você deseja adicionar:', size=[30, 2])],
            [sg.Text('Placa', size=[15, 1]),
             sg.InputText('OOO7777', size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Adição de Chaves').Layout(layout)

        self.open_gui('insert')

    def init_delete_components(self):
        self.close_gui()
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Remoção de Chave')],
            [sg.Text(
                'Digite a Placa do carro ao qual pertence a chave:', size=[30, 1])],
            [sg.Text('Placa:', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Chaves').Layout(layout)

        self.open_gui('delete')

    def init_edit_components(self):
        self.close_gui()
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Edição de Chave', size=[30, 1])],
            [sg.Text(
                'Digite a matrícula da Chave que você deseja editar:', size=[30, 1])],
            [sg.Text('Matricula(não pode ser editada)', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text(
                'Digite os novos dados da chave:'
            )],
            [sg.Text('Placa', size=[15, 1]), sg.InputText('', size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Edição de Chaves').Layout(layout)

        self.open_gui('edit')

    def init_list_components(self):
        self.close_gui()
        keys = super().controller.keys
        key_layout_array = []
        index = 0
        for key in keys:
            key_layout_array.append(
                [sg.Text('Chave nº', size=[15, 1]),
                 sg.Text(index, size=[30, 1])])
            key_layout_array.append(
                [sg.Text('Matricula', size=[15, 1]),
                 sg.Text(key.id_key, size=[30, 1])])
            key_layout_array.append(
                [sg.Text('Placa', size=[15, 1]),
                 sg.Text(key.car.car_plate, size=[30, 1])])
            key_layout_array.append([])
            index += 1
        key_layout_array.append(
            [sg.OK()]
        )

        sg.ChangeLookAndFeel('Reddit')

        layout = key_layout_array

        self.__window = sg.Window('Chaves').Layout(layout)

        self.open_gui('list')

    def open_gui(self, screen_type='menu'):
        print(screen_type)
        if(screen_type == 'menu'):
            event = self.__window.Read()
            values = [0]
            if(event[0] == 'INSERT_BUTTON'):
                super().controller.open_main_screen()
            elif(event[0] == 'DELETE_BUTTON'):
                values[0] = -3
            elif(event[0] == 'EDIT_BUTTON'):
                values[0] = -4
            elif(event[0] == 'LIST_BUTTON'):
                values[0] = -5
            elif(event[0] == 'EXIT_BUTTON'):
                super().controller.open_main_screen()

        elif(screen_type == 'insert'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            print(values)
            message = self.add(values[0])
            sg.Popup(message)

        elif(screen_type == 'delete'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            print(values)
            deleted = self.delete(values[0])
            sg.Popup(deleted)
            self.init_menu_components()
            self.open_gui('menu')

        elif(screen_type == 'edit'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            print(values)
            super().controller.edit_key(values)

            self.init_menu_components()
            self.open_gui('menu')

        elif(screen_type == 'list'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            print(values)
            self.init_menu_components()
            self.open_gui('menu')

        if(isinstance(values[0], int) and values[0] <= -1 and values[0] >= -5):
            if(values[0] == -2):
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

    # def open_add_menu(self):
    #     print(" Cadastro de Chave ".center(60, "-"))
    #     car_plate = input(" | Placa do Carro | ".center(60))
    #     return self.add(car_plate)

    # def open_edit_menu(self):
    #     print("Desculpe, mas essa Opcao nao esta disponivel para chaves".center(60, "-"))
    #     super().open()

    # def open_delete_menu(self):
    #     print("Deletar Chave". center(60, "-"))
    #     car_plate = input(
    #         " | Qual a placa do chave a qual a chave pertence? |".center(60))
    #     return self.delete(car_plate)

    # def open_list_menu(self):
    #     print(" Listagem de Chaves ".center(60, "-"))
    #     keys = super().controller.keys
    #     if keys is not None:
    #         key_number = 1
    #         for key in keys:
    #             key_array = key.to_array()
    #             print((" *** Requisicao " + str(key_number) + " *** ").center(60))
    #             for KEY in key_array:
    #                 string = (" | %s => %s | " % (KEY, key_array[KEY]))
    #                 print(string.center(60))
    #             key_number = key_number + 1

    def back_handler(self):
        self.close_gui()
        self.init_menu_components()
        self.open_gui('menu')
