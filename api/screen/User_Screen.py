# Models
from ..model import User

# Views
from ..screen.General_Screen import GeneralScreen

# Controllers
from ..controller.User_Controller import UserController


class UserScreen(GeneralScreen):

    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller

    def add(self):
        return self.__user_controller.add_user()

    def delete(self, user: User):
        return self.__user_controller.delete_user(user)

    def edit(self, user: User):
        return self.__user_controller.edit_user(User.id())

    def open_main_screen(self):
        return GeneralScreen()
