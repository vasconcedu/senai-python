# Este programa utiliza uma tomada de decisao if para
#   verificar se um numero eh maior ou igual a zero

numero = float(input("Digite um numero: "))

# *** ATENCAO: NOVO OPERADOR ***
# O operador >= verifica se um valor eh maior ou igual ao outro
#   Existe o equivalente <= que verifica se um valor eh menor 
#   ou igual ao outro!
if numero >= 0:
    print("O numero eh maior ou igual a zero")
else:
    print("O numero eh menor do que zero")
