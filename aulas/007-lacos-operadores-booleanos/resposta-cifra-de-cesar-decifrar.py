# Solucao para a cifra de Cesar usando somente 
#   estruturas da linguagem Python que nos ja 
#   aprendemos ao longo do curso

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("*** Cifra de Cesar - decifrar ***")

frase_cifrada = input("Digite a frase a decifrar> ")
chave = int(input("Chave> "))

frase = ""

for letra_frase_cifrada in frase_cifrada:
    for i in range(0, len(alfabeto)):
        if alfabeto[i] == letra_frase_cifrada:
            frase = frase + alfabeto[
                (i - chave) % len(alfabeto)
            ]

print(f"Frase: {frase}")
