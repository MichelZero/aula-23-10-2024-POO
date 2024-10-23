#
#
#
# autor: Michel
# data: 23/10/2024

#classe 1
class Classe01:
  nome1_1 = "classe01"
  def __init__(self):
    self.nome1_4 = "nome4"
    
#classe2
class Classe02(Classe01):
  nome2_3 = "classe2"
  def __init__(self):
    super().__init__()
    self.nome2_2 = "pedro"


# teste
c1 = Classe01()
c2 = Classe02()
print(dir(c1))
