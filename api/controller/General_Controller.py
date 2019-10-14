from abc import ABC, abstractmethod


class GeneralController(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_screen(self):
        pass

    @abstractmethod
    def destroy_screen(self):
        pass

    @abstractmethod
    def open_main_screen(self):
        pass

    @abstractmethod
    def create_dependencies_by_list(self, dependencies_list: []):
        pass
