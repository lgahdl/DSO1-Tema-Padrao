# Models
from api.model import User

# Views
from api.screen.General_Screen import GeneralScreen

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
        print(" User Screen ".center(60, "-"))
        print(" | Você Deseja:  | ".center(60))
        print(" | Inserir User [1]  | ".center(60))
        print(" | Deletar User [2]  | ".center(60))
        print(" | Editar User [3]  | ".center(60))
        print(" | Listar Users [4]  | ".center(60))
        print(" | Voltar Para o Menu[5] | ".center(60))
        while True:
            option = int(input(" Insira a opção desejada: ".center(60)))
            if option == 1:
                self.open_add_menu()
            elif option == 2:
                self.open_delete_menu()
            elif option == 3:
                self.open_edit_menu()
            elif option == 4:
                self.open_list_menu()
            elif option == 5:
                self.open_main_screen()
            else:
                print("Opção Inválida".center(60, "-"))

    def open_add_menu(self):
        print(" Cadastro de Usuário ".center(60, "-"))
        id = int(input(" | Matrícula:  | ".center(60)))
        name = input(" | Nome:  | ".center(60))
        birth_date = input(" | Data de Nascimento:  | ".center(60))
        print(" | Insira o Código do Cargo: | ".center(60))
        print(" | | CEO[3] Gerente[2] Empregado[1] Estagiário[0] | | ".center(60))
        role = None
        while role is None:
            input_role = int(input(" | Insira o Código do Cargo:  | ".center(60)))
            if 0 <= input_role <= 3:
                role = input_role
            else:
                print(" !!!Opção Inválida!!! ".center(60))
        phone = int(input(" | Telefone:  | ".center(60)))
        return self.add(id, name, birth_date, role, phone)

    def open_delete_menu(self):
        print(" Remoção de Usuário ".center(60, "-"))
        id_user = int(input(" | Insira a Matrícula do Usuário:  |".center(60)))
        deleted = self.delete(id_user)
        if deleted:
            print(" | Usuário Apagado do Sistema | ".center(60))
        else:
            print(" !!! Não foi possível apagar o usuário !!!".center(60))

    def open_edit_menu(self):
        print(" Edição de Usuário ".center(60, "-"))
        user_id = int(input(" Insira a Matrícula do usuário ".center(60)))
        user = super().controller.get_user_by_id(user_id)
        user_array = user.to_array()
        for key in user_array:
            if key == "Data de Nascimento":
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
                birth_date = input(" Nova Data de Nascimento ".center(60))
                if birth_date is None:
                    birth_date = user.user_birthday
                user.user_birthday = birth_date
            elif key == "Cargo":
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
                print(" | Insira o Código do Cargo: | ".center(60))
                print(" | | CEO[3] Gerente[2] Empregado[1] Estagiário[0] | | ".center(60))
                role = None
                while role is None:
                    input_role = int(input(" | Código:  | ".center(60)))
                    if 0 <= input_role <= 3:
                        role = input_role
                    elif role is None:
                        role = user.user_role
                    else:
                        print(" !!!Opção Inválida!!! ".center(60))
                user.user_role = role
            elif key == "Telefone":
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
                phone = int(input(" Novo Telefone ".center(60))) or user.user_phone
                user.user_phone = phone
            else:
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
        return super().controller.edit_user(user, user_id)

    def open_list_menu(self):
        print(" Listagem de Usuário ".center(60, "-"))
        users = super().controller.users
        if users is not None:
            user_number = 1
            for user in users:
                user_array = user.to_array()
                print((" *** Usuário "+str(user_number)+" *** ").center(60))
                for key in user_array:
                    string = (" | %s => %s | " % (key, user_array[key]))
                    print(string.center(60))
                user_number = user_number + 1

    def open_main_screen(self):
        super().controller.open_main_screen()
