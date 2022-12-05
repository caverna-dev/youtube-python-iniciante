###############
# DICTIONARY #
###############
# - Dicionarios sao uma estrutura de dados do tipo key-value pair (par 'chave-valor'). Isto é, dentro de um dicionário
#   existem índices que chamamos de 'chave', e cada chave está associada a um 'valor'.
# - Para obter um valor associado a uma chave, basta indexar o dicionário usando-a.
# - Chaves podem ser formadas a partir qualquer objeto HASABLE: string, integer, float, boolean e tuples contendo apenas objetos
#   imutáveis, sao alguns exemplos de objetos hashable;
# - Nao iremos nos aprofundar no conceito de hashable, mas pra facilitar: um objeto é 'hashable' se conseguimos executar
#   a função built-in hash(), passando o objeto como parametro, sem o Python lançar um erro. Exemplos derao dados nesta liçao.
# - Até a versao 3.7 do python, dicionários eram DESORDENADOS. A partir da versão 3.8, passaram a ser estruturas ORDENADAS,
#   isto é: o python garante que a ordem com que você cria novos pares chave-valor dentro do dicionário será preservada.
# - UMA DICA: pelo fato de dicionarios terem sempre sido estruturas desordenadas desde a primeira versao do python e apenas
#   recentemente isso ter mudado, recomendo que ainda por alguns anos, voce nao desenvolva com a premissa de que
#   dicionarios sao estruturas ordenadas. Isto vai evitar bugs no seu codigo com eventuais versoes mais antigas do python.
# - Mesmo tendo se tornado uma estrutura ordenada, dicionários nao sao SEQUENCES, uma vez que nao é possivel indexar
#   elementos dentro de um dicionário através de um index numérico, mas apenas através de suas CHAVES.
# - Se nao é sequence, nao dá pra fazer 'slicing'.
# - Reforçando: dicionários nao sao SEQUENCES, mas são ITERABLES.

# Verificando se um objeto é hashable:
hash("caverna_dev")
hash(1)
hash(-100.1)
hash(False)
hash(("string", "outra string"))

# descomente as proximas duas linhas para ver o erro
# tupla_com_lista = ("listas sao mutaveis", [1, 2, 3])  # nao é hashable, pq 1 ou mais objetos dentro da tupla é mutável
# hash(tupla_com_lista)

# # criando um dicionário em python
meu_dicionario = {
    "chave_1": "1",
    "chave_2": 2,
    3: True,
    4.1: -173.6,
    (1, 2): "tuplas podem ser chaves",
    "list": [0, 1, 2],
    "dict": {
        "a": 1,
        "b": 2
    }
}
print(meu_dicionario)
print(type(meu_dicionario))

# # criando um dicionario vazio - ambas formas abaixo produzem o mesmo resultado
dict_vazio_1 = {}
dict_vazio_2 = dict()

# # Truth test com bool()
print(bool(meu_dicionario))
print(bool(dict_vazio_2))

# indexando em dicionarios
valor_1 = meu_dicionario['chave_1']
print(f"o valor armazenado pela chave 'chave_1' é: {valor_1}")
print(f"o valor armazenado pela chave '(1, 2)' é: {meu_dicionario[(1, 2)]}")
print(f"o tipo do dado armazenado pela chave 'dict' é: {type(meu_dicionario['dict'])}")

# o que acontece quando voce tentar acessar uma chave que nao existe?
# meu_dicionario["chave_3"]  # 'chave_3' nao é uma chave em meu_dicionario -> KeyError

# adicionando novos elementos a um dicionario
novo_dict = {}
# print(novo_dict)
novo_dict["nome"] = "Clark"
novo_dict["sobrenome"] = "Kent"
novo_dict["profissao"] = "Jornalista"
novo_dict["identidade_secreta"] = "Superman"
print(novo_dict)

# Alterando valores armazenados por uma chave
novo_dict["nome"] = "Kal"
novo_dict["sobrenome"] = "El"
print(novo_dict)


