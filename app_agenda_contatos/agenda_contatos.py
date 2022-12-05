import sys
print("Bem-vindo ao seu app de Contatos.")
print("A seguir, insira os dados do usuário que você deseja armazenar.")


nome_contato = input("Nome: ")
# validando nome do contato
if not nome_contato:
    print("Nao é possível continuar sem um nome do contato.")
    sys.exit(1)
elif len(nome_contato) > 10:
    print("O nome nao pode ter mais que 10 chars")
    sys.exit(1)

sobrenome_contato = input("Sobrenome: ")
# validando sobrenome do contato
if not sobrenome_contato:
    print("Nao é possível continuar sem um sobrenome do contato.")
    sys.exit(1)
elif len(sobrenome_contato) > 10:
    print("O sobrenome nao pode ter mais que 10 chars")
    sys.exit(1)

data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
# validando data de nascimento
if not data_nascimento:
    print("Nao é possível continuar sem uma data de nascimento.")
    sys.exit(1)
elif len(data_nascimento) > 10:
    print("Data de nascimento nao pode ter mais que 10 chars")
    sys.exit(1)

telefone_contato = input("Numero do telefone: ")
# validando num. telefone
if not telefone_contato:
    print("Nao é possível continuar sem um numero de telefone.")
    sys.exit(1)
elif len(telefone_contato) > 11:
    print("Numero de telefone nao pode ter mais que 11 chars")
    sys.exit(1)


print("Dados do contato validados e serão salvos...")

# aqui precisamos de persistir os dados que o usuario entrou de alguma forma.
# Mas como?

