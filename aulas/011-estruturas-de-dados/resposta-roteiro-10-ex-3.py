lista = []

def ler():
    nome = input("nome do aluno> ")
    if nome == "parar":
        return None, None
    nota = float(input("nota do aluno> "))
    return nome, nota

while(True):
    nome, nota = ler()
    if nome != None and nota != None:
        lista.append( [nome, nota] )
    else:
        break

print(lista)
