# Views
from api.screen.General_Screen import GeneralScreen

# Models
from api.controller.Request_Controller import RequestController


class RequestScreen(GeneralScreen):

    def __init__(self, request_controller: RequestController):
        super().__init__(request_controller)

    @property
    def request_controller(self):
        return super().controller

    @request_controller.setter
    def request_controller(self, request_controller):
        super().controller = request_controller

    def open(self):
        print(" User Screen ".center(60, "-"))
        print(" | Você Deseja:  | ".center(60))
        print(" | Pedir uma chave [1]  | ".center(60))
        print(" | Devolver uma chave [2]  | ".center(60))
        print(" | Deletar uma das Requisicoes [3]  | ".center(60))
        print(" | Listar as Requisicoes [4]  | ".center(60))
        print(" | Voltar Para o Menu[5] | ".center(60))
        while True:
            option = input("Digite o numero que corresponde ao que voce deseja fazer:".center(60))
            if(option == 1):
                self.open_add_menu()
            elif(option == 2):
                self.open_return_key_screen()
            elif(option == 3):
                self.open_delete_menu()
            elif(option == 4):
                self.open_delete_menu()
            elif(option == 5):
                super().controller.open_main_screen()
            else:
                print("Opcao Invalida!!!".center(60, "-"))


    def add(self, user, car_plate):
        super().controller.add_request(user, car_plate)

    def edit(self, request, id_request):
        super().controller.edit_request(request, id_request)

    def delete(self, id_request):
        super().controller.delete_request(id_request)

    def open_main_screen(self):
        super().controller.open_main_screen()

    def show_is_blocked_message(self):
        print("Você tentou mais de 3 vezes acessar esse mesmo veículo, você está bloqueado")

    def open_add_menu(self):
        print(" Nova Requisicao".center(60, "-"))
        user_array = super().controller.__main_controller.user.to_array()
        print((" *** Requisicao para o Usuario: *** ").center(60))
        for key in user_array:
            string = (" | %s => %s | " % (key, user_array[key]))
            print(string.center(60))
        car_plate = input("---Digite a placa do carro(formato: ZZZ9999) que você deseja requirir\
                            ou digite 'Voltar' para voltar para a tela anterior---".center(60))
        if (car_plate == "Voltar"):
            self.open()
        else:
            return self.add(super().controller.main_controller.user, car_plate)


    def open_delete_menu(self):
        print(" Remoção de Requisicao ".center(60, "-"))
        id_request = int(input(" | Insira o ID da requisicao:  |".center(60)))
        deleted = self.delete(id_request)
        if deleted:
            print(" | Requisicao Apagada do Sistema | ".center(60))
        else:
            print(" !!! Não foi possível apagar a Requisicao !!!".center(60))

    def open_return_key_screen(self):
        print(" Devolucao".center(60, "-"))
        user_array = super().controller.__main_controller.user.to_array()
        print((" *** Devolucao do Usuario: *** ").center(60))
        for key in user_array:
            string = (" | %s => %s | " % (key, user_array[key]))
            print(string.center(60))
        request = super().controller.get_unfinished_request_by_user(super().controller.__main_controller.user)
        super().controller.return_key(request)
        print("Chave Devolvida")
        finished_request = super().controller.get_request_by_id(request.id_request)
        request_array = finished_request.to_array()
        for key in request_array:
            string = (" | %s => %s | " % (key, request_array[key]))
            print(string.center(60))

    def open_list_menu(self):
        print(" Listagem de Requisicoes ".center(60, "-"))
        requests = super().controller.requests
        if requests is not None:
            request_number = 1
            for request in requests:
                request_array = request.to_array()
                print((" *** Requisicao " + str(request_number) + " *** ").center(60))
                for key in request_array:
                    string = (" | %s => %s | " % (key, request_array[key]))
                    print(string.center(60))
                request_number = request_number + 1
