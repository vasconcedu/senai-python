# Esse programa mostra na tela os numeros de 1 a 100 
#   que sao divisiveis por 3 e por 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Achei um! {} eh divisivel por 3 e por 5!".format(i))
