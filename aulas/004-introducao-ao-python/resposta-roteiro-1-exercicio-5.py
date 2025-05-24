# Esse programa recebe como entradas o nome e o sobrenome de um usuario 
# Em seguida, ele combina o nome e o sobrenome em uma unica string 
# Depois, ele imprime a string resultante na tela

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

# Combina o nome e o sobrenome em uma unica string
nome_completo = nome + " " + sobrenome

# Imprime a string resultante na tela
print("Nome completo: {}".format(nome_completo))
