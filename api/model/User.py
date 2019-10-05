from ..model import General_Model


class User(General_Model):

    def __init__(self, id_user: int):
        self.__id_user = id_user

    @property
    def id(self):
        return self.__id_user
    
    @id.setter
    def id(self, id_user: int):
        self.__id_user = id_user
