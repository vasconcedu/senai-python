while True:
    nome = input("Nome: ")
    senha = input("Senha: ")
    if nome == "Pythonio" and senha == "senhadopythonio":
        print("Bem-vindo, {}!".format(nome))
        break
    else: 
        print("Tente novamente!")
