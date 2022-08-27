nome_usuario = 'Fulano de Tal'  # str - texto
idade_usuario = 28              # int - numero inteiro
peso_usuario = 70.0             # float - numero decimal
altura_usuario = 1.69           # float - numero decimal
# maior_de_idade = True           # bool - valor lógico

####################################################################
# Operadores Matemáticos: Produzem como resultado um tipo numerico #
####################################################################

# OBS: A forma pythonica de representar uma 'constante' é com uma variável
# com letras maiúsculas apenas, como abaixo.
# DECADA = 10  # CONSTANTE quer armazena o valor de anos em 1 década
#
# # 300 linhas de codigo depois
# DECADA = 3
#
# # Operação de soma:
# print("A idade do usuário daqui a 10 anos será:")
# idade_em_10_anos = idade_usuario + DECADA
# print(idade_em_10_anos)
#
# # Operação de divisão:
# print("A idade do usuário em número de décadas é de:")
# idade_em_decadas = idade_usuario / DECADA
# print(idade_em_decadas)
#
# # Operação de subtração:
# print("Para atingir um peso de 65kg, o usuário necessita emagrecer: ")
# diff_peso = peso_usuario - 65
# print(diff_peso)
#
# # Operação de multiplicação:
# print("O peso do usuário em gramas é:")
# peso_em_gr = peso_usuario * 1000
# print(peso_em_gr)







##############################
# Mais operacoes matematicas #
##############################
# int_a = 10
# print("O valor de int_a:", int_a)
# int_b = 3
# print("O valor de int_b:", int_b)

# Módulo: resto da divisão
# mod_a_b = 10 % 3
# print("O resto da divisado de int_a por int_b é:", mod_a_b)

# Potenciação: um numero elevado a outro
# pot_a_b = 10 ** 3
# print("int_a elevado a potencia de int_b é:", pot_a_b)
#
# # Raiz Quadrada
# import math
# raiz_int_a = math.sqrt(int_a)
# print("A raiz quadrada de int_a é:", raiz_int_a)
#
# imc_usuario = peso_usuario/(altura_usuario ** 2)
# print("O IMC do usuário é:", imc_usuario)















################################################################
# Comparadores Lógicos: Produzem como resultado um tipo 'bool' #
################################################################
# print("O usuario é maior de idade?", maior_de_idade)

# MAIORIDADE = 18
#
# maior_de_idade = idade_usuario > MAIORIDADE
# print("O usuario é maior de idade?", maior_de_idade)
#
# Operacoes de MAIOR e MENOR
# # definição arbitrária e fictícia: Se maior ou igual a 1.70m é considerado 'alto'. Caso contrário, é considerado 'baixo'
# print("O usuário é alto?", altura_usuario >= 1.70)
# print("O usuário é baixo?", altura_usuario < 1.70)
#
# # Operacao de IGUALDADE

# print("O nome do usuário é Ciclano de Tal:", nome_usuario == 'Ciclano de Tal')
# print('O nome do usuário é Fulano de Tal:', nome_usuario == "Fulano de Tal")

# Operacao de DESIGUALDADE
# print("A idade do usuário é diferende de 20 anos?", idade_usuario != 28.0)

# print(28 == "28")
# print(1.1 >= 1.111111)
print("a" < "a")











# ##############################################################
# # Operadores Lógicos: Produzem como resultado um tipo 'bool' #
# ##############################################################
# t = True
# f = False
#
#
# # Operação 'and' - E lógico
# # valor_logico_a and valor_lógico_b
# # - 'True': somente se valor_logico_a e valor_logico_b forem 'True'
# # - 'False': para qualquer outra combinacao de valores.
# print("True AND True:", t and t)
# print("True AND False:", t and f)
# print("False AND True:", f and t)
# print("False AND False:", f and f)
#
#
# # Operação 'or' - OU lógico
# # valor_logico_a or valor_lógico_b
# # - 'True': se pelo menos 1 dos valores lógicos forem True
# # - 'False': apenas se ambos os valores lógicos forem False
# print("True OR True:", t or t)
# print("True OR False:", t or f)
# print("False OR True:", f or t)
# print("False OR False:", f or f)
#
#
# # Operacao NOT - NEGACAO/INVERSÃO lógica
# # not valor_logico_a
# # - 'True': se valor_logico_a for 'False'
# # - 'False': se valor_logico_a for 'True'
# print("NOT True:", not t)
# print("NOT False:", not f)
#
#
# # Operacao NAND - Negação do AND
# nand_t_t = not (t and t)
# print("NOT (True AND True):", nand_t_t)
#
# nand_t_f = not (t and f)
# print("NOT (True AND False):", nand_t_f)
#
# nand_f_t = not (f and t)
# print("NOT (False AND True):", nand_f_t)
#
# nand_f_and_f = not(f and f)
# print("False AND False:", nand_f_and_f)









