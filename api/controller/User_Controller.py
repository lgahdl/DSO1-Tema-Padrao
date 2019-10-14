# Utils
from datetime import date as Date

# Models
from api.model.User import User

# Views
from api.screen.User_Screen import UserScreen

# Controllers
from api.controller.General_Controller import GeneralController


class UserController(GeneralController):

    def __init__(self, main_controller, users=None):
        super().__init__()
        if users is None:
            users = []
        self.__users = users
        self.__main_controller = main_controller
        self.create_screen()

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def users(self):
        return self.__users

    def create_screen(self):
        self.__user_screen = UserScreen(self)

    def destroy_screen(self):
        if self.__user_screen is not None:
            del self.__user_screen

    def create_dependencies_by_list(self, dependencies_list: []):
        for encapsulated_user in dependencies_list:
            self.add_user(
                encapsulated_user['id_user'],
                encapsulated_user['user_name'],
                encapsulated_user['user_birthday'],
                encapsulated_user['user_role'],
                encapsulated_user['user_phone'],
                encapsulated_user['cars'],
            )

    def add_user(
            self,
            id_user: int,
            user_name: str,
            user_birthday: Date,
            user_role: int,
            user_phone: int,
            cars: [] = []
    ) -> User:
        user = User(id_user, user_name, user_birthday, user_role, user_phone, cars)
        users = self.__users
        if users is None or users == []:
            self.__users.append(user)
        else:
            for controller_user in users:
                if controller_user.id != user.id and \
                        controller_user.user_name != user.user_name:
                    self.__users.append(user)
        return user

    def delete_user(self, id_user: int):
        users = self.__users
        for controller_user in users:
            if controller_user.id == id_user:
                self.__users.remove(controller_user)
                return True

    def edit_user(self, user: User, id_user: int):
        users = self.__users
        for controller_user in users:
            if controller_user.id == id_user:
                index = users.index(controller_user)
                self.__users[index] = user

    def open_user_screen(self):
        self.__user_screen.open()

    def open_main_screen(self):
        self.destroy_screen()
        self.__main_controller.open_main_screen()

    def get_user_by_id(self, id_user):
        for user in self.__users:
            if user.id == id_user:
                return user