# Metodos utilitarios para dicionarios
# dict.get(): Retorna o valor associado a uma chave, ou um valor padrão caso a chave informada nao exista. Por default,
# esse valor padrao é o 'None'
nome = novo_dict.get("nome")
print(f"Nome: {nome}")


idade = novo_dict.get("idade")
print(f"A idade de {nome} é: {idade}")

status_civil = novo_dict.get("status_civil", "NAO INFORMADO")
print(f"O status civil de {nome} é: {status_civil}")


# dict.keys(): Retorna um objeto iterable de um tipo especial chamado 'dict_keys', que contem todas as chaves do dicionario.
keys = novo_dict.keys()
print(type(keys))
print(keys)


# dict.values(): Retorna um objeto iterable de um tipo especial chamado 'dict_values', que contem todos os valores do dicionario.
values = novo_dict.values()
print(type(values))
print(values)


# dict.items(): Retorna um objeto iterable de um tipo especial chamado 'dict_items', que contem todos os pares (chave, valor) do dicionario.
items = novo_dict.items()
print(type(items))
print(items)

# dict.pop(): Remove uma chave de dentro de um dicionario, caso estivesse presente, retornando o valor associado a ela.
# Caso a chave nao exista, o python lança um KeyError
profissao_removida = novo_dict.pop("profissao")
print(profissao_removida)
print(novo_dict)

# a linha abaixo causa um erro
# idade_removida = novo_dict.pop("idade")


# dict.popitem(): Remove o ultimo elemento chave-valor e o retorna como uma tupla
elemento_removido = novo_dict.popitem()
print(elemento_removido)
print(novo_dict)


# dict.clear(): Limpa um dicionario, deletando todos os elementos.
print(novo_dict)
novo_dict.clear()
print(novo_dict)


# dict.update(): Atualiza/Funde um dicionário com outro
dict_1 = {1: "um", 2: "dois"}
print(dict_1)

dict_2 = {3: "tres", 4: "quatro"}
print(dict_2)

dict_1.update(dict_2)
print(dict_1)








########
# SETS #
########
# - Sao uma representaçao em python de CONJUNTOS (mesmo fundamento matemático de teoria dos conjuntos).
#   -> Em matemática, um conjunto é uma coleção de elementos DISTINTOS.
# - Podem armazenar APENAS objetos (elementos) 'hashable'. Conceito já visto acima em dictionaries.
# - sets sao estruturas de dados NAO SEQUENCIAIS (desordenadas), e MUTÁVEIS. Como consequência direta disto, temos que:
#   -> Nao existe o conceito de "index" em sets, nao sendo possível acessar um elemento especificamente por uma 'posição'.
#   -> Elementos (objetos) podem ser deletados ou adicionados a um set
# - ATENÇÃO: os elementos em si nao podem ser alterados, visto que sao IMMUTABLE
# - sets nao permitem duplicação de elementos dentro de si.
# - sets são, ITERABLES, mas não são SEQUENCES.


# Criando um set em python
meu_set = {"caverna_dev", 1, -100.1, True, False, ("string", "outra string")}
print(meu_set)
print(type(meu_set))
print(bool(meu_set))

set_vazio = set()
print(set_vazio)
print(bool(set_vazio))


# # criando sets a partir de uma lista - Note que os elementos no set nao se repetem
lista_nome_canal = list("caverna_dev")
print(f"lista_nome_canal é {lista_nome_canal} e tem tamanho {len(lista_nome_canal)}")

set_nome_canal = set(lista_nome_canal)
print(f"set_nome_canal é: {set_nome_canal} e tem tamanho {len(set_nome_canal)}")

# criando sets a partir de um dicionário
print(set({"chave_1": 1, "chave_2": 2, "chave_3": 3}))


# tentando usar um objeto mutável dentro de um set:
# set_que_vai_dar_ruim = {"uma string", 3.14, [True, False]}

