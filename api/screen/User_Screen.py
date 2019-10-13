from ..screen import General_Screen
from ..controller import User_Controller
from ..model import User


class UserScreen(General_Screen):

    def __init__(self, user_controller: User_Controller):
        self.user_controller = user_controller

    def add_user(self):
        return self.__user_controller.add_user()

    def delete_user(self, user: User):
        return self.__user_controller.delete_user(user)

    def edit_user(self, user: User):
        return self.__user_controller.edit_user(User.id())

    def open_main_screen(self):
        return General_Screen()
