import random 

matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(10 * random.random())

print(matriz)
