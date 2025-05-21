# Este programa le 3 entradas do usuario e imprime na tela
# - Nome
# - Idade
# - Cidade

# Ler entradas 

nome = input("Digite seu nome: ") # Le o nome do usuario para a variavel nome
idade = input("Digite sua idade: ") # Le a idade do usuario para a variavel idade
cidade = input("Digite sua cidade: ") # Le a cidade do usuario para a variavel cidade

# Imprimir saida

# Diferentes formas de formatar a string com a mensagem para imprimir na tela
# Vao imprimir exatamente a mesma coisa! 

# Forma 1. Usando concatenacao de strings (operador +)
print("Ola, " + nome + " de " + idade + " anos de " + cidade + "!")

# Forma 2. Usando o metodo format
print("Ola, {} de {} anos de {}!".format(nome, idade, cidade))

# Forma 3. Usando a forma reduzida do metodo format
print(f"Ola, {nome} de {idade} anos de {cidade}!")
