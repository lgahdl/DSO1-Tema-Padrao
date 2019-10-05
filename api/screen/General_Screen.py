from abc import ABC, abstractmethod
from ..controller import Gerenal_Controller as ABCController


class GeneralScreen(ABC):

    @abstractmethod
    def __init__(self, controller: ABCController):
        pass
