from Pessoa import Pessoa

class Control:

    def __init__(self):
        self.person = Pessoa()

    def Coletar(self):
        print("Informe seu nome: ")
        self.person.setNome(input())
        print("Informe seu telefone: ")
        self.person.setTelefone(input())
        print("Informe seu endereço: ")
        self.person.setEndereco(input())

    def Mostrar(self):
        print(self.person.consultarUsuario())