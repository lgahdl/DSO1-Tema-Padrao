# Utils
from datetime import date

# Models
from ..model.General_Model import GeneralModel
from ..model.Key import Key
from ..model.User import User


class Request(GeneralModel):

    def __init__(self, id_request: int, user: User, key: Key,
                 created_date: date, devolution_date: date, accepted: bool, reason: str):
        super().__init__()
        self.__id_request = id_request
        self.__user = user
        self.__key = key
        self.__created_date = created_date
        self.__devolution_date = devolution_date
        self.__accepted = accepted
        self.__reason = reason

    """
    |--------------|
    |   GETTERS    |
    |--------------|
    """

    @property
    def id(self):
        return self.__id_request

    @property
    def user(self):
        return self.__user

    @property
    def key(self):
        return self.__key

    @property
    def created_date(self):
        return self.__created_date

    @property
    def devolution_date(self):
        return self.__devolution_date

    @property
    def accepted(self):
        return self.__accepted

    @property
    def reason(self):
        return self.__reason

    """
    |--------------|
    |   SETTERS    |
    |--------------|
    """

    @id.setter
    def id(self, id_request):
        self.__id_request = id_request

    @user.setter
    def user(self, user):
        self.__user = user

    @key.setter
    def key(self, key):
        self.__key = key

    @created_date.setter
    def created_date(self, created_date):
        self.__created_date = created_date

    @devolution_date.setter
    def devolution_date(self, devolution_date):
        self.__devolution_date = devolution_date

    @accepted.setter
    def accepted(self, accepted):
        self.__accepted = accepted

    @reason.setter
    def reason(self, reason):
        self.__reason = reason
