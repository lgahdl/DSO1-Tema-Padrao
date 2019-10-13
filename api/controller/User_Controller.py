# Models
from ..model import User

# Views
from ..screen.User_Screen import UserScreen
from ..screen.Main_Screen import MainScreen

# Controllers
from ..controller.General_Controller import GeneralController


class UserController(GeneralController):

    def __init__(self, users: [User], user_screen: UserScreen):
        self.__users = users
        self.__user_screen = user_screen

    def add_user(self, user: User):
        users = self.__users
        for userController in users:
            if userController.id != user.id and \
                    userController.name != user.user_name:
                self.__users.append(user)

    def delete_user(self, id_user: int):
        users = self.__users
        for userController in users:
            if userController.id == id_user:
                self.__users.remove(userController)

    def edit_user(self, user: User, id_user: int):
        users = self.__users
        for userController in users:
            if userController.id == id_user:
                index = users.index(userController)
                self.__users[index] = user

    def open_user_screen(self):
        self.__user_screen.open()

    @staticmethod
    def open_main_screen():
        MainScreen.open()

    def get_user_by_id(self, id_user):
        for user in self.__users:
            if user.id == id_user:
                return user