# tentando usar um objeto imutável, porém NON-HASHABLE dentro de um set:
# outro_set_que_vai_dar_ruim = {"uma string", 3.14, ({1, 2, 3}, 1)}

# sets sao DESORDENADOS: indexing e slicing nao funcionam com sets
# tentando_retornar_um_objeto_especifico = meu_set[3]







# MÉTODOS UTILITARIOS PARA SETS

# set.add(): adiciona um elemento ao set. 'Similar' ao list.append()
meu_set.add("elemento adicional")
print(meu_set)

# # set.remove(): remove um elemento do set. O elemento PRECISA existir, ou o python lanca um erro.
meu_set.remove("elemento adicional")
print(meu_set)

# a linha abaixo causa um erro
# meu_set.remove(999)

# # set.discard(): funciona exatamente como o metodo remove(). Porém, caso o elemento passado como parametro nao exista,
# # o python nao lança um erro e continua a execução do programa normalmente.
meu_set.discard(999)
print(f"Nenhum erro aconteceu e 'meu_set' é: {meu_set}")

# set.pop(): Remove um elemento arbitrariamente do set e retorna esse elemento. Diferentemente dos metodos vistos acima,
# o set.pop() nao recebe nenhum paramentro. Caso o set esteja vazio, o python lança um erro:
elemento_removido = meu_set.pop()
print(f"O elemento removido foi '{elemento_removido}'. Agora meu_set é: {meu_set}")

# set.clear(): Limpa o set, isto é: remove todos os elementos armazenados pelo set, deixando-o vazio.
meu_set.clear()
print(f"o tamanho de 'meu_set' é: {len(meu_set)} -> {meu_set}")


# Um dos macetes mais uteis com sets: reduzir uma lista apenas para o seu numero de elementos unicos
lista_com_elementos_repetidos = [1, 1, 1, 2, 2, 2, 3, 3, 3, 100, 100, 100]
lista_com_elementos_unicos = list(set(lista_com_elementos_repetidos))
print(lista_com_elementos_unicos)













# Os métodos que veremos abaixo possuem também um operador especificado entre parenteses.
# Você pode alcançar o mesmo resultado usando tanto o método, como o operador. Contudo, há uma diferença importante:
# - usando o método, o(s) parâmetro(s) passado(s) pode(m) ser qualquer(quaisquer) ITERABLE(s). Ex: string, list, tuple, sets...
# - usando o operador (que você vê entre parênteses), TODOS operandos devem ser sets.

# Para os exemplos a seguir, usaremos os seguintes sets:
# a = {1, 2, 3, 10}
# b = {3, 4, 5, 10}
# c = {5, 6, 7, 10}
# d = {7, 8, 9, 10}


# set.union() (|): Recebe uma quantidade indeterminada de iterables como parametros e retorna um objeto set com todos os elementos
# que existem em todos os iterables (incluindo o set que chama o metodo), sem repetir elementos.
# novo_set = a.union(b, c, d)
# # novo_set = a | b | c | d
# print(novo_set)


# set.intersection (&): Recebe uma quantidade indeterminada de iterables como parametros e retorna um objeto set APENAS os elementos
# que se repetem em todos os iterables (incluindo o set que chama o metodo)
# novo_set = a.intersection(b, c, d)
# # novo_set = a & b & c & d
# print(novo_set)


# set.difference (-): Recebe uma quantidade indeterminada de iterables como parametros e retorna um objeto set APENAS com os elementos
# que existem no set que chamou o metodo (ou no set mais a esquerda se estiver usando o operador '-')
# novo_set = a.difference(b, c, d)
## novo_set = a - b - c - d
# print(novo_set)



# set.symmetric_difference (^): Recebe APENAS um iterable como parametros e retorna um objeto set APENAS com os elementos
# que existem em um set, mas nao em multiplos. Se utilizando o operador '^', a operacao pode acontecer com um numero indeterminado de sets.
# novo_set = a.symmetric_difference(b)
# novo_set = a ^ b ^ c ^ d
# print(novo_set)