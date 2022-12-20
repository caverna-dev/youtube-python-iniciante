### FUNÇÕES ####
# - conceitualmente parecido com função matemática:
#   -> f(x), f(x,y), f(x,y,z,...)
#   -> Algo que recebe qualquer quantidade de parametros, e produz um resultado de acordo com
#      'as definicoes internas' da função.

# - Em programação, uma função define um bloco de código que encapsula uma lógica a ser executada usando os
#   parametros passados para a função

# - Funções em python:
#   -> podem ser declaradas para receber qualquer quantidade de parametros
#   -> mesmas regras de nomenclatura de variáveis

# - A rigor também existe uma diferença entre "parâmetro" e "argumento":
#   -> "parametro" é o que está dentro dos parênteses na declaração da função
#   -> "argumento" é o valor (o objeto) que você associa a um paraâmetro quando invoka a função


# Declarando & Chamando funções em python

def func_sem_parametros():
    for i in range(-5, 5):
        print(i)

func_sem_parametros()


def func_com_parametros(minimo, maximo):
    for i in range(minimo, maximo):
        print(i)

# usando POSITIONAL arguments
func_com_parametros(0, 10)

# usando KEYWORD arguments
func_com_parametros(maximo=10, minimo=0)

def func_com_parametros_default(minimo=0, maximo=10):
    for i in range(minimo, maximo):
        print(i)

# usando os defineaults
func_com_parametros_default()

# alterando os defaults
func_com_parametros_default(minimo=5, maximo=15)


def func_com_e_sem_defaults(x, y=10):
    potencia_x_y = pow(x, y)
    print(potencia_x_y)

func_com_e_sem_defaults(2)

func_com_e_sem_defaults(y=2, x=10)


# funções podem retornar valores:
def calcula_potencia(x, y):
    potencia_x_y = pow(x, y)
    return potencia_x_y

potencia_2_10 = calcula_potencia(2, 10)
print(potencia_2_10)






# - Importância:
#   -> Princípio DRY: Abstração e Reusabilidade
#   -> Legibilidade
#   -> Modularidade

# Problema: Seu programa recebe 3 pares de numeros e deve:
#   1 - informar o resultado da divisao do primeiro numero pelo segundo
#   2 - informar se o numero calculado acima é par
input_1 = (100, 33)
input_2 = (40, 2)
input_3 = (50, 25)

# Caso 1: Repetindo a logica N vezes:
if input_1[1] == 0:
    print("nao eh possivel continuar")
else:
    divisao_1 = input_1[0]/input_1[1]
    print(f"{input_1[0]} dividido por {input_1[1]} = {divisao_1}")
    if divisao_1 % 2 == 0:
        print(f"{divisao_1} é par!")

divisao_2 = input_2[0]/input_2[1]
print(f"{input_2[0]} dividido por {input_2[1]} = {divisao_2}")
if divisao_2 % 2 == 0:
    print(f"{divisao_2} é par!")

divisao_3 = input_3[0]/input_3[1]
print(f"{input_3[0]} dividido por {input_3[1]} = {divisao_3}")
if divisao_3 % 2 == 0:
    print(f"{divisao_3} é par!")


# Caso 2: Usando funções
def divide_e_verifica(numerador, denominador):
    if denominador != 0:
        divisao = numerador / denominador
        print(f"{numerador} dividido por {denominador} = {divisao}")

        if divisao % 2 == 0:
            print(f"{divisao} é par!")
    else:
        return "Nao é possivel continuar"
#
divide_e_verifica(input_1[0], input_1[1])
divide_e_verifica(input_2[0], input_2[1])
divide_e_verifica(input_3[0], input_3[1])



# - Em python costuma-se fazer uma distinção entre os termos "funções" e "métodos" (mas no dia-a-dia isso importa pouco).
#         - "métodos" estão sempre associados a um objeto (um função que define uma ação daquele objeto)
#             - str: .replace(), .strip(), .upper(), .lower()
#             - list: .append(), .index()
#             - dict: .keys(), .values(), .items()
#         - "funções" é o termo mais genérico, e se refere a este conceito de encapsular um bloco de comandos em um
#           "nome" que pode ser posteriormente invocado para executar aquela lógica

class MinhaClasse:

    def metodo_sem_parametro(self):
        print("Oi, Mundo!")

    def metodo_com_parametro(self, param="python"):
        print(f"O parametro passado foi: {param}")


meu_obj = MinhaClasse()

meu_obj.metodo_sem_parametro()
meu_obj.metodo_com_parametro()
