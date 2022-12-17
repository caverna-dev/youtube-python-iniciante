# - Estruturas de Repetição, ou Loops, são mecanismos oferecidos por uma linguagem de programação para executar um
#   mesmo conjunto de instruções varias vezes - potencialmente com valores (parametros) diferentes a cada vez.
# - A cada repetição, damos o nome de iteração (daí quem vem o nome ITERABLE 👍🏻).
# - Uma "condição de parada" precisa existir, caso contrário o loop repete-se indefinidamente (loop infinito)
# - O python oferece dois mecanismos de Loops: FOR e WHILE



#############
# Loops FOR #
#############
# - Em python, sempre percorrem (iteram sobre) objetos ITERABLES: strings, lists, tuples, dictionaries, sets, sao os
#   exemplos de iterables que já vimos por aqui.
# - Também é comum usar ranges, outro tipo de Iterable que nao vimos ainda, mas veremos nessa aula.
# - Por isso, FOR loops implementam um número de repetições pré-definidas, que no python será o tamanho do iterable.
# - Pelo numero de repetições ser já conhecido na própria declaração do loop (o tamanho do iterable), nao existe risco
#   de um loop FOR ser infinito.


# Declarando alguns iterables:
my_str = "strings sao ITERABLES"
my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
my_tuple = ("a", "b", "c", 1, 2, 3)
my_set = set(my_list)
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
my_range = range(1, 15)

# exemplo 1
soma_nums = 0
str_concat = ""
for item in range(3, 6):
    print(my_list.index(item))
    # if type(elemento) == int:
    #     soma_nums += elemento
    #     print(soma_nums)
    # elif isinstance(elemento, str):
    #     str_concat += elemento
    #     print(str_concat)




# clausula 'break': força o python a SAIR do loop imediatamente, sem sequer executar a próxima iteração
for elemento in my_range:
    if elemento == 5:
        break
    print(elemento)


# # clausula 'continue': força o python pular da iteração atual direto para próxima
for elemento in my_range:
    if elemento % 2 == 0:
        continue
    print(elemento)


# clausula 'else': Executa APENAS se o loop FOR executou todas as suas iterações e chegou ao final sem se deparar com
# uma clausula 'break'
import math
for inteiro in range(6):
    raiz_q = math.sqrt(inteiro)
    print(f"raiz quadrada de {inteiro} é: {raiz_q}")
    if raiz_q > 2:
        break
else:
    print("Todas as iterações executaram")




###############
# Loops WHILE #
###############
# - Diferentemente dos loops FOR, nao possuem um fim determinado por um Iterable, mas sim por uma condicional (boolean).
# - Enquanto a condição na declaração do loop while resolver para 'True', o python executa as instruções definidas dentro
#   do loop. O python para apenas quando a condição resolver para 'False'.
# - Pelo numero de repetições ser entaão atrelado a uma condição, existe risco de um loop WHILE ser infinito.
# - as cláusulas 'break', 'continue' e 'else' funcionam para o WHILE exatamente da mesma maneira que nos loops FOR



# Exemplo 1
i = 1
while i < 10:
    print(i)
    i += 1


# Exemplo 2
operacao = ""
while operacao != "3":
    print("1 - Saudaçao")
    print("2 - Frase Inspiradora")
    print("3 - Sair do programa")

    operacao = input("Escolha uma operação: ")
    if operacao == "1":
        print("Bom dia, mundo!")

    elif operacao == "2":
        print("Se ontem foi ruim, hoje vai ser pior!")

    print("\n\n")


# Exemplo 3: Condicao que nunca é satisfeita leva a um "loop infinito"
i = 0
while i != -1:
    print(i)





# Exemplo 4: Abaixo, tente entender porque mesmo o  WHILE sendo declarado com "True"
# ainda assim, o programa nao entrará num loop infinito.

import random
while True:
    aleatorio = random.randint(1, 100)
    print(f"numero gerado: {aleatorio}")
    for numero in range(2, aleatorio):
        if aleatorio % numero == 0:
            print(f"{aleatorio} dividio por {numero} = {aleatorio/numero}")
            print("\n")
            break
    else:
        # se essa clausula executar, significa que o
        # loop FOR acima nunca executou o 'break'. Portanto
        # 'aleatorio' é primo
        print(f"{aleatorio} é um numero primo")
        break
