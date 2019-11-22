# Views
from api.screen.General_Screen import GeneralScreen

# Models
from api.model.Request import Request

# Utils
from PySimpleGUI import PySimpleGUI as sg


class RequestScreen(GeneralScreen):

    def __init__(self, request_controller):
        super().__init__(request_controller)
        self.init_menu_components()

    @property
    def request_controller(self):
        return super().controller

    @request_controller.setter
    def request_controller(self, request_controller):
        super().controller = request_controller

    def open(self):
        print(" Request Screen ".center(60, "-"))
        print(" | Você Deseja:  | ".center(60))
        print(" | Pedir uma chave [1]  | ".center(60))
        print(" | Devolver uma chave [2]  | ".center(60))
        print(" | Deletar uma das Requisicoes [3]  | ".center(60))
        print(" | Listar as Requisicoes [4]  | ".center(60))
        print(" | Voltar Para o Menu[5] | ".center(60))
        while True:
            option = int(
                input("Digite o numero que corresponde ao que voce deseja fazer:".center(60)))
            if(option == 1):
                self.open_add_menu()
            elif(option == 2):
                self.open_return_key_screen()
            elif(option == 3):
                self.open_delete_menu()
            elif(option == 4):
                self.open_list_menu()
            elif(option == 5):
                super().controller.open_main_screen()
            else:
                print("Opcao Invalida!!!".center(60, "-"))

    def init_menu_components(self):
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Requisição')],
            [sg.Text('Você deseja:')],
            [sg.Button('Inserir', key='INSERT_BUTTON')],
            [sg.Button('Deletar', key='DELETE_BUTTON')],
            [sg.Button('Editar', key='EDIT_BUTTON')],
            [sg.Button('Listar', key='LIST_BUTTON')],
            [],
            [sg.Button('Sair', key='EXIT_BUTTON')],
        ]
        self.__window = sg.Window('Requisições').Layout(layout)

    def init_insert_components(self):
        # Antes essa função funcionava diretamente para o usuário logado, mas como está sem persistência de arquivos(no momento em que escrevo essa função)...
        # ...o main_controller não armazena user até esse ponto por causa do PySimpleGUI, irei efetuar ela pedindo para ser digitado o ID
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Adição de Requisição', size=[30, 1])],
            [sg.Text('Digite o ID do Usuário que está requerindo:', size=[30, 1])],
            [sg.Text('Matricula', size=[30, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text(
                'Digite a Placa do carro que você deseja:', size=[20, 1]),
             sg.InputText('XYZ9955', [30, 1])],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Adição de Requisições').Layout(layout)

        self.open_gui('insert')

    def init_delete_components(self):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Remoção de Requisição')],
            [sg.Text(
                'Digite o ID da Requisição que você deseja remover:', size=[30, 1])],
            [sg.Text('ID:', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Requisições').Layout(layout)

        self.open_gui('delete')

    def init_edit_components(self):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Edição de Requisição', size=[30, 1])],
            [sg.Text(
                'Requisições não oferecem essa opção!', size=[30, 1])],
            [],
            [sg.Cancel()]
        ]
        self.__window = sg.Window('Edição de Requisições').Layout(layout)

        self.open_gui('edit')

    def init_list_components(self):

        requests = super().controller.requests
        request_layout_array = []
        for request in requests:
            request_layout_array.append(
                [sg.Text('ID', size=[15, 1]),
                 sg.Text(request.id_request, size=[30, 1])])
            request_layout_array.append([sg.Text('ID', size=[15, 1]),
                                         sg.Text(request.id_request, size=[30, 1])])
            request_layout_array.append([sg.Text('Nome do usuário', size=[15, 1]),
                                         sg.Text(request.user.user_name, size=[30, 1])])
            request_layout_array.append([sg.Text('Data da requisição', size=[15, 1]),
                                         sg.Text(request.created_date, size=[30, 1])])
            request_layout_array.append([sg.Text('Data da Devolução', size=[15, 1]),
                                         sg.Text(request.devolution_date, size=[30, 1])])
            request_layout_array.append([sg.Text('Placa do Carro', size=[15, 1]),
                                         sg.Text(str(request.key.car.car_plate), size=[30, 1])])
            request_layout_array.append([sg.Text('Foi aceita?', size=[15, 1]),
                                         sg.Text(str(request.accepted), size=[30, 1])])
            request_layout_array.append([sg.Text('Razão da Negação(se negada)', size=[15, 1]),
                                         sg.Text(str(request.reason), size=[30, 1])])
        request_layout_array.append(
            [sg.OK()]
        )

        sg.ChangeLookAndFeel('Reddit')

        layout = request_layout_array

        self.__window = sg.Window('Requisições').Layout(layout)

        self.open_gui('list')

    def open_gui(self, screen_type='menu'):
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
                super().controller.open_main_screen()

        elif(screen_type == 'insert'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            self.add_request_with_array(values)

        elif(screen_type == 'delete'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            deleted = self.delete(int(values[0]))
            print(deleted)
            if deleted:
                sg.Popup("Requisição Apagada do Sistema")
                self.close_gui()
                self.init_menu_components()
                self.open_gui('menu')
            else:
                sg.Popup("Não foi possível apagar a Requisição !!!")
                self.close_gui()
                self.init_menu_components()
                self.open_gui('menu')

        elif(screen_type == 'edit'):
            button, values = self.__window.Read()
            if(button == 'Cancel' or button == None):
                self.back_handler()
            super().controller.edit_user(values)

            self.init_menu_components()
            self.open_gui('menu')

        elif(screen_type == 'list'):
            button, values = self.__window.Read()
            self.close_gui()
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

    def add(self, car_plate):
        return super().controller.add_request(car_plate)

    def add_request_with_array(self, values):
        self.close_gui()
        super().controller.add_request_with_array(values)
        self.init_menu_components()
        self.open_gui('menu')

    def edit(self, request, id_request):
        return super().controller.edit_request(request, id_request)

    def delete(self, id_request):
        return super().controller.delete_request(id_request)

    def open_main_screen(self):
        return super().controller.open_main_screen()

    def show_is_blocked_message(self):
        print("Você tentou mais de 3 vezes veículos não permitidos, você está bloqueado")

    # def open_add_menu(self):
    #     print(" Nova Requisicao".center(60, "-"))
    #     user_array = super().controller.main_controller.user.to_array()
    #     print((" *** Requisicao para o Usuario: *** ").center(60))
    #     for key in user_array:
    #         string = (" | %s => %s | " % (key, user_array[key]))
    #         print(string.center(60))
    #     car_plate = input(
    #         "---Digite a placa do carro(formato: ZZZ9999) que você deseja requirir ou digite 'Voltar' para voltar para a tela anterior---".center(60))
    #     if (car_plate == "Voltar"):
    #         self.open()
    #     else:
    #         return self.add(car_plate)

    # def open_delete_menu(self):
    #     print(" Remoção de Requisicao ".center(60, "-"))
    #     id_request = int(input(" | Insira o ID da requisicao:  |".center(60)))
    #     deleted = self.delete(id_request)
    #     if deleted:
    #         print(" | Requisicao Apagada do Sistema | ".center(60))
    #     else:
    #         print(" !!! Não foi possível apagar a Requisicao !!!".center(60))

    # def open_return_key_screen(self):
    #     print(" Devolucao".center(60, "-"))
    #     user_array = super().controller.main_controller.user.to_array()
    #     print((" *** Devolucao do Usuario: *** ").center(60))
    #     for key in user_array:
    #         string = (" | %s => %s | " % (key, user_array[key]))
    #         print(string.center(60))
    #     request = super().controller.get_unfinished_request_by_user(
    #         super().controller.main_controller.user)
    #     if(isinstance(request, Request)):
    #         super().controller.return_key(request)
    #         print("Chave Devolvida")
    #         print(request)
    #         finished_request = super().controller.get_request_by_id(request.id_request)
    #         request_array = finished_request.to_array()
    #         for key in request_array:
    #             string = (" | %s => %s | " % (key, request_array[key]))
    #             print(string.center(60))
    #     else:
    #         print("Voce nao tem chave para devolver")

    # def open_list_menu(self):
    #     print(" Listagem de Requisicoes ".center(60, "-"))
    #     requests = super().controller.requests
    #     if requests is not None:
    #         request_number = 1
    #         for request in requests:
    #             request_array = request.to_array()
    #             print((" *** Requisicao " + str(request_number) + " *** ").center(60))
    #             for key in request_array:
    #                 string = (" | %s => %s | " % (key, request_array[key]))
    #                 print(string.center(60))
    #             request_number = request_number + 1

    # def open_edit_menu(self):
    #     print("Requisicoes não oferecem essa opção")
    #     self.open()

    def back_handler(self):
        self.close_gui()
        self.init_menu_components()
        self.open_gui('menu')
