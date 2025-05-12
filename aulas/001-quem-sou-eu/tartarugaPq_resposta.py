#!/usr/bin/python

#
# tartarugaPq.py
#
# Programa para resolver o problema da tartaruga e do pao de queijo no
# labirinto. Se houver um pao de queijo dentro do labirinto, a tartaruga deve
# encontrar o pao de queijo, soltar um barbante na posicao onde o encontrou
# e voltar ate a sua posicao de partida pelo caminho mais curto desta ate o
# pao de queijo, desenrolando o barbante para marcar o caminho.
#
# Autores:
#
# ... <...@...>
# ... <...@...>
#

import turtle
import random

""" *********** SOMENTE ESTE TRECHO DE CODIGO DEVE SER ALTERADO ************ """

ladoLabirinto = 10 # Lado do labirinto
probPq = 1.0 # Probabilidade de haver um pao de queijo no labirinto

# Manda a tartaruga procurar o pao de queijo a direita
def procuraDireita() :
    viraDireita()
    r = procuraFrente()
    viraEsquerda()
    return r

# Manda a tartaruga procurar o pao de queijo a esquerda
def procuraEsquerda() :
    viraEsquerda()
    r = procuraFrente()
    viraDireita()
    return r

# Manda a tartaruga procurar o pao de queijo a frente
def procuraFrente() :
    if (temParedeFrente()) :
        return False
    else :
        andaFrente()
        r = procuraPaoDeQueijo()
        andaTras()
        return r

# Procura o pao de queijo na posicao corrente da tartaruga no labirinto
def procuraPaoDeQueijo() :    

    if achou() :
        desenrolaBarbante()
        return True
    else :
        return procuraEsquerda() or procuraFrente() or procuraDireita()

""" ************************************************************************ """










"""
                    _______ ______ _   _  _____          ____  _ _ _ 
                 /\|__   __|  ____| \ | |/ ____|   /\   / __ \| | | |
                /  \  | |  | |__  |  \| | |       /  \ | |  | | | | |
               / /\ \ | |  |  __| | . ` | |      / /\ \| |  | | | | |
              / ____ \| |  | |____| |\  | |____ / ____ \ |__| |_|_|_|
             /_/    \_\_|  |______|_| \_|\_____/_/    \_\____/(_|_|_)

                              
********************** NAO ALTERAR NADA DAQUI PARA BAIXO **********************

    Esta parte do programa serve apenas para gerar o labirinto aleatorio 
    e para movimentar a tartaruga. A unica informacao necessaria desta parte
    do programa para resolver o problema sao os nomes e comportamentos das
    funcoes que voce pode chamar. As unicas funcoes que podem ser chamadas
    desta parte do programa sao:

        1. viraDireita()
            |
            -> Faz a tartaruga virar a direita sobre o proprio eixo

        2. viraEsquerda()
            |
            -> Faz a tartaruga virar a esquerda sobre o proprio eixo

        3. temParedeFrente()
            |
            -> Verifica se tem uma parede diante da tartaruga

        4. andaFrente()
            |
            -> Faz a tartaruga andar para a frente (desobedece se houver parede)

        5. andaTras()
            |
            -> Faz a tartaruga andar para tras (desobedece se houver parede)

        6. desenrolaBarbante()
            |
            -> Faz a tartaruga desenrolar o barbante no chao

        7. achou()
            |
            -> Verifica se a tartaruga esta sobre o pao de queijo

"""

ladoCelula = 20 # Tamanho do lado das celulas do labirinto em pixels
xPq = 0 # Coordenada x do pao de queijo (gerada aleatoriamente)
yPq = 0 # Coordenada y do pao de queijo (gerada aleatoriamente)
x = 0 # Coordenada x da tartaruga
y = 0 # Coordenada y da tartaruga

# Lembrar que o heading do turtle eh:
#
#      90
#      ^
# 180 < > 0
#      v
#     270       
#

# Calcular vizinhos da celula recebida como argumento. Retorna
# uma lista de tuplas [ (parede que leva ao vizinho,i,j) ... ]
# Posicao relativa dos vizinhos:
#
#    3
#    _
# 2 |_| 0
#
#    1
#
def vizinhos(i,j) :

    global ladoLabirinto
    
    if (i == 0 and j == 0) :
        viz = [0,1]
    elif (i == 0 and j == ladoLabirinto-1) :
        viz = [1,2]
    elif (i == ladoLabirinto-1 and j == ladoLabirinto-1) :
        viz = [2,3]
    elif (i == ladoLabirinto-1 and j == 0) :
        viz = [3,0]
    elif (i == 0) :
        viz = [0,1,2]
    elif (j == ladoLabirinto-1) :
        viz = [1,2,3]
    elif (i == ladoLabirinto-1) :
        viz = [2,3,0]
    elif (j == 0) :
        viz = [3,0,1]
    else :
        viz = [0,1,2,3]

    for v in range(0, len(viz)) :
        if (viz[v] == 0) :
            viz[v] = (0,i,j+1)
        elif (viz[v] == 1) :
            viz[v] = (1,i+1,j)
        elif (viz[v] == 2) :
            viz[v] = (2,i,j-1)
        else :
            viz[v] = (3,i-1,j)

    return viz

