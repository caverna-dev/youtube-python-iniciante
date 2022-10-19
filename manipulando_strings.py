#### CONCATENAÇÃO DE STRINGS ###
# Trata-se basicamente de uma operacao de adição de duas (ou mais) strings
nome = "Charles"
sobrenome = "Xavier"
nome_completo = nome + " " + sobrenome
print(nome_completo)


#### ACCESSANDO CARACTERES ESPECÍFICOS EM UMA STRING ####
# - strings fazem parte de um conjunto de estruturas que o Python chama de 'sequences' (como veremos mais para frente, sequences tbm sao 'iterables');
# - uma 'sequence' é um objeto especial do python em que dados armazenados na memoria de uma forma sequencial (obedecendo uma ordem), e que podem ser acessados através de um index (índice).
# - o primeiro item (carácter) de uma sequence esta no index 0 (zero).
# - o ultimo item pode ser acessado com o index -1

texto = "Um texto longo que nao diz nada"
print(texto)

# acessando elementos especificos dentro de uma string (iterable)
primeiro_char = texto[0]
print("O primeiro char é:", primeiro_char)

segundo_char = texto[1]
print("O segundo char é:", segundo_char)

ultimo_char = texto[-1]
print("O ultimo char é:", ultimo_char)

penultimo_char = texto[-2]
print("O penultimo_char char é:", penultimo_char)


#### STRING SLICING - FATIAMENTO DE STRINGS ####
# pelo fato de serem 'iterables', as strings no python podem ser
# 'fatiadas', ou seja, você tem a possibilidade de solicitar ao python apenas
# uma 'fatia' de indices especifica.

texto = "Um texto inútil que nao diz nada"
print(texto)

primeiros_8 = texto[0:8]
print("Os primeiros 8 caracteres:", primeiros_8)

primeiros_8_tambem = texto[:8]
print("Também sao os primeiros 8 caracteres:", primeiros_8_tambem)

caracteres_depois_do_8 = texto[8:]
print("Todos os caracters depois do oitavo:", caracteres_depois_do_8)


# também é possível fatiar saltando caracteres
str_numeros = "0123456789"
print(str_numeros)
fateando_e_saltando = str_numeros[0:6:3]
print(fateando_e_saltando)


# ### FORMATAÇAO DE STRINGS ###
# Significa usar valores armazenados em variaveis para de formar uma string,
# para apresentar os dados para os usuários de uma forma legível.
#
# Primeiro Estilo: Substituição de valores com o operador %
# ATENÇÃO: apesar de ainda ser suportado, este estilo é desencorajado.
# Isto porque tem a pior legibilidade e é mais propenso a erros.
age = 60
name = "Charles Xavier"
job = "Líder dos X-Men"

formato_1 = "%s tem %f anos de idade e ele é %s" % (name, age, job)
print(formato_1)

formato_2 = "%(nome)s tem %(idade)s anos de idade e ele é %(ocupacao)s" % {"idade": age, "ocupacao": job, "nome": name, }
print(formato_2)


# Segundo Estilo: Formatação usando a função format()
formato_1 = "{} tem {} anos de idade e ele é {}".format(name, age, job)
print(formato_1)

formato_2 = "{1} tem {2} anos de idade e ele é {0}".format(job, name, age)
print(formato_2)

formato_3 = "{nome} tem {idade} anos de idade e ele é {ocupacao}".format(nome=name, idade=age, ocupacao=job)
print(formato_3)


# Terceiro Estilo: Interpolação com f-strings
# - Suportado apenas no Python3.6 ou maior
# - Metodo recomendado: mais legivel, menos suscetível a erros e bugs

texto = f"{name} tem {age} anos de idade e ele é {job}"
print(texto)

# Pode fazer processamento diretamente dentro dos colchetes
print(f"1 + 1 = {1+1}")
#
print(f"O IMC de alguém com 1.80m e 75Kg é: { 75 / 1.80**2 }")
#
nome = "Charles"
sobrenome = "Xavier"
print(f"O nome completo é: {nome} {sobrenome}")
