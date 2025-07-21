# Programa para ler dois numeros e mostrar a soma deles na tela

# Sem usar exception
print("Sem usar exception:")
num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite outro numero: "))
print("A soma eh: {}".format(num_1 + num_2))

print("---")

# Usando exception
print("Agora usando exception:")
try:
    num_3 = int(input("Digite um numero: "))
    num_4 = int(input("Digite outro numero: "))
    print("A soma eh: {}".format(num_3 + num_4))
except:
    print("Erro ao ler numeros!")

print("Esse print sempre executa...")
