ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} eh um ano bissexto")
        else:
            print(f"{ano} nao eh um ano bissexto")
    else:
        print(f"{ano} eh um ano bissexto")
else:
    print(f"{ano} nao eh um ano bissexto")
