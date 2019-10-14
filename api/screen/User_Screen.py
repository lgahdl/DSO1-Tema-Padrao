# Models
from api.model import User

# Views
from api.screen.General_Screen import GeneralScreen

# Controllers


class UserScreen(GeneralScreen):

    def __init__(self, user_controller):
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

    def open(self):
        super().open()

    def open_add_menu(self):
        print(" Cadastro de Usuário ".center(60, "-"))

        user_id = int(input(" | Matrícula  | ".center(60)))
        user_name = input(" | Nome  | ".center(60))
        user_birth_date = input(" | Data de Nascimento  | ".center(60))
        user_phone = int(input(" | Telefone  | ".center(60)))

        print(" | Insira o Código do Cargo: | ".center(60))
        print(" | | CEO[3] Gerente[2] Empregado[1] Estagiário[0] | | ".center(60))
        user_role = None
        while user_role is None:
            input_role = int(input(" | Insira o Código do Cargo  | ".center(60)))
            if 0 <= input_role <= 3:
                user_role = input_role
            else:
                print(" !!!Opção Inválida!!! ".center(60))
        return self.add(user_id, user_name, user_birth_date, user_role, user_phone)

    def open_delete_menu(self):
        print(" Remoção de Usuário ".center(60, "-"))
        user_id = int(input(" | Insira a Matrícula do Usuário  |".center(60)))
        deleted = self.delete(user_id)
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
                birth_date = input(" Nova Data de Nascimento ".center(60)) or user.user_birthday
                user.user_birthday = birth_date
            elif key == "Cargo":
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
                print(" | Insira o Código do Cargo: | ".center(60))
                print(" | | CEO[3] Gerente[2] Empregado[1] Estagiário[0] | | ".center(60))
                role = None
                while role is None:
                    input_role = input(" | Código  | ".center(60))
                    if input_role is None or input_role is '':
                        for KEY in user.permission_role:
                            if user.permission_role[KEY] == user.user_role:
                                input_role = KEY
                    input_role = int(input_role)
                    if 0 <= input_role <= 3 and input_role is not None:
                        role = input_role
                    else:
                        print(" !!!Opção Inválida!!! ".center(60))
                user.user_role = int(role)
            elif key == "Telefone":
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
                phone = input(" Novo Telefone ".center(60)) or user.user_phone
                user.user_phone = int(phone)
            else:
                string = (" | %s => %s | " % (key, user_array[key]))
                print(string.center(60))
        return super().controller.edit_user(user, user_id)

    def open_list_menu(self):
        print(" Listagem de Usuários ".center(60, "-"))
        users = super().controller.users
        if users is not None:
            user_number = 1
            for user in users:
                user_array = user.to_array()
                print("\n")
                print((" *** Usuário "+str(user_number)+" *** ").center(60))
                for key in user_array:
                    string = (" | %s => %s | " % (key, user_array[key]))
                    print(string.center(60))
                user_number = user_number + 1

    def open_main_screen(self):
        super().open_main_screen()
