def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

a = float(input("a> "))
b = float(input("b> "))
op = input("op> ")

if op == "+":
    print(soma(a, b))
elif op == "-":
    print(subtracao(a, b))
elif op == "*":
    print(multiplicacao(a, b))
elif op == "/":
    print(divisao(a, b))
else:
    print("Erro: op desconhecida")
