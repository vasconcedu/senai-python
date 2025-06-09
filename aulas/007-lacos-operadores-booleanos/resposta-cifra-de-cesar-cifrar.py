# Solucao para a cifra de Cesar usando somente 
#   estruturas da linguagem Python que nos ja 
#   aprendemos ao longo do curso

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("*** Cifra de Cesar - cifrar ***")

frase = input("Digite a frase a cifrar> ")
chave = int(input("Chave> "))

frase_cifrada = ""

for letra_frase in frase:
    for i in range(0, len(alfabeto)):
        if alfabeto[i] == letra_frase:
            frase_cifrada = frase_cifrada + alfabeto[
                (i + chave) % len(alfabeto)
            ]

print(f"Frase cifrada: {frase_cifrada}")
