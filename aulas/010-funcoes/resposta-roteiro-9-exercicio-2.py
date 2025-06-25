with open("cancao-do-exilio.txt") as f:
    cont = f.read()
    f.close()
    caracs = 0
    linhas = 0
    
    for c in cont:
        caracs += 1
        if c == '\n':
            linhas += 1
    
    linhas += 1 # A ultima linha nunca tem \n
    
    print("Caracs: {}".format(caracs))
    print("Linhas: {}".format(linhas))
