# Models
from api.model import User

# Views
from api.screen.General_Screen import GeneralScreen

# Controllers

# PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg


class UserScreen(GeneralScreen):

    def __init__(self, user_controller):
        super().__init__(user_controller)
        self.init_menu_components()

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

    def add_user_with_array(self, user_array):
        super().controller.add_user_with_array(user_array)
        self.close_gui()
        self.init_menu_components()
        self.open_gui('menu')

    def delete(self, id_user: int):
        return super().controller.delete_user(id_user)

    def edit(self, user: User, id_user: int):
        return super().controller.edit_user(user, id_user)

    def open(self):
        super().open()

    def init_menu_components(self):

        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Usuário')],
            [sg.Text('Você deseja:')],
            [sg.Button('Inserir', key='INSERT_BUTTON')],
            [sg.Button('Deletar', key='DELETE_BUTTON')],
            [sg.Button('Editar', key='EDIT_BUTTON')],
            [sg.Button('Listar', key='LIST_BUTTON')],
            [],
            [sg.Button('Sair', key='EXIT_BUTTON')],
        ]
        self.__window = sg.Window('Usuários').Layout(layout)

    def init_insert_components(self):
  
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Adição de Usuário', size=[30, 1])],
            [sg.Text(
                'Digite os dados do Usuário que você deseja adicionar:', size=[30, 1])],
            [sg.Text('Matricula', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Nome', size=[15, 1]), sg.InputText('', size=[30, 1])],
            [sg.Text('Data de Nascimento', size=[15, 1]),
             sg.InputText('dd/mm/YYYY', size=[30, 1])],
            [sg.Text('Telefone', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Cargo', size=[15, 1]), sg.InputCombo(
                ('Estagiário', 'Empregado', 'Gerente', 'CEO'), size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Adição de Usuários').Layout(layout)

        self.open_gui('insert')

    def init_delete_components(self):
  
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Remoção de Usuário')],
            [sg.Text(
                'Digite a Matricula do Usuário que você deseja remover:', size=[30, 1])],
            [sg.Text('Matricula:', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()],
        ]
        self.__window = sg.Window('Usuários').Layout(layout)

        self.open_gui('delete')

    def init_edit_components(self):
  
        sg.ChangeLookAndFeel('Reddit')

        layout = [
            [sg.Text('Tela de Edição de Usuário', size=[30, 1])],
            [sg.Text(
                'Digite a matrícula do Usuário que você deseja editar:', size=[30, 1])],
            [sg.Text('Matricula(não pode ser editada)', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text(
                'Digite os novos dados do usuário:'
            )],
            [sg.Text('Nome', size=[15, 1]), sg.InputText('', size=[30, 1])],
            [sg.Text('Data de Nascimento', size=[15, 1]),
             sg.InputText('dd/mm/YYYY', size=[30, 1])],
            [sg.Text('Telefone', size=[15, 1]),
             sg.InputText('', size=[30, 1])],
            [sg.Text('Cargo', size=[15, 1]), sg.InputCombo(
                ('Estagiário', 'Empregado', 'Gerente', 'CEO'), size=[30, 1])],
            [],
            [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Edição de Usuários').Layout(layout)

        self.open_gui('edit')

    def init_list_components(self):
  
        users = super().controller.users
        user_layout_array = []
        index = 0
        for user in users:
            print(user.user_name)
            user_layout_array.append(
                [sg.Text('Usuário nº', size=[15, 1]),
                 sg.Text(index, size=[30, 1])])
            user_layout_array.append(
                [sg.Text('Matricula', size=[15, 1]),
                 sg.Text(user.id_user, size=[30, 1])])
            user_layout_array.append(
                [sg.Text('Nome', size=[15, 1]),
                 sg.Text(user.user_name, size=[30, 1])])
            user_layout_array.append(
                [sg.Text('Data de Nascimento', size=[15, 1]),
                 sg.Text(user.user_birthday, size=[30, 1])])
            user_layout_array.append(
                [sg.Text('Telefone', size=[15, 1]),
                 sg.Text(user.user_phone, size=[30, 1])])
            user_layout_array.append(
                [sg.Text('Cargo', size=[15, 1]),
                 sg.Text(user.user_role, size=[30, 1])])
            user_layout_array.append([])
            index += 1
        user_layout_array.append(
            [sg.OK()]
        )

        sg.ChangeLookAndFeel('Reddit')

        layout = user_layout_array

        self.__window = sg.Window('Usuários').Layout(layout)

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
                super().controller.open_main_screen()

        elif(screen_type == 'insert'):
            button, values = self.__window.Read()
            print(button)
            if(button == 'Cancel' or button == None):
                self.back_handler()
            print(values)
            return self.add_user_with_array(values)

        elif(screen_type == 'delete'):
            button, values = self.__window.Read()
            print(values)
            deleted = self.delete(int(values[0]))
            if(button == 'Cancel' or button == None):
                self.back_handler()
            if deleted:
                sg.Popup("Usuário Apagado do Sistema")
                self.init_menu_components()
                self.open_gui('menu')
            else:
                sg.Popup("Não foi possível apagar o usuário !!!")
                self.init_menu_components()
                self.open_gui('menu')

        elif(screen_type == 'edit'):
            button, values = self.__window.Read()
            print(values)
            if(button == 'Cancel' or button == None):
                self.back_handler()
            super().controller.edit_user(values)

            self.init_menu_components()
            self.open_gui('menu')

        elif(screen_type == 'list'):
            button, values = self.__window.Read()
            if(button == 'OK' or button == None):
                self.back_handler()
            print(values)
            self.init_menu_components()
            self.open_gui('menu')

        if(isinstance(values[0], int) and values[0] <= -1 and values[0] >= -5):
            if(values[0] == -1):
                super().controller.open_main_screen()
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

    # def open_add_menu(self):
    #     print(" Cadastro de Usuário ".center(60, "-"))

    #     user_id = int(input(" | Matrícula  | ".center(60)))
    #     user_name = input(" | Nome  | ".center(60))
    #     user_birth_date = input(" | Data de Nascimento  | ".center(60))
    #     user_phone = int(input(" | Telefone  | ".center(60)))

    #     print(" | Insira o Código do Cargo: | ".center(60))
    #     print(
    #         " | | CEO[3] Gerente[2] Empregado[1] Estagiário[0] | | ".center(60))
    #     user_role = None
    #     while user_role is None:
    #         input_role = int(
    #             input(" | Insira o Código do Cargo  | ".center(60)))
    #         if 0 <= input_role <= 3:
    #             user_role = input_role
    #         else:
    #             print(" !!!Opção Inválida!!! ".center(60))
    #     return self.add(user_id, user_name, user_birth_date, user_role, user_phone)

    # def open_delete_menu(self):
    #     print(" Remoção de Usuário ".center(60, "-"))
    #     user_id = int(input(" | Insira a Matrícula do Usuário  |".center(60)))
    #     deleted = self.delete(user_id)
    #     if deleted:
    #         print(" | Usuário Apagado do Sistema | ".center(60))
    #     else:
    #         print(" !!! Não foi possível apagar o usuário !!!".center(60))

    # def open_edit_menu(self):
    #     print(" Edição de Usuário ".center(60, "-"))
    #     user_id = int(input(" Insira a Matrícula do usuário ".center(60)))
    #     user = super().controller.get_user_by_id(user_id)
    #     user_array = user.to_array()
    #     for key in user_array:
    #         if key == "Data de Nascimento":
    #             string = (" | %s => %s | " % (key, user_array[key]))
    #             print(string.center(60))
    #             birth_date = input(" Nova Data de Nascimento ".center(
    #                 60)) or user.user_birthday
    #             user.user_birthday = birth_date
    #         elif key == "Cargo":
    #             string = (" | %s => %s | " % (key, user_array[key]))
    #             print(string.center(60))
    #             print(" | Insira o Código do Cargo: | ".center(60))
    #             print(
    #                 " | | CEO[3] Gerente[2] Empregado[1] Estagiário[0] | | ".center(60))
    #             role = None
    #             while role is None:
    #                 input_role = input(" | Código  | ".center(60))
    #                 if input_role is None or input_role is '':
    #                     for KEY in user.permission_role:
    #                         if user.permission_role[KEY] == user.user_role:
    #                             input_role = KEY
    #                 input_role = int(input_role)
    #                 if 0 <= input_role <= 3 and input_role is not None:
    #                     role = input_role
    #                 else:
    #                     print(" !!!Opção Inválida!!! ".center(60))
    #             user.user_role = int(role)
    #         elif key == "Telefone":
    #             string = (" | %s => %s | " % (key, user_array[key]))
    #             print(string.center(60))
    #             phone = input(" Novo Telefone ".center(60)) or user.user_phone
    #             user.user_phone = int(phone)
    #         else:
    #             string = (" | %s => %s | " % (key, user_array[key]))
    #             print(string.center(60))
    #     return super().controller.edit_user(user, user_id)

    # def open_list_menu(self):
    #     print(" Listagem de Usuários ".center(60, "-"))
    #     users = super().controller.users
    #     if users is not None:
    #         user_number = 1
    #         for user in users:
    #             user_array = user.to_array()
    #             print("\n")
    #             print((" *** Usuário "+str(user_number)+" *** ").center(60))
    #             for key in user_array:
    #                 string = (" | %s => %s | " % (key, user_array[key]))
    #                 print(string.center(60))
    #             user_number = user_number + 1

    def open_main_screen(self):
        super().open_main_screen()
    
    def back_handler(self):
        self.close_gui()
        self.init_menu_components()
        self.open_gui('menu')
