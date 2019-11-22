from api.data.DAO import DAO
from api.model.User import User


class UserDAO(DAO):
    def __init__(self):
        super().__init__('data/users.pkl')

    def add(self, key, user: User):
        if (isinstance(user.id_user, int)) and (user is not None) \
                and isinstance(user, User) and (key == user.id_user):
            print(1235)
            super().add(key, user)

    def get(self, key: int):
        if key is not None and isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if key is not None and isinstance(key, int):
            return super().remove(key)
