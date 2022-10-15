#### DEFINICOES INCOMPLETAS QUE SERAO MELHOR EXPLICADAS FUTURAMENTE ####
# Tanto funções quanto métodos podem ser entendidos como "nomes" que encapsulam uma lógica que pode ser reusada.
# Isto quer dizer que quando uma função/método é invocada, algum tipo de processamento acontecerá.
# Tanto funções quanto métodos podem ou não receber parâmetros (passados entre parênteses e separados por vírgulas).

# A principal diferença entre funçaão e método é:

# - MÉTODOS: sao dependentes de um objeto. Portanto só podem ser chamados a partir de um 'objeto'.
#   Exemplos:
#       - meu_objeto.faz_alguma_coisa()
#       - outo_objeto.faz_outra_coisa(parametro1, parametro2, ...)

# - FUNÇÕES: sao independentes de objetos e podem ser invocadas de forma avulsa.
#   Exemplos:
#       - realiza_processamento()
#       - realiza_outro_processamento(parametro1, parametro2, ...)




##### FUNÇOES E MÉTODOS UTEIS PARA PROCESSAMENTO DE STRINGS #####
first_name = "bruce"
last_name = "wayne"
full_name = f"{first_name} {last_name}"

print(f"Nome: {first_name}")
print(f"Sobrenome: {last_name}")
print(f"Nome Completo: {full_name}")


# Funcao len(): retorna o tamanho de um iterable
# Lembre-se: strings são Sequences (e portanto tbm saão Iterables)
print(len(full_name))




# Método str.capitalize(): retorna uma CÓPIA da string com a primeira letra maiuscula
print(full_name.capitalize())
print(f"O objeto string em si nao é alterado pelo método capitalize(): {full_name}")

print("1 abc".capitalize())



# Método str.title(): retorna uma CÓPIA da string com todas as primeiras letras maiusculas
print(full_name.title())

print("1 abc 2cde |yz # wy".title())




# Método str.upper(): retorna uma CÓPIA da string com todas as letras maiúsculas
print(full_name.upper())
print("caverna Dev".upper())



# Método str.lower(): retorna uma CÓPIA da string com todas as letras minúsculas
str_maiuscula = "CAVERNA DEV"
print(str_maiuscula.lower())



# Método str.replace(): retorna uma CÓPIA da string com todas as ocorrencias de uma sbstring substituidas por outra string
print(full_name.replace("wayne", "dickinson"))

numer_subs = 3 # objeto do tipo int
print("abc def abc ghi abcjkl mnoabcpqr".replace("abc", "www", numer_subs))



# Métodos de stripping:
# lstrip(): retorna uma CÓPIA da string com espaços em brancos iniciais (a esquerda) removidos.
# rstrip(): retorna uma CÓPIA da string com espaços em brancos finais (a direita) removidos.
# strip(): retorna uma CÓPIA da string com espaços em brancos iniciais e finais removidos.

# Os 3 métodos acima aceitam um parametro opcional do tipo string, que se informado, será a substring removida
# em vez de 'espaços em branco'

nome_canal = " Canal caverna_dev    "
print(nome_canal.lstrip())
print(nome_canal.rstrip())
print(nome_canal.strip())
print(nome_canal.lstrip(" Canal "))


# Praticando:
# 1 - usando a str armazenada em 'channel_name' acima, obtenha uma string que contenha APENAS o nome do
# canal ('caverna_dev'), sem nenhum espaço em branco inicial, ou final.

# Abaixo, uma soluçao possível (tente outras possibilidades você mesmo):
apenas_nome_canal = nome_canal.strip().lstrip(" Canal ")  # imprima 'apenas_nome_canal' usando a função print() para ver o resultado
print(apenas_nome_canal)

# 2 - Novamente, processe o valor armazenado em 'channel_name' para obter como resultado final a string "Caverna Dev".
# Tente usar uma abordagem distinta da que usou no exercicio anterior.
# Abaixo, uma soluçao possível (tente outras possibilidades você mesmo):
apenas_nome_canal = nome_canal[7:18].replace("_", " ").title() # imprima 'apenas_nome_canal' usando a função print() para ver o resultado
print(apenas_nome_canal)

# OBS: Note que para as duas soluções acima, eu concatenei multiplas operações: 2xmétodos na primeira &
# slicing seguido de 2xmétodos na segunda. O python permite isto. Nao é necessário armazenar o resultado (objeto)
# retornado por uma função ou método em uma variável, para só então invocar outra função ou método.
# Você pode fazer tudo em uma única linha, se necessário. Mas lembre-se: preocupe-se com a legibilidade!



# Método str.startswith(): retorna True se a str começa com o parametro informado; False caso contrário.
"bruce wayne"
print(full_name.startswith("bruce"))
print(full_name.startswith("wayne"))



# Método str.endswith(): retorna True se a str termina com o parametro informado; False caso contrário.
"bruce wayne"
print(full_name.endswith("wayne"))
print(full_name.endswith("bruce"))



# Operador lógico 'in': retorna True se o primeiro operando (lado esquerdo) for um subconjunto do segundo (lado direito)
result = "bruce" in full_name
print(result)
print("-" in "caverna_dev")




# # BONUS:
# # Nao vimos este durante o video porque o que o método split() retorna é uma LISTA! E nós ainda nao falamos de listas.
# # Vou deixar aqui comentado para referencia, porque o split() é muito importante e amplamente usado,
# # mas só falarei dele no video de Listas.
#
# # Método str.split(sep): retorna uma lista em que cada elemento é um subconjunto do objeto string usado,
# # tendo sido separado nos pontos em que o argument 'sep' ocorre.
#
# nome_canal = "caverna_dev"
# palavras_nome_canal = nome_canal.split("_")  # aqui, o agumento 'sep' é o '_'
# print(type(palavras_nome_canal))  # usando a funçaão type(), veja que 'palavras_nome_canal' nao armazena um objeto 'str', mas sim 'list'.
# print(palavras_nome_canal)
#
# # lists também são Sequences, o que significa que também são Iterables.
# # Portanto podemos usar a função len() nelas:
# print(len(palavras_nome_canal))
#
# # Por serem Sequences, podemos acessar os elementos de uma 'list' através de indexes:
# print(f"A primeira palavra no nome do canal é: {palavras_nome_canal[0]}")
# print(f"A segunda palavra no nome do canal é: {palavras_nome_canal[1]}")
