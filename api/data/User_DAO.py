from api.data.DAO import DAO
from api.model.User import User


class UserDAO(DAO):
    def __init__(self):
        super().__init__('users.pkl')

    def add(self, index, user: User):
        if (isinstance(user.id_user, int)) and (user is not None) \
                and isinstance(user, User) and (index == user.id_user):
            super().add(index, user)

    def get(self, index: int):
        if index is not None and isinstance(index, int):
            return super().get(index)

    def remove(self, index):
        if index is not None and isinstance(index, int):
            return super().remove(index)
