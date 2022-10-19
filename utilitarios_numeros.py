# FUNÇÕES ÚTEIS "BUILT-IN" PARA SE LIDAR COM NÚMEROS

# abs(): retorna o valor ABSOLUTO de um número. Aceita apenas um argumento, que pode ser inteiro ou ponto flutuante
print(abs(10))
print(abs(-10))
print(abs(-3.14))

# min(): retorna o menor valor entre os argumentos numericos passados para a funcao
menor_numero = min(1, 3, 6, 7, 23.4, 7, 8, 23, 3, 6, -1)
print(f"O menor numero informado é: {menor_numero}")

# # max(): retorna o maior entre os argumentos numericos passados para a funcao
maior_numero = max(1, 3, 6, 7, 23.4, 7, 8, 23, 3, 6, -1)
print(f"O maior numero informado é: {maior_numero}")

# # round(): Se receber apenas 1 argumento (numero), apenas arredonda este numero para o inteiro mais proximo.
# # caso receba 2 argumentos, arredonda o numero recebido no primeiro parametro para a quantidade de casas decimais do segundo.
print(round(10))
print(round(10.4))
print(round(10.5))
print(round(10.6))
print(round(10.356, 2))

pi = 3.141592
print(round(pi))
print(round(pi, 2))
print(round(pi, 3))
print(round(pi, 4))

# FUNÇÕES ÚTEIS PARA NÚMEROS DISPONÍVEIS ATRAVÉS DO MÓDULO 'math'
import math

# # Curiosidade:
# # O módulo math oferece o numero Pi com 15 casas decimais através de uma constante nomeada 'pi' (letas minúsculas mesmo)
pi = math.pi
print(f"O numero pi definido dentro do módulo math é: {pi}")


# # ceil(): arredonda para cima -> Retorna o proximo iteiro maior que ou igual ao argumento passado
print(math.ceil(1.001))
print(math.ceil(1.1))
print(math.ceil(1.2))
print(math.ceil(1.9))
print(math.ceil(1))

print(f"math.ceil(pi): {math.ceil(pi)}")
print(f"math.ceil(-pi): {math.ceil(-pi)}")


# # floor(): arredonda para baixo -> Retorna o proximo inteiro menor ou igual ao argumento passado
print(math.floor(1.001))
print(math.floor(1.1))
print(math.floor(1.2))
print(math.floor(1.9))
print(math.floor(1))

print(f"math.floor(pi): {math.floor(pi)}")
print(f"math.floor(-pi): {math.floor(-pi)}")


# # trunc(): remove a parte fracionada (casas decimais de um numero).
# # Na pratica, acaba se comportanto exatamente como floor() para numeros positivos, ou como ceil() para numeros negativos.
print(f"math.trunc(pi): {math.trunc(pi)}")
print(f"math.trunc(-pi): {math.trunc(-pi)}")


# FUNÇÕES ÚTEIS PARA NÚMEROS DISPONÍVEIS ATRAVÉS DO MÓDULO 'random'

import random

aleatorio_int = random.randint(1, 10)
print(aleatorio_int)

# lembre-se que voce pode passar resultados retornados por funcoes/metodos para outras funcoes/metodos.
# portando se voce quiser, pode usar a funçao round() (ou qualquer uma das outras funcoes que vimos aqui) para
# arredondar o numero Ponto Flutuante aleatorio retornado abaixo para algo mais adequado.
aleatorio_decim = random.uniform(1, 10)  # ex: round(random.uniform(1, 10), 3) -> retornaria um aleatorio com 3 casas decimais em vez de 15.
print(aleatorio_decim)
