import sys
print("Bem-vindo ao seu app de Contatos.")

agenda = []
operacao = ""
while operacao != "6":
    print()
    print("### MENU ###")
    print("Operações possíveis:")
    print("1 - Salvar")
    print("2- Editar")
    print("3 - Listar")
    print("4 - Pesquisar")
    print("4 - Deletar")
    print("6 - Sair")
    operacao = input("Escolha uma operação acima pelo seu numero: ")

    if operacao == "1":
        print("A seguir, insira os dados do usuário que você deseja armazenar.")
        novo_contato = {}

        nome_contato = input("Nome: ")
        # validando nome do contato
        if not nome_contato:
            print("Nao é possível continuar sem um nome do contato.")
            sys.exit(1)
        elif len(nome_contato) > 10:
            print("O nome nao pode ter mais que 10 chars")
            sys.exit(1)
        novo_contato["nome_contato"] = nome_contato

        sobrenome_contato = input("Sobrenome: ")
        # validando sobrenome do contato
        if not sobrenome_contato:
            print("Nao é possível continuar sem um sobrenome do contato.")
            sys.exit(1)
        elif len(sobrenome_contato) > 10:
            print("O sobrenome nao pode ter mais que 10 chars")
            sys.exit(1)
        novo_contato["sobrenome_contato"] = sobrenome_contato

        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        # validando data de nascimento
        if not data_nascimento:
            print("Nao é possível continuar sem uma data de nascimento.")
            sys.exit(1)
        elif len(data_nascimento) > 10:
            print("Data de nascimento nao pode ter mais que 10 chars")
            sys.exit(1)
        novo_contato["data_nascimento"] = data_nascimento

        telefone_contato = input("Numero do telefone: ")
        # validando num. telefone
        if not telefone_contato:
            print("Nao é possível continuar sem um numero de telefone.")
            sys.exit(1)
        elif len(telefone_contato) > 11:
            print("Numero de telefone nao pode ter mais que 11 chars")
            sys.exit(1)
        novo_contato["telefone_contato"] = telefone_contato


        print("Dados do contato validados e serão salvos...")
        agenda.append(novo_contato)

    elif operacao == "3":
        for contato in agenda:
            for chave, valor in contato.items():
                print(f"{chave.replace('contato', '').replace('_', ' ').title().strip()}: {valor}")
            print()