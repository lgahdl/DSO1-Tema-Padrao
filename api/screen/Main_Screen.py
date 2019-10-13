from General_Screen import General_Screen
from ..controller.General_Controller import General_Controller

class Main_Screen(General_Screen):

  def __init__(self, general_controller: General_Controller):
    super.__init__()
    self.__general_controller = general_controller
  
  def open(self):
    id_user = raw_input('Olá, por favor, digite sua Matrícula')
    user_phone = raw_input('Agora digite seu número de Telefone')
    self.login()


