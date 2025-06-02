# Esse programa le uma entrada do usuario e mostra na tela as strings de uma lista
# Especificamente, se a string for "Python", ele mostra uma mensagem especial e 
#   interrompe o laco
lista = ["Java", "C", "Python", "JavaScript", "Ruby"]
for linguagem in lista:
    # Mostrar na tela a linguagem atual
    print("linguagem: {}".format(linguagem))
    
    # Ver se a linguagem eh Python
    if linguagem == "Python":
        # Mostrar uma mensagem especial
        print("Python eh a melhor linguagem de programacao do mundo vlws flws")
        break
