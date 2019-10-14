from ..screen.Main_Screen import MainScreen
from api.controller.General_Controller import GeneralController


class MainController(GeneralController):

    def __init__(self):
        pass

    identifier = ''
    phone = ''

    def start(self):
        MainScreen(self).open()

    def login(self, identifier: str, phone: str):
        self.identifier = identifier
        self.phone = phone

    def logout(self):
        self.identifier = ''
        self.phone = ''

    def open_screen(self):
        MainScreen(self).open()