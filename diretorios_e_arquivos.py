##############################
# TRABALHANDO COM DIRETÓRIOS #
##############################

# usaremos recursos disponiveis nos modulos 'os' & 'pathlib'
import os
from pathlib import Path

# 1 - obtendo diretorio onde o arquivo python (modulo) executando está
# current_dir_os = os.getcwd()
# print(current_dir_os)
#
# # # Path() retorna uma referencia a um caminho (path) no sistema de arquivos.
# # # voce pode passar uma string para Path() para indicar qual o diretorio que deseja referenciar: Path("C:\Documentos")
# # # se nenhum argumento for passado para Path(), entao a referencia sera ao diretorio "atual"
# current_dir_pathlib = Path()
# print(current_dir_pathlib.absolute())




# # 2 - listando tudo que existe em um determinado caminho (diretorio)
# ls_dir_os = os.listdir() # se nenhum parametro for passado, assume o diretorio onde este arquivo .py está
# print(ls_dir_os)

# ls_dir_path = Path("/Users/andrelima").iterdir()
# for i in ls_dir_path:
#     print(i)






# 3 - listando apenas arquivos em um diretorio
# for item in os.listdir():
#     if os.path.isfile(item):
#         print(item)

# for item in Path().iterdir():
#     if item.is_file():
#         print(item)










# 4 - listando apenas outros diretórios em um diretorio
# for item in os.listdir():
#     if os.path.isdir(item):
#         print(item)
#
# for item in Path().iterdir():
#     if item.is_dir():
#         print(item)





# 5 - Criando um diretório
# os.mkdir("test_dir_os")

# current_dir = Path("test_dir_path")
# current_dir.mkdir()
















############################
# TRABALHANDO COM ARQUIVOS #
############################

# Quando accessamos um arquivo em python, precisamos informar o "modo" (mode) de acesso ao arquivo. O modo trata de
# informar o python a respeito de 2 coisas:
#   1 - As operações que se deseja realizar sobre o arquivo. Por padrao, python assume que será apenas "leitura" (r).
#   2 - Como tratar os dados (os bits) dentro do arquivo:
#       a - como strings, isto é TEXTO simples. Por padrão, é isto que o Python assume.
#       b - como bytes. Util para manipular arquivos de audio, video, imagens, PDFs, etc..
# Existe ainda outro parametro que pode ser informado ao abrir-se um arquivo:
#   A codificação (encoding) do arquivo, que aplica-se apenas à arquivos abertos em modo texto (item 2a acima),
#   porque o encoding serve como uma "tradução" de bytes para caracteres legíveis ao ser humano. Se um encoding nao
#   for explicitamente informado, o valor padrao aplicado pelo python dependerá do sistema em que está sendo executado.
#   Nao nos aprofundaremos em 'encoding' aqui e deixaremos o sempre o python defini-lo.

# A seguir, começaremos focando exclusivamente no item 1 acima:
# Existem diversos "modes" para acessar arquivos, mas veremos apenas os mais relevantes.

# 'r': read:
#   - o arquivo será aberto no modo 'apenas leitura'. O python vai conseguir ler dados do arquivo, mas nao escrever;
#   - o arquivo precisa existir, caso contrário uma exceçao acontece;

# 'w': write:
#   - o arquivo será aberto no modo 'apenas escrita'. O python consegue escrever dados no arquivo, mas nao ler.
#   - Se o arquivo nao existe, o python criará um.
#   - Se ele existe, informações existentes serão perdidas. O arquivo é sobrescrito.

# 'a': append:
#   - uma variação do modo 'w', que permite o arquivo ser aberto em modo 'escrita', porém para adicionar dados somente
#   ao final do arquivo, preservando dados que já existam
#   - Ainda assim, neste modo, continua nao sendo possivel LER do arquivo

# 'r+': read and wirte:
#   - neste modo é possível tanto ler, quanto escrever no arquivo
#   - a escrita acontece na posiçao que o ponteiro esta, que incialmente é a Zero. Veremos como manipular essa posicao aqui.



# Uma forma de acessar arquivos que funciona, mas que você deve evitar, é usando a função built-in 'open()'

# f = open(file="teste.txt", mode="r")
# # realiza o processamento necessário
# f.close() # muito importante FECHAR o arquivo para evitar memory leaks



# A forma pythonica de se acessar arquivos: usando context manager
# Desta forma, o python garante que o arquivo sempre será fechado e nao haverá problemas de liberacao de memoria
# with open("teste.txt", "r") as f:
#     print(f.mode)
#     conteudo_arquivo = f.read()
#     print(conteudo_arquivo)

# De agora em diante, usaremos apenas "with open()..." para trabalhar com arquivos

# Método .read():
#   - Se nao receber nenhum parametro, le e retorna 100% do conteudo do arquivo
#   - Opcionalmente, pode receber 1 parametro inteiro que indica quantos bytes de dados devem ser lidos

# with open("teste.txt", "r") as f:
#     conteudo_arquivo = f.read(10)
#     print(conteudo_arquivo)


# Método .readline():
#   - le uma linha do arquivo

# with open("teste.txt", "r") as f:
#     linha = f.readline()
#     print(linha)


# Método .readlines():
#   - le todas as linhas do arquivo e retorna uma lista, em que cada elemento é uma das linhas

# with open("teste.txt", "r") as f:
#     conteudo_arquivo = f.readlines()
#     print(conteudo_arquivo)


# Método .write():
#   - Escreve o parametro passado no arquivo

# with open("teste.txt", "r+") as f:
#     novo_personagem = "!"
#     f.write(novo_personagem)



# Método .writelines():
#   - recebe como parametro um iterable e escreve cada elemento do iterable no arquivo
#   - atencao pq o nome do metodo engana: nao ha separacao de linhas entre cada elemento do iterable. Se for necessario
#     colocar cada elemento numa nova linha, o codigo deve garantir isso.

# with open("teste.txt", "a") as f:
#     novo_personagem = ["\n\nNome: Mr. Meeseeks", "\nSobrenome: NA", "\nProfissao: Faz-Tudo", "\nIdade: Variável"]
#     f.writelines(novo_personagem)






# # TRABALHANDO COM ARQUIVOS EM MODO BINÁRIO
# # Aqui estamos nos referindo ao item 2b mencionado anteriormente.
# # Em modo binário, dados são lidos e escritos no arquivo como objetos 'byte'. Portanto, o 'encoding' nao faz sentido.
# # Para abrir um arquivo em modo BINARIO, basta adicionar um 'b' a letra correspondente a qualquer um dos modos que vimos
# # ate agora


# # Tetnando abrir um arquivo de imagem como texto:
# with open("avatar.png", "rb") as f:
#     imagem = f.read()


# Manipulando um arquivo de imagem - OBS: este repositorio nao inclui um arquivo avatar.png. Crie um voce mesmo ;)
with open("avatar.png", "rb") as f_original:
    with open("avatar_copy.png", "wb") as f_copy:
        conteudo_original = f_original.read()
        f_copy.write(conteudo_original)







# FILE POINTER
# Cada byte dentro de um arquivo é mapeado para uma posiçao, começando do 0. O Python mantém um registro que aponta
# para a "posição" atual dentro do arquivo. É desta forma sabe qual o próximo byte a ler, ou o onde deve começar a
# escrever quando necessário.


# # Método .tell():
# #   - retorna um inteiro que corresponde a posicao atual do ponteiro dentro do arquivo
#
# bytes_a_ler = 10
#
# with open("teste.txt", "r") as f:
#     bytes_lidos = f.read(bytes_a_ler)
#     while bytes_lidos:
#         print(bytes_lidos)
#         print(f.tell())
#         bytes_lidos = f.read(bytes_a_ler)


# Método .seek():
#   - reposiciona o ponteiro para a posição passada como parametro

# with open("teste.txt", "r") as f:
#     linha = f.read(10)
#     print(linha)
#
#     f.seek(100)
#
#     linha = f.read(10)
#     print(linha)

