from ..controller import Gerenal_Controller


class UserController(Gerenal_Controller):

    def __init__(self, users: [], user_screen: User_Screen):
        self.__users = users
        self.__user_screen = user_screen

    def add_user(self):
        pass

    def delete_user(self):
        pass

    def edit_user(self, id_user: int):
        pass

    def open_user_screen(self):
        pass

    def open_main_screen(self):
        pass
