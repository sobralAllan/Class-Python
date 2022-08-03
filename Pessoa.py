class Pessoa:
    def __init__(self):
        self.nome = ""
        self.telefone = ""
        self.endereco = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

    def cadastrarUSuario(self, nome, telefone, endereco):
        self.setNome(nome)
        self.setTelefone(telefone)
        self.setEndereco(endereco)

    def consultarUsuario(self):
        return "Nome: {}, \nTelefone: {}, \nEndereço: {}".format(self.getNome(), self.getTelefone(), self.getEndereco())

