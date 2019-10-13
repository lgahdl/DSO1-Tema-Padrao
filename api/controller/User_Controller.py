# Models
from ..model import User

# Views
from ..screen.User_Screen import UserScreen

# Controllers
from ..controller.General_Controller import GeneralController


class UserController(GeneralController):

    def __init__(self, users: [User], user_screen: UserScreen):
        self.__users = users
        self.__user_screen = user_screen

    def add_user(self):
        pass

    def delete_user(self, user: User):
        pass

    def edit_user(self, id_user: int):
        pass

    def open_user_screen(self):
        pass

    def open_main_screen(self):
        pass

    def get_user_by_id(self, id_user):
        for user in self.__users:
            if user.id == id_user:
                return user