# Gera um labirinto quadrado de lado ladoLabirinto recursivamente,
# iniciando na celula enderecada por i,j
def geraLabirinto(i,j) :

    global labirinto

    # Marcando como visitado
    labirinto[i][j]['visitado'] = 1

    # Determinando quem sao os vizinhos
    viz = vizinhos(i,j) # viz = [ (parede,i,j), ... ]
    # Ordem aleatoria de visita aos vizinhos
    random.shuffle(viz)

    for v in range(0,len(viz)) :
        if (labirinto[viz[v][1]][viz[v][2]]['visitado'] != 1) :
            # Abrindo as paredes das celulas
            labirinto[i][j]['paredes'][viz[v][0]] = False
            labirinto[viz[v][1]][viz[v][2]]['paredes'][(viz[v][0] + 2) % 4] = False

            # Indo visitar o proximo vizinho
            geraLabirinto(viz[v][1],viz[v][2])

    return labirinto

# Desenha o pao de queijo em posicao aleatoria dentro do labirinto
def desenhaPaoDeQueijo() :

    global c
    global xPq
    global yPq
    global ladoLabirinto
    global probPq

    if (random.random() < probPq) :

        # Seleciona um dos 3 quadrantes mais afastados da posicao
        # onde a tartaruga aparece (quina superior esquerda do labirinto)
        # => a escolha eh um pouco deterministica
        xPq = random.randint(int(ladoLabirinto/2), ladoLabirinto-1)
        yPq = random.randint(int(ladoLabirinto/2), ladoLabirinto-1)

        turtle.setpos(c[yPq][xPq][0], c[yPq][xPq][1])
        turtle.pd()
        turtle.dot(10, 'orange')
        turtle.pu()
    else :
        xPq = -1
        yPq = -1

# Desenha o labirinto gerado na tela
def desenhaLabirinto() :
    global labirinto
    global ladoLabirinto
    global ladoCelula

    turtle.hideturtle()
    turtle.shape('turtle')
    turtle.color('black')
    turtle.bgcolor('#ccff99')
    turtle.speed('fastest')
    turtle.pu()

    # Quina superior do quadrado em funcao do lado da celula do labirinto
    turtle.setpos(-ladoCelula * ladoLabirinto/2, ladoCelula * ladoLabirinto/2)
    
    for i in range(0, ladoLabirinto) :
        turtle.setheading(0) # Para la >
        turtle.forward(ladoCelula) # Avanca para a quina de la > da celula
        for j in range(0, ladoLabirinto) :

            # Desenhar (ou passar por cima sem desenhar) cada uma
            # das 4 paredes da celula
            for p in range(0,4) :

                # Se houver essa parede, pendown
                if (labirinto[i][j]['paredes'][p]) :
                    turtle.pd()

                # Em funcao do indice da parede, anda em uma posicao (so
                # desenha de tiver pendown)
                if (p == 0) :
                    turtle.setheading(270)
                    turtle.forward(ladoCelula)
                elif (p == 1) :
                    turtle.setheading(180)
                    turtle.forward(ladoCelula)
                elif (p == 2) :
                    turtle.setheading(90)
                    turtle.forward(ladoCelula)
                else :
                    turtle.setheading(0)
                    turtle.forward(ladoCelula)

                turtle.pu() # Penup, para parar de desenhar essa parede,
                            # agora so na proxima

            # Proxima coluna >
            turtle.setheading(0)
            turtle.forward(ladoCelula)

        # Proxima linha v
        turtle.setheading(270)
        turtle.forward(ladoCelula)
        turtle.setheading(180)
        turtle.forward((ladoLabirinto+1)*ladoCelula)

# Retorna uma celula do labirinto com os parametros visitado = 0 (nao visitado)
# e paredes = [1,1,1,1] (todas as paredes estao completas inicialmente)
def criaCelula(p1, p2, p3, p4):
    celula = {}
    celula['visitado'] = 0
    celula['paredes'] = [p1,p2,p3,p4]
    return celula 

