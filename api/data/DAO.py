import pickle
from abc import ABC, abstractmethod


class DAO(ABC):
    def __init__(self, data_source=''):
        self.__data_source = data_source
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__data_source, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__data_source, 'rb'))

    def add(self, index, model):
        self.__cache[index] = model
        self.__dump()

    @abstractmethod
    def get(self, index):
        try:
            return self.__cache[index]
        except KeyError:
            pass

    @abstractmethod
    def remove(self, index):
        try:
            self.__cache.pop(index)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()
