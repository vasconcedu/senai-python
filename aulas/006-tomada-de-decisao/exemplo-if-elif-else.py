# Este programa utiliza uma tomada de decisao if-elif-else para
#   verificar se um numero eh maior do que zero, menor do que zero
#   ou igual a zero

numero = float(input("Digite um numero: "))

# *** ATENCAO: NOVO OPERADOR ***
# O operador > verifica se um valor eh maior do que o outro
if numero > 0:
    print("O numero eh maior do que zero")
# *** ATENCAO: NOVO OPERADOR ***
# O operador < verifica se um valor eh menor do que o outro
elif numero < 0:
    print("O numero eh menor do que zero")
else:
    print("O numero eh igual a zero")
