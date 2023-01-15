from utils import carrega_contatos
from utils import salva_contatos
from utils import exibe_agenda
from utils import pesquisa_contato
from utils import atualiza_ou_cria_contato
from constants import CONTATO

print("Bem-vindo ao seu app de Contatos.")

agenda = carrega_contatos()
operacao = ""
while operacao != "6":
    print()
    print("### MENU ###")
    print("Operações possíveis:")
    print("1 - Salvar")
    print("2 - Editar")
    print("3 - Listar")
    print("4 - Pesquisar")
    print("5 - Deletar")
    print("6 - Sair")
    operacao = input("Escolha uma operação acima pelo seu numero: ")

    if operacao == "1":
        print("A seguir, insira os dados do usuário que você deseja armazenar.")

        novo_contato = atualiza_ou_cria_contato(dicionario_contato={}, chaves=CONTATO.keys())

        print("Dados do contato validados e serão salvos...")
        agenda.append(novo_contato)
        salva_contatos(agenda=agenda)

    elif operacao == "2":
        agenda_filtrada = pesquisa_contato(agenda=agenda, inclui_ref=True)
        if agenda_filtrada:
            ref_contato = input("Informe a Referencia do contato a ser editado: ")
            contato_para_editar = agenda_filtrada[int(ref_contato)]

            lista_de_chaves = list(CONTATO.keys())

            for chave, valor in CONTATO.items():
                print(f"{lista_de_chaves.index(chave)} - {valor[0]}")

            index_chaves = input("Escolha os campos acima para editar pelos seus numeros, separados por virgula: ")
            index_chaves = index_chaves.split(",")

            chaves = []
            for index in index_chaves:
                chave = lista_de_chaves[int(index)]
                chaves.append(chave)

            # usando list comprehensions
            # chaves = [lista_de_chaves[int(index)] for index in index_chaves]

            atualiza_ou_cria_contato(dicionario_contato=contato_para_editar, chaves=chaves)
            salva_contatos(agenda=agenda)



    elif operacao == "3":
        exibe_agenda(agenda=agenda)

    elif operacao == "4":
        pesquisa_contato(agenda=agenda)

    elif operacao == "5":
        agenda_filtrada = pesquisa_contato(agenda=agenda, inclui_ref=True)
        if agenda_filtrada:
            ref_contato = input("Informe a Referencia do contato a ser deletado: ")
            contato_para_deletar = agenda_filtrada[int(ref_contato)]
            agenda.remove(contato_para_deletar)
            salva_contatos(agenda=agenda)
            print(f"O contato {contato_para_deletar} foi removido com sucesso")

