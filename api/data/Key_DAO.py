from api.data.DAO import DAO
from api.model.Key import Key


class KeyDAO(DAO):
    def __init__(self):
        super().__init__('keys.pkl')

    def add(self, index, key: Key):
        if (isinstance(key.id_key, int)) and (key is not None) \
                and isinstance(key, Key) and (index == key.id_key):
            super().add(index, key)

    def get(self, index: int):
        if index is not None and isinstance(index, int):
            return super().get(index)

    def remove(self, index):
        if index is not None and isinstance(index, int):
            return super().remove(index)
