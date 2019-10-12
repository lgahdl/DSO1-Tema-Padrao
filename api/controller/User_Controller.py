from ..controller import Gerenal_Controller
from ..model import User


class UserController(Gerenal_Controller):

    def __init__(self, user_screen: User_Screen):
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
