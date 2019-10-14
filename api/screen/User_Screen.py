# Models
from api.model import User

# Views
from api.screen.General_Screen import GeneralScreen
from api.screen.Main_Screen import MainScreen


# Controllers


class UserScreen(GeneralScreen):

    def __init__(self, user_controller=None):
        super().__init__(user_controller)

    def add(self,
            id_user,
            user_name,
            user_birthday,
            user_role,
            user_phone):
        return super().controller.add_user(
            id_user,
            user_name,
            user_birthday,
            user_role,
            user_phone
        )

    def delete(self, id_user: int):
        return super().controller.delete_user(id_user)

    def edit(self, user: User, id_user: int):
        return super().controller.edit_user(user, id_user)

    # @staticmethod
    # def open_main_screen():
    #     MainScreen.open()

    def open(self):
        print(" --- User Screen --- ")
        print(" | Você Deseja:  | ")
        print(" | Inserir User [1]  | ")
        print(" | Deletar User [2]  | ")
        print(" | Editar User [3]  | ")
        print(" | Listar Users [4]  | ")
        print(" | Voltar Para o Menu[5] | ")
        while True:
            option = int(input("Insira a opção desejada: "))
            if option == 1:
                self.open_add_menu()
            elif option == 2:
                self.open_delete_menu()
            elif option == 3:
                self.open_edit_menu()
            elif option == 4:
                self.list_users()
            elif option == 5:
                pass
            else:
                print("Opção Inválida")

    def open_add_menu(self):
        print(" --- Cadastro de Usuário --- ")
        id = int(input(" | Matrícula:  | "))
        name = input(" | Nome:  | ")
        birthdate = input(" | Data de Nascimento:  | ")
        print(" | Insira o Código do Cargo: | ")
        print(" | | CEO[0] Gerente[1] Empregado[2] Estagiário[3] | | ")
        role = None
        while role is None:
            input_role = int(input(" | Insira o Código do Cargo:  | "))
            if 0 >= input_role <= 3:
                role = input_role
            else:
                print(" !!!Opção Inválida!!! ")
        phone = int(input(" | Telefone:  | "))
        return self.add(id, name, birthdate, role, phone)

    def open_delete_menu(self):
        print(" --- Remoção de Usuário --- ")
        id_user = int(input(" | Insira a Matrícula do Usuário:  |"))
        deleted = self.delete(id_user)
        if deleted:
            print(" | Usuário Apagado do Sistema | ")
        else:
            print(" !!! Não foi possível apagar o usuário !!!")

    def open_edit_menu(self):
        print(" --- Edição de Usuário --- ")

    def list_users(self):
        print(" --- Listagem de Usuário --- ")
        users = super().controller.users
        if users is not None:
            user_number = 1
            for user in users:
                user_array = user.to_array()
                print(" *** Usuário "+str(user_number)+" *** ")
                for key in user_array:
                    print(" | %s => %s | " % (key, user_array[key]))
                user_number = user_number + 1