# Manda a tartaruga virar a direita (muda heading do turtle)
def viraDireita() :
    turtle.setheading((turtle.heading() - 90) % 360)

# Manda a tartaruga virar a esquerda (muda heading do turtle)
def viraEsquerda() :
    turtle.setheading((turtle.heading() % 360) + 90)

# Verifica se ha uma parede a frente da tartaruga, com relacao ao
# seu valor de heading (do turtle)
def temParedeFrente() :
    global x
    global y
    if (turtle.heading() == 0) :
        return labirinto[y][x]['paredes'][0]
    elif (turtle.heading() == 90) :
        return labirinto[y][x]['paredes'][3]
    elif (turtle.heading() == 180) :
        return labirinto[y][x]['paredes'][2]
    else :
        return labirinto[y][x]['paredes'][1]

# Verifica se ha uma parede atras da tartaruga, com relacao ao
# seu valor de heading (do turtle)
def temParedeAtras() :
    global x
    global y
    if (turtle.heading() == 0) :
        return labirinto[y][x]['paredes'][2]
    elif (turtle.heading() == 90) :
        return labirinto[y][x]['paredes'][1]
    elif (turtle.heading() == 180) :
        return labirinto[y][x]['paredes'][0]
    else :
        return labirinto[y][x]['paredes'][3]

# Manda a tartaruga avancar de uma celula com relacao ao seu heading
# Lembrar: x >, y v
def andaFrente() :
    global x
    global y
    global ladoCelula

    if (not temParedeFrente()) :
        if (turtle.heading() == 0) :
            x = x + 1
        elif (turtle.heading() == 90) :
            y = y - 1
        elif (turtle.heading() == 180) :
            x = x - 1
        else :
            y = y + 1

        turtle.forward(ladoCelula)
    else :
        print('Chamou andaFrente(), mas tem uma parede na minha frente !')

# Manda a tartaruga recuar de uma celula com relacao ao seu heading
# Lembrar: x >, y v
def andaTras() :
    global x
    global y
    global ladoCelula

    if (not temParedeAtras()) :
        if (turtle.heading() == 0) :
            x = x - 1
        elif (turtle.heading() == 90) :
            y = y + 1
        elif (turtle.heading() == 180) :
            x = x + 1
        else :
            y = y - 1

        turtle.backward(ladoCelula)
    else :
       print('Chamou andaTras(), mas tem uma parede atras de mim !') 

# Manda a tartaruga soltar o barbante (i.e. pendown no turtle)
def desenrolaBarbante() :
    turtle.pd()

# Verifica se a tartaruga achou o pao de queijo, ou seja, se a posicao da
# tartaruga eh igual a posicao do pao de queijo
def achou() :

    global x
    global y
    global xPq
    global yPq

    return x == xPq and y == yPq

# Funcao principal do programa
def __main__() :

    global labirinto
    global c
    global ladoLabirinto

    if (not isinstance(ladoLabirinto, int) or ladoLabirinto < 2) :
        print('ERRO: ladoLabirinto deve ser um inteiro e >= 2 !')
        exit()

    if (not isinstance(probPq, float) or probPq > 1 or probPq < 0) :
        print('ERRO: espera-se probPq float e 0 <= probPq <= 1 !')
        exit()

    # Cria e desenha o labirinto
    labirinto = [[criaCelula(True,True,True,True) for i in range(ladoLabirinto)] for j in range(ladoLabirinto)] 
    labirinto = geraLabirinto(0,0)
    desenhaLabirinto()

    # Matriz de posicoes no centro das celulas do labirinto
    c = [[(0,0) for i in range(ladoLabirinto)] for j in range(ladoLabirinto)]

    pX = -ladoCelula * ladoLabirinto/2 + ladoCelula/2
    pY = ladoCelula * ladoLabirinto/2 - ladoCelula/2

    for i in range(0, ladoLabirinto) :
        for j in range(0, ladoLabirinto) :
            c[j][i] = (pX,pY)
            pY = pY - ladoCelula

        pY = ladoCelula * ladoLabirinto/2 - ladoCelula/2
        pX = pX + ladoCelula

    # Cria e desenha o pao de queijo
    desenhaPaoDeQueijo()

    # Posiciona turtle em (0,0)
    turtle.showturtle()
    turtle.color('green')
    turtle.setpos(c[0][0][0],c[0][0][1])
    turtle.setheading(0)
    turtle.speed('slowest')

    # Buscar o pao de queijo a partir da origem,
    # que eh a posicao inicial da tartaruga
    procuraPaoDeQueijo()

    # Mantem graficos abertos
    turtle.done()

# Chama a funcao principal do programa
__main__()

""" ************************************************************************ """
