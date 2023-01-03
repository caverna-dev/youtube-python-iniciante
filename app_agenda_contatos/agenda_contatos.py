import sys
from datetime import datetime

def validacao_generica(nome_atributo, valor_atributo, max_len):
    if not valor_atributo:
        print(f"Nao é possível continuar sem um '{nome_atributo}'.")
        sys.exit(1)
    elif len(valor_atributo) > max_len:
        print(f"O campo '{nome_atributo}' nao pode ter mais que {max_len} chars")
        sys.exit(1)

def valida_telefone(telefone):
    if not telefone.isnumeric():
        print("Um numero de telefone precisa ser composto apenas por caracteres numericos")
        sys.exit(1)

def valida_data(data):
    try:
        data_validada = datetime.strptime(data, "%d/%m/%Y")
        hoje = datetime.today()

        if data_validada > hoje:
            raise ValueError

    except ValueError:
        print("A data informada nao e valida!")
        sys.exit(1)

def valida_atributo(nome_atributo, valor_atributo, max_len):

    validacao_generica(nome_atributo, valor_atributo, max_len)

    if "telefone" in nome_atributo.lower():
        valida_telefone(telefone=valor_atributo)

    elif "data" in nome_atributo.lower():
        valida_data(data=valor_atributo)

def obtem_e_valida_atributo(nome_atributo, max_len):
    atributo = input(f"{nome_atributo}: ")
    valida_atributo(nome_atributo=nome_atributo, valor_atributo=atributo, max_len=max_len)
    return atributo

def salva_contatos(agenda, nome_arquivo="agenda.txt"):
    with open(file=nome_arquivo, mode="w") as f_agenda:
        for dicionario_contato in agenda:
            linha = ""
            for valor in dicionario_contato.values():
                linha = linha + f"{valor},"
            linha = linha.rstrip(",")
            f_agenda.write(f"{linha}\n")

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
        novo_contato["nome_contato"] = obtem_e_valida_atributo(nome_atributo="Nome", max_len=10)
        novo_contato["sobrenome_contato"] = obtem_e_valida_atributo(nome_atributo="Sobrenome", max_len=10)
        novo_contato["data_nascimento"] = obtem_e_valida_atributo(nome_atributo="Data de Nascimento (dd/mm/aaaa)", max_len=10)
        novo_contato["telefone_contato"] = obtem_e_valida_atributo(nome_atributo="Numero do telefone", max_len=11)

        print("Dados do contato validados e serão salvos...")
        agenda.append(novo_contato)
        salva_contatos(agenda=agenda)

    elif operacao == "3":
        for contato in agenda:
            for chave, valor in contato.items():
                print(f"{chave.replace('contato', '').replace('_', ' ').title().strip()}: {valor}")
            print()