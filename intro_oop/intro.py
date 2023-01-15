class Contato:
    def __init__(self, nome, sobrenome, data_nascimento, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def __str__(self):
        return f"{self.nome_completo()} - {self.telefone}"

contato_1 = Contato("Bruce", "Wayne", "12/12/1980", "11999990000")
contato_2 = Contato(nome="Bruce", data_nascimento="06/06/1666", telefone="016677889900", sobrenome="Dickinson")


nome_comp = contato_1.nome_completo()
# nome_comp = Contato.nome_completo(contato_1)

print(nome_comp)