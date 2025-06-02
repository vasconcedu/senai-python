idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade invalida")
elif 0 <= idade <= 12: 
    print("Crianca")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")
