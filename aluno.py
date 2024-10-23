from pessoa import Pessoa as P

class Aluno(P):
  def __init__(self, nome, idade, matricula):
    super().__init__(nome, idade) # inicializa a classe mãe/pai com os atributos nome e idade 
    self.matricula = matricula

  def falar(self):
    print("Olá, meu nome é " + self.nome)

  def estudar(self):
    print("Estou estudando")