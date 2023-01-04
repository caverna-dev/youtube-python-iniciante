class Disciplina():

    def __init__(self):
    pass

d1 = Disciplina()
d2 = Disciplina()

d1.nome = "Programacao I"
d1.professor = "Fulaninho"
d1.curso = "Eng de Computacao"
d1.media_aprovacao = 7.0
d1.ativa = True

print(d1.__dict__)
print(d2.__dict__)

