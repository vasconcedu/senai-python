peso = float(input("Digite o peso da pessoa em kg: "))
altura = float(input("Digite a altura da pessoa em m: "))

if peso <= 0:
    print("Peso invalido")
elif altura <= 0:
    print("Altura invalida")
else:
    imc = peso / (altura ** 2)

    print(f"O IMC da pessoa é: {imc}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso normal")
    elif 24.9 < imc <= 29.9:
        print("Sobrepeso")
    elif 29.9 < imc <= 39.9:
        print("Obesidade")
    elif 39.9 < imc:
        print("Obesidade grave")
