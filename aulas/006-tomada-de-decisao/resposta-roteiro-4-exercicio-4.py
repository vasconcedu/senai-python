# Este programa resolve o exercicio 4 do roteiro 4 de tomada de decisao
#   utilizando somente estruturas qus nos ja conhecemos ate aqui. Entretanto,
#   poderemos propor uma solucao mais elegante com recursos que vamos aprender
#   mais adiante no curso. 

saque = int(input("Digite o valor do saque: "))

notas_200 = 0
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0

saque_restante = saque

# Inicialmente, consideramos o saque valido
# String nao eh a melhor forma de representar um estado, mas vamos usar
#   por enquanto para simplificar o codigo. Mais adiante no curso, vamos
#   aprender um tipo de dado mais adequado para isso
saque_valido = "Sim"

if saque_restante > 0:
    # Notas de 200
    notas_200 = saque_restante // 200
    saque_restante = saque_restante - 200 * notas_200

    # Notas de 100
    notas_100 = saque_restante // 100
    saque_restante = saque_restante - 100 * notas_100

    # Notas de 50
    notas_50 = saque_restante // 50
    saque_restante = saque_restante - 50 * notas_50

    # Notas de 20
    notas_20 = saque_restante // 20
    saque_restante = saque_restante - 20 * notas_20

    # Notas de 10
    notas_10 = saque_restante // 10
    saque_restante = saque_restante - 10 * notas_10

    # Tratamento especial para notas menores do que 10
    #   Existem casos de borda a considerar aqui! 
    if saque_restante % 2 == 0: # 8, 6, 4 ou 2 => somente notas de 2
        notas_2 = saque_restante // 2
        saque_restante = saque_restante - 2 * notas_2

    elif saque_restante >= 5: # 9, 7, 5 => uma nota de 5 e o restante em notas de 2
        notas_5 = 1
        saque_restante = saque_restante - 5 * notas_5
        notas_2 = saque_restante // 2
        saque_restante = saque_restante - 2 * notas_2

    else: # Os valores possiveis aqui sao 1 ou 3 => o saque eh invalido 
        notas_2 = saque_restante // 2 # Mero purismo, nao seria necessario nem calcular 
        saque_restante = saque_restante - 2 * notas_2 # Sempre vai sobrar 1    

# Se de cara, o saque restante ja nao for positivo, o saque eh invalido
else:
    saque_valido = "Nao"

# Finalizada a rotina de calculo, verificamos se ainda sobrou algum valor
#   Se tiver sobrado algum valor, o saque eh invalido
if saque_restante > 0:
    saque_valido = "Nao"

# Verificamos a validade do saque e imprimimos a saida 
if saque_valido == "Nao":
    print("Saque invalido")
else:
    print(f"Notas de 200: {notas_200}")
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 20: {notas_20}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Notas de 2: {notas_2}")
