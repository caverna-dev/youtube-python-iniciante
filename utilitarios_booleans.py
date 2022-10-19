# bool(): Na verdade, na verdade, esta não é exatamente uma "função". Mas para efeitos práticos, você pode entender como tal por enquanto.
# Ao passar um argumento nao booleano para bool() (por exemplo um numero, ou uma string, ou alguma outra coisa), o python
# vai tentar o seu melhor "traduzir" o argumento passado para True ou False, e isso é MUITO BOM! Acredite.

# Exemplos:
# Sequences (como strings, tuples, lists - ainda vamos ver o que sao essas 'coisas') vazias, são 'traduzidas' para False
string_vazia = ""
print(f"uma string vazia é avaliada como: {bool(string_vazia)}")

string_com_algo = "."
print(f"uma string nao vazia é avaliada como: {bool(string_com_algo)}")


# numeros
um = 1
print(bool(um))

dois = 2
print(bool(dois))

zero = 0
print(bool(zero))

pi = -3.14
print(bool(pi))





# Na verdade, por trás dos panos, booleans sao tipos numericos! Acredita???
# Mais especificamente, o python internamente representa True como 1 e False como 0
# Por isso, o único numero que convertido para booleano retorna False é o Zero (0).
# No entanto, qualquer numero diferente de zero (seja positivo, negativo, inteiro ou decimal) quando convertido para
# bool retorna True, como vimos acima.

# Isso significa que: internamente booleans sao essencialmente os números 1 (True) ou 0 (False). Portanto,
# voce pode realizar operacoes matemáticas com booleans:

bool_t = bool(-2)
bool_f = bool(0)

soma_t_t = bool_t + bool_t
print(f"Resultado numerico de True + True: {soma_t_t}")
soma_t_f = bool_t + bool_f
print(f"Resultado numerico de True + False: {soma_t_f}")

subtracao_t_t = bool_t - bool_t
print(f"Resultado numerico de True - True: {subtracao_t_t}")
subtracao_t_f = bool_t - bool_f
print(f"Resultado numerico de True - False: {subtracao_t_f}")

# tente outras operacoes (divisao, multiplicacao, e etc...) voce mesmo.


# Detectando quantos valores são True ou False dentro de um conjunto de valores booleans:
a = False
b = False
c = False
d = False
e = True

numero_de_inputs_true = a + b + c + d + e
print(f"A quantidade de inputs True foi: {numero_de_inputs_true}")
print(f"A quantidade de inputs False foi: {5 - numero_de_inputs_true}")


# all(): Retorna True se todos os argumentos sao True; Retorna False caso contraário.
# IMPORTANTE: all() aceita apenas UM argumento: um iterable com elementos booleans.
lista_inputs = [a, b, c, d, e]
print(all(lista_inputs))

# any(): Retorna True se pelo menos um dos argumentos passados são True; Retorna False, caso contrário.
# IMPORTANTE: any() aceita apenas UM argumento: um iterable com elementos booleans.
print(any(lista_inputs))


