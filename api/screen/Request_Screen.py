# Views
from api.screen.General_Screen import GeneralScreen

# Models
from api.controller.Request_Controller import RequestController


class RequestScreen(GeneralScreen):

    def __init__(self, request_controller: RequestController):
        self.__request_controller = super().__init__(request_controller)

    @property
    def request_controller(self):
        return self.__request_controller

    @request_controller.setter
    def request_controller(self, request_controller):
        self.__request_controller = request_controller

    def open(self):
        option = input("Digite o numero que corresponde ao que voce deseja fazer: \
                            \n 1- Pedir uma chave \n 2- Devolver uma chave \n \
                             3- Deletar uma das Requisiçoes \n 4- Voltar ao menu principal")
        if(option == 1):
            car_plate = input("Digite a placa do carro(formato: ZZZ9999) que você deseja ou digite 'Voltar' para voltar para a tela anterior")
            if(car_plate == "Voltar"):
                self.open()
            else:
                self.add(self.__request_controller.main_controller.user, car_plate)
        elif(option == 2):
            request = self.__request_controller.get_request_by_user(self.__request_controller.main_controller.user)
            self.__request_controller.return_key(request)
            print("Chave Devolvida")
        elif(option == 3):
            id_request = input("Digite o id da requisição que você deseja deletar:")
            request = self.__request_controller.get_request_by_id(id_request)
            self.__request_controller.delete_request(request)
        elif(option == 4):
            self.__request_controller.open_main_screen()
        else:
            self.open()


    def add(self, user, car_plate):
        self.__request_controller.add_request(user, car_plate)

    def edit(self, request, id_request):
        self.__request_controller.edit_request(request, id_request)

    def delete(self, request):
        self.__request_controller.delete_request(request)

    def open_main_screen(self):
        self.__request_controller.open_main_screen()

    def show_is_blocked_message(self):
        print("Você tentou mais de 3 vezes acessar esse mesmo veículo, você está bloqueado")
