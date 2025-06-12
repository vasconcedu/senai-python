alunos = [] 

while(True):
    operacao = int(input("\n==========\n\nSelecione a operacao:\n\n\t1: cadastrar aluno\n\t2: mostrar aluno\n\t3: remover aluno\n\t4: mostrar lista completa de alunos\n\t5: apagar todos os alunos\n\t6: sair\n\nOperacao> "))
    
    if operacao == 1:
        nome = input("Digite o nome do novo aluno> ")
        alunos.append(nome)
        print("Novo aluno cadastrado com sucesso!")
    elif operacao == 2:
        i = int(input("Digite o indice do aluno> "))
        if i < len(alunos):
            print(f"Aluno {i}: {alunos[i]}")
        else: 
            print("Erro: indice invalido!")
    elif operacao == 3:
        nome = input("Digite o nome do aluno a remover> ")
        indice = -1
        for i in range(0, len(alunos)):
            if nome == alunos[i]:
                indice = i
        if indice != -1:
            alunos.pop(indice)
            print("Aluno removido com sucesso!")
        else: 
            print("Erro: aluno nao encontrado!")
    elif operacao == 4:
        print("Lista completa de alunos:")
        for aluno in alunos:
            print(aluno)
    elif operacao == 5:
        alunos.clear()
        print("Todos os registros foram apagados!")
    elif operacao == 6:
        exit()
    else:
        print("Erro: operacao desconhecida!")
