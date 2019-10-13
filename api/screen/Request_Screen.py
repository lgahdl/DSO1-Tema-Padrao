from General_Screen import General_Screen
from ..controller.Request_Controller import Request_Controller

class Request_Screen():

  def __init__(self, request_controller: Request_Controller):
    self.__request_controller = super().__init__(request_controller)
  
  @property
  def request_controller(self):
    return self.__request_controller
  
  @request_controller.setter
  def request_controller(self, request_controller):
    self.__request_controller = request_controller
  
  def add_request(self, user, car):
    self.__request_controller.add_request(user, car)
  
  def edit_request(self, request, id_request):
    self.__request_controller.edit_request(request, id_request)
  
  def delete_request(self, request):
    self.__request_controller.delete_request(request)
  
  def open_main_screen(self):
    self.__request_controller.open_main_screen()
