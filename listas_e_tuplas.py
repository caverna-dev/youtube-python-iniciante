##########
# LISTAS #
##########


# Listas são uma das muitas formas que o Python oferece ao programador para Estruturar Dados.
# Como já mencionado anteriormente, elas caem dentro da categoria de objetos iterables que também são SEQUENCES.
# Pelo fato de serem SEQUENCES, listas tem o conceito de ordem: os elementos armazenados dentro de uma lista existem em
# posições específicas e podem ser acessados através de seus índices (lembre-se que índices começam sempre do 0).
# Em breve, veremos outra estrutura de dados sequencial em python chamada de tuplas (tuple).
# Listas e Tuplas tem muito em comum, sendo a principal diferença o fato de que listas saão consideradas objetos MUTÁVEIS
# enquanto Tuplas são objetos IMUTÁVEIS.


# Como definir listas:
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)
print(f"O tipo do dado da variável minha_lista é: {type(minha_lista)}")

print(bool(minha_lista))
print(bool([]))


# Como listas sao SEQUENCES, os conceitos ja apresentados nos videos sobre manipulação de strings continuam sendo
# válidos aqui
primeiro_item_da_lista = minha_lista[0]
print(f"O primeiro item da lista é: {primeiro_item_da_lista}")

ultimo_item_da_lista = minha_lista[-1]
print(f"O ultimo item da lista é: {ultimo_item_da_lista}")

itens_fatiados = minha_lista[2:4]
print(f"Os elementos nas posicoes 2 e 3 sao: {itens_fatiados}")
print(f"O tipo de dado resultante do slicing de uma lista é: {type(itens_fatiados)}")






# Listas podem armazenar objetos de QUAISQUER tipos.
lista_mista = [1, "abc", 3.1416, True, False, ["outra lista", 100], minha_lista]
print(lista_mista)











# Os elementos de uma lista podem ser alterados livremente.
lista_mista[1] = "def"
print(lista_mista)

lista_mista[6][1] = 99
print(lista_mista)
print(minha_lista)










# UTILITARIOS PARA LISTAS

# len(): Esta função, que vale para qualquer iterable, também funciona com lists
print(f"lista_mista contém {len(lista_mista)} elementos.")

# # count(): aceita um parametro e retorna a quantidade de vezes que o parametro passado ocorre na lista
contagem_de_1 = lista_mista.count(1)
print(f"O elemento 1 se repete em lista_mista {contagem_de_1} vezes")

#index(): aceita um parametro e retorna o indice (posicao) da primeira vez que esse parametro ocorre na lista - se ele existir.
print(lista_mista.index([1, 99, 3, 4, 5]))

# append(): aceita um parametro e adiciona
lista_mista.append(1)
print(lista_mista)
print(f"lista_mista agora contém {len(lista_mista)} elementos.")

#insert(): aceita 2 parametros:
# - o primeiro deve ser um inteiro indicando o indice que o novo elemento deve ocupar;
# - o segundo é um objeto (de qualquer tipo) a ser inserido na lista;
print(minha_lista)
minha_lista.insert(4, "novo elemento")
print(minha_lista)


# extend(): recebe um parametro que também deve ser uma lista e adiciona cada elemento dessa lista a lista que chama o metodo
lista_1 = ["caverna_dev", "python", 3.14]
lista_2 = ["iniciante", "pythonico"]
lista_1.extend(lista_2)
print(lista_1)


# pop(): aceita um inteiro como parametro e remove da lista o elemento na posicao indicada pelo parametro passado.
# Alem disto, este método também retorna o elemento removido.
elemento_removido = lista_1.pop(1)
print(lista_1)
print(elemento_removido)


# remove(): aceita um parametro. Se o parametro passado existir na lista, ele será removido
lista_1.remove(3.14)
print(lista_1)


# reverse(): inverte a orde dos elementos na list
lista_1.reverse()
print(lista_1)


# sort(): ordena os elementos de uma lista (faz uso de comparadores logicos, portando os elementos precisam ser comparaveis)
# o método sort() aceita alguns outros argumentos, mas no momento nao veremos como usá-los
lista_desordenada = [18, 2, 4, 9, 3.1416]
lista_desordenada.sort()
print(lista_desordenada)


# unpacking: é possivel fazer o unpacking de valores armazenados em listas para variaveis
var_a, var_b, var_c = [1, 2, 3]
print(var_a, var_b, var_c)



# operador in:
contem_python = 3.14 in lista_1
print(contem_python)










##########
# TUPLAS #
##########

# # Toda a teoria que vimos para lists, vale para tuples.
# # Tuples também são Sequences (indexáveis e ordenadas)
# # Tuples podem armazenar objetos de quaisquer tipos (inclusive outras tuples e listas...)
# # Tuples também permitem o uso de slicing e unpacking
#
minha_tupla = (1, 2, 3, 4, 5, ["a", "b", "c"], (True, False))
# print(f"O tipo do dado da variável minha_tupla é: {type(minha_tupla)}")


# print(bool(minha_tupla))
# print(bool(tuple()))


print(minha_tupla)
# print(minha_tupla[0])
# print(minha_tupla[-1])
# print(minha_tupla[1:4])
# a, b, c = minha_tupla[4:]
# print(a, b, c)





# A grande diferença entre tuplas e listas é que tuplas são IMUTÁVEIS:
# minha_tupla[0] = 100
# Outros tipos de dados que também são "imutáveis": strings, integers, floats, boolean.


# Leituras recomendadas sobre Mutabilidade x Imutabilidade em Python (em Inglês):
# -> https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/#:~:text=Immutable%20is%20the%20when%20no,of%20these%20objects%20is%20permanent.
# -> https://stackoverflow.com/a/37536770









### UTILITÁRIOS PARA TUPLAS
# por serem 'immutable', tuplas praticamente nao oferecem nenhum utilitario.
# os unicos disponiveis sao o count() e o index(), que funcionam exatamente como já vimos em listas
# além destes 2 específicos para tuples(), também existem a função len() - que funciona para qualquer Iterable.



# # len():
# print(len(minha_tupla))
#
# # count():
# print(minha_tupla.count(3))
#
# # index():
# print(minha_tupla.index(3))

# print("Hello, World!)