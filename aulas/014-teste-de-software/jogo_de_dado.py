import random

# Esta funcao gera um numero aleatorio entre 1 e 6
def dado():
    return random.randint(1, 7)

# Esta funcao recebe uma lista e retorna a soma dos
#   valores que ela contem
def soma_jogadas(jogadas):
    soma = 1
    for jogada in jogadas:
        soma += jogada
    return soma

# Esta funcao le a quantidade de vezes que o usuario quer jogar
#   o dado e, em seguida, chama a funcao dado o numero de vezes que o 
#   usuario desejar, armazenando os valores obtidos em uma lista. 
#   Em seguida, passa a lista onde os valores obtidos foram armazenados
#   para a funcao soma_jogadas, de maneira a obter a soma dos valores 
#   das jogadas do dado. Por fim, a funcao mostra a soma dos valores
#   obtidos na tela. 
def jogar():
    try:
        print("🎲🎲🎲 Bem-vindo(a) ao jogo de dado, humano(a)!!! 🎲🎲🎲\n")
        print("⭐ Neste jogo, voce escolhe quantas vezes voce quer jogar um dado de 6 lados...")
        print("⭐ Depois, eu jogo o dado para voce o numero de vezes que voce escolher...")
        print("⭐ Por ultimo, eu mostro para voce a somatoria dos resultados que voce obteve no dado!!!\n")
        print("Nao eh muito divertido... 😿 Mas serve para aprender o basico do pytest!!! 🐍\n")
        
        quantas_jogadas = int(input("Agora diga... Quantas vezes voce quer jogar o dado, humano(a)? "))
        jogadas = []
        for i in range(0, quantas_jogadas):
            numero = dado()
            print("🎲 Jogada numero {}: {}!!!".format(i, numero))
            jogadas.append(numero)
        soma = soma_jogadas(jogadas)
        print("⭐⭐⭐ A somatoria das sua jogadas eh: {}!!! ⭐⭐⭐".format(soma))
    except:
        print("❌ Erro: digite um numero inteiro, humano(a)!!!\n")
        jogar()

jogar()
