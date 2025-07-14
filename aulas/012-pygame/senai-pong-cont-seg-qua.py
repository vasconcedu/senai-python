import pygame

pygame.init()

clock = pygame.time.Clock()
velocidade_tick = 64

pygame.display.set_caption("Pong")

tela_largura = 800
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))

retangulo_largura = 24
retangulo_altura = 120
retangulo_velocidade = 8

retangulo_1_centro_x = tela_largura - retangulo_largura/2
retangulo_1_centro_y = tela_altura/2
retangulo_1 = pygame.Rect(retangulo_1_centro_x, retangulo_1_centro_y, retangulo_largura, retangulo_altura)
retangulo_1.center = (retangulo_1_centro_x, retangulo_1_centro_y)

retangulo_2_centro_x = retangulo_largura/2
retangulo_2_centro_y = tela_altura/2
retangulo_2 = pygame.Rect(retangulo_2_centro_x, retangulo_2_centro_y, retangulo_largura, retangulo_altura)
retangulo_2.center = (retangulo_2_centro_x, retangulo_2_centro_y)

while True:
    tela.fill((0, 0 ,0))

    pygame.draw.rect(tela, (255, 255, 255), retangulo_1)
    pygame.draw.rect(tela, (255, 255, 255), retangulo_2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        retangulo_1_centro_y -= retangulo_velocidade
    if teclas[pygame.K_DOWN]:
        retangulo_1_centro_y += retangulo_velocidade

    retangulo_1.center = (retangulo_1_centro_x, retangulo_1_centro_y)

    pygame.display.flip()
    clock.tick(velocidade_tick)
