class Pessoa:
    MAX_LEN_NOME = 10
    MAX_LEN_SOBRENOME = 10
    MAX_LEN_DATA = 10

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"{self.nome_completo}"

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if len(valor) <= self.MAX_LEN_NOME:
            self._nome = valor
        else:
            raise ValueError(f"O atributo 'nome' pode ter no maximo {self.MAX_LEN_NOME}")


    @classmethod
    def metodo_classe(cls):
        # metodos de classe sao utilziados para manipular a propria class
        # e nao uma instancia em particular. Um caso de uso comum para
        # eses tipos de metodos é na criaçao de "factory methods".
        pass

    @staticmethod
    def metodo_estatico(arg1, arg2):
        pass



class Contato:

    def __init__(self, pessoa, telefone, email):
        self.pessoa = pessoa
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.pessoa.nome_completo} - {self.telefone} - {self.email}"


p1 = Pessoa("Bruce", "Wayne", "12/12/1980")
print(p1.nome) # retorna o atributo 'nome'
p1.nome = "Beiçola da pastelaria" # altera o atributo 'nome'
print(p1.nome)

# print(p1)
# c1 = Contato(p1, "11111111", "bats@gotahm.com")
# print(c1)

