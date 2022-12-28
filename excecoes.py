# Excecoes ocorrem quando algum erro acontece em tempo tempo de execuçao
# Isso significa que há uma diferença entre erros de sintaxe (SyntaxError) e exceções.
#   -> Se o interpretador Python encontra um problema no seu código durante o processo de PARSING: SyntaxError
#   -> Se o seu coódigo já foi validado e carregado na memória, mas o Python se depara com um problema durante a
#      execução das intruções: Exception



# Exemplo de erro de sintaxe
# if True:
#     print("ok")

# Exemplos de exceções (apenas alguns)
# 1 - ZeroDivisionError: quando o código tenta realizar um divisao por zero
# def division(a, b):
#     return a/b

# div = division(10, 0)

# 2 - TypeError: quando o tipo de um dado nao condiz com o que se espera para executar uma instrucao
# div = division(1, "texto")

# 3 - IndexError: quando o código tenta indexar uma Sequence com um index maior que o seu proprio tamanho
# my_tuple = (1, 2, 3, 4, 5)
# index_5 = my_tuple[5]

# 4 - KeyError: Tentar acessar uma chave que nao existe em um dicionário
# my_dict = {"nome": "Fulaninho", "altura": 1.87}
# telefone= my_dict["telefone"]


# Para ser resiliente, seu programa precisa antecipar a possibilidade de exceções acontecerem
# Para isso, usamos a estrutura "try/except".
#   - O código indentado no block TRY é aquele em que existe a possibilidade de uma exceção acontecer
#   - O código indentado no bloco EXCEPT é o que "lida" com a exceção, isto é: é acionado apenas se a exceção de fato
#     acontecer

# IMPORTANTE: o block try precisa ser acompanhado de um bloco except. Caso contrário, acontece um SyntaxError

# Existem ainda outros 2 blocos opcionais que podem compor sua estratégia de Tratamento de Exceções: 'else' e 'finally'.
#   - Se incluído, o bloco ELSE executa apenas se nenhuma exceção aconteceu dentro do bloco TRY
#   - Se incluiído, o bloco FINALLY executa sempre, quer uma exceção tenha ocorrido ou não.



# refatorando a funcao division() com try/except:
# def division(a, b):
#     try:
#         d = a/b
#         return d
#     except (ZeroDivisionError, TypeError):
#         print("Os parametros passados nao permitem realizar uma operacao de divisao")
#
#
# div_1 = division(10, 0)
# div_2 = division(10, "2")


# Usando os blocos opcionais 'else' e 'finally'
try:
    l = [1, 2, 3]
    index_2 = l[2]
except IndexError:
    print("a lista contém apenas 3 elementos")
else:
    print("o código dentro do bloco ELSE só executa quando nenhuma exceção acontece dentro do bloco TRY")
finally:
    print("o código dentro do bloco FINALLY sempre executa")



##################################
# Criando suas proprias exceções #
##################################

# - Um pouco mais de teoria sobre POO e CLASSES em python:
#   - Como já vimos, o conceito de classes está associado ao Paradigma da Programação Orientada a Objetos (POO)
#   - Dentro da POO, existe tbm o conceito de HERANÇA: classes podem herdar de outras classes.
#   - Outros termos tbm usados para se referir a isso é "estender" ou "especializar"
#   - À classe que 'herda' (ou 'estende', ou 'especializa') também damos o nome de  classe FILHA. Dizemos que é uma
#     "Subclasse de XYZ"
#   - À classe que foi 'herdada' (ou 'estendida', 'especializada'), também damos o nome de classe PAI. Dizemos que é a
#     "Superclasse de XPTO"
#
#   - Algumas infos importantes:
#       1 - Subclasses podem também ser superclasses (herança indireta). Exemplo:
#           - Class A: ...
#             Class B(A): ...
#             Class C(B): ...
#
#           - Neste exemplo, 'A' é a superclasse direta de 'B'; 'B' é a superclasse direta de 'C'.
#             Porém 'A' também é considerada superclasse de 'C', já que a Superclasse de 'C' é subclasse de 'A'
#
#       2 - Em Python, TUDO é indiretamente subclasse de uma classe fundamental chamada 'object'
#
# - Todas as exceções em python são implementadas como subclasses de 'Exception'

# arithmetic_is_subclass = issubclass(ZeroDivisionError, ArithmeticError)
#
# print(arithmetic_is_subclass)

# Tudo que você precisa fazer para customizar suas próprias Exceções é cliar uma subclasse de 'Exception', ou talvez
# de alguma outra Subclasse de Exception.

# Exemplo 1
# Suponha que você precisa validar a idade de um usuário que esta tentando se registrar para usar um app que voce criou.
# As condicoes sao que ele precisa ter mais que 18 e menos que 120 anos.

class AgeOutOfRangeException(Exception):
    pass

def valida_idade_usuario(idade):
    if 18 > idade or idade >= 120:
        raise AgeOutOfRangeException("A Idade do usuário precisa ser maior ou igual a 18 e menor que 120.")

# em algum momento dentro do seu programa, depois de capturar/calcular a idade do usuário:
idade_usuario = 17

try:
    valida_idade_usuario(idade=idade_usuario)
except AgeOutOfRangeException as err:
    print(err)
else:
    print("Idade válida... continuando com o processamento do registro")



# TENTE VOCE MESMO!
# Exemplo 2: Voltando ao exemplo da funçao division(), em vez de tratar individualmente ZeroDivisionError ou TypeError,
# agora voce precisa lançar uma exceçao mais genérica que apenas sinaliza um problema de divisao

# class ErroDeDivisaoInesperado(ArithmeticError):
#     pass
#
#
# def division(a, b):
#     try:
#         d = a/b
#         return d
#     except (ZeroDivisionError, TypeError):
#         raise ErroDeDivisaoInesperado("Um erro cabuloso aconteceu ao chamar a funçao 'division()'. Chama o Sênior pra debugar...")
#
# try:
#     division(1, 0)
# except ErroDeDivisaoInesperado as err:
#     print(err)