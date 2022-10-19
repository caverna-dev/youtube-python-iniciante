# condicionais 'if' em python sao uma das formas de 'CONTROLE DE FLUXO' que a linguagem oferece. Veremos outros em liçoes futuras.
# É o que permite realizar "Tomadas de Decisões" durante a execução do código, baseado em OPERACOES e/ou COMPARACOES lógicas
# (Videos #3 e #4, respectivamente, da playlist Python Iniciante).

#########################################
## Exemplos com if statement "simples" ##
#########################################

# Exemplo 1:
print("O exemplo 1 começa aqui!")

if True:
    print("esta linha sempre vai executar, pq a condição é 'True'")

print("Ja passamos pela primeira tomada de decisão.")

if False:
    print("esta linha nunca vai executar, pq a condição é 'False'")

print("Já passamos pela segunda tomada de decisão.")


# Exemplo 2:
print("O exemplo 2 começa aqui!")

nome_usuario = "James"
sobrenome_usuario = "Howlett"
idade_usuario = 150

if sobrenome_usuario.startswith("H") and "a" in nome_usuario and idade_usuario >= 100:
    print(f"qualquer outra coisa")

if idade_usuario >= 18:
    print(f"O usuário {nome_usuario} {sobrenome_usuario} já é maior de idade tem {idade_usuario} anos de idade!")


#
# ##########################
# ## Exemplos com if/else ##
# ##########################

# Exemplo 3:
print("O exemplo 3 começa aqui!")

if False:
    print("esta linha nao vai executar, pq a condição é 'False'")
# para usar if/else, a proxima instrucao na mesma indentacao do IF, tem que ser o ELSE.
else:
    print("esta linha vai executar, pq a condição anterior nao executou")

#
# Exemplo 4: Reescrevendo o Exemplo 2, mas agora do jeito certo! ;)
print("O exemplo 4 começa aqui!")

nome_usuario = "James"
sobrenome_usuario = "Howlett"
idade_usuario = 150

# # No exemplo 2 anterior, repare que as condicoes sao mutuamente exclusivas:
# # - A idade de alguém é menor a 18; ou
# # - A idade de alguém é maior-ou-igual a 18.
# # Nao existe outra possibilidade. Portanto, este é o caso ideal para if/else
# # Vamos reescrever aquela lógica
if idade_usuario < 18:
    print(f"O usuário {nome_usuario} {sobrenome_usuario} é menor de idade!")
else:
    print(f"O usuário {nome_usuario} {sobrenome_usuario} já é maior de idade tem {idade_usuario} anos de idade!")


# ###############################
# ## Exemplos com if/elif/else ##
# ###############################
#
# Exemplo 5:
print("Começando o exemplo 5!")
# Apenas uma condição irá executar
condicao_a = False
condicao_b = False
condicao_c = False
condicao_d = False

if condicao_a:
    print("executei na primeira tomada de decisao")
elif condicao_b:
    print("executei na segunda tomada de decisao")
elif condicao_c:
    print("executei na terceira tomada de decisao")
elif condicao_d:  # você pode ter quantos 'elifs' achar necessário
    print("executei na quarta tomada de decisao")
else:  # O else é opcional
    print("nenhuma condicao executou, entao o 'else' executa")

print("Acabou!")