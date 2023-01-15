from datetime import datetime
from pathlib import Path
from exceptions import ValidationException
from constants import CONTATO

def validacao_generica(nome_atributo, valor_atributo, max_len):
    if not valor_atributo:
        raise ValidationException(f"Nao é possível continuar sem um '{nome_atributo}'.")
    elif len(valor_atributo) > max_len:
        raise ValidationException(f"O campo '{nome_atributo}' nao pode ter mais que {max_len} chars")

def valida_telefone(telefone):
    if not telefone.isnumeric():
        raise ValidationException("Um numero de telefone precisa ser composto apenas por caracteres numericos")

def valida_data(data):
    try:
        data_validada = datetime.strptime(data, "%d/%m/%Y")
        hoje = datetime.today()

        if data_validada > hoje:
            raise ValueError

    except ValueError:
        raise ValidationException("A data informada nao e valida!")

def valida_atributo(nome_atributo, valor_atributo, max_len):
    try:
        validacao_generica(nome_atributo, valor_atributo, max_len)

        if "telefone" in nome_atributo.lower():
            valida_telefone(telefone=valor_atributo)

        elif "data" in nome_atributo.lower():
            valida_data(data=valor_atributo)

        return True

    except ValidationException as err:
        print(err)
        return False

def obtem_e_valida_atributo(nome_atributo, max_len):
    atributo_valido = False

    while not atributo_valido:
        atributo = input(f"{nome_atributo}: ")
        atributo_valido = valida_atributo(nome_atributo=nome_atributo, valor_atributo=atributo, max_len=max_len)
        if not atributo_valido:
            print(f"Informe {nome_atributo} mais uma vez...")

    return atributo

def salva_contatos(agenda, nome_arquivo="agenda.txt"):
    with open(file=nome_arquivo, mode="w") as f_agenda:
        for dicionario_contato in agenda:
            linha = ",".join(dicionario_contato.values())
            f_agenda.write(f"{linha}\n")

def carrega_contatos(nome_arquivo="agenda.txt"):
    if arquivo_existe(nome_arquivo):
        with open(file=nome_arquivo, mode="r") as f_agenda:
            linhas = f_agenda.readlines()
            agenda = []
            for linha in linhas:
                nome, sobrenome, data_nascimento, telefone = linha.split(",")

                contato = {
                    "nome_contato": nome,
                    "sobrenome_contato": sobrenome,
                    "data_nascimento": data_nascimento,
                    "telefone_contato": telefone.strip()
                }

                agenda.append(contato)

        return agenda

    return []

def arquivo_existe(nome_arquivo):
    arquivos = []

    for item in Path().iterdir():
        if item.is_file():
            arquivos.append(item.name)

    return nome_arquivo in arquivos

def exibe_agenda(agenda, inclui_ref=False):
    for contato in agenda:
        if inclui_ref:
            print(f"Ref.: {agenda.index(contato)}")

        for chave, valor in contato.items():
            print(f"{chave.replace('contato', '').replace('_', ' ').title().strip()}: {valor}")
        print()

def pesquisa_contato(agenda, inclui_ref=False):
    nome_pesquisa = input("Informe o NOME do contato: ")

    agenda_filtrada = []
    for contato in agenda:
        if contato["nome_contato"].lower() == nome_pesquisa.lower():
            agenda_filtrada.append(contato)

    # usando list comprehensions:
    # agenda_filtrada = [contato for contato in agenda if contato["nome_contato"] == nome_pesquisa

    if agenda_filtrada:
        exibe_agenda(agenda=agenda_filtrada, inclui_ref=inclui_ref)
    else:
        print(f"Nenhum contato com o nome {nome_pesquisa} foi encontrado.")

    return agenda_filtrada

def atualiza_ou_cria_contato(dicionario_contato, chaves):
    for chave in chaves:
        dicionario_contato[chave] = obtem_e_valida_atributo(*CONTATO[chave])

    return dicionario_contato