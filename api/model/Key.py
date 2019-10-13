from Car import Car

class Key():
  def __init__(self, id_key: int, car: Car):
    self.__id_key = id_key
    self.__car = car
  
  @property
  def id_key(self):
    return self.__id_key
  
  @property
  def car(self):
    return self.__car
  
  @id_key.setter
  def id_key(self, id_key: int):
    self.__id_key = id_key
  
  @car.setter
  def car(self, car: Car):
    self.__car = car