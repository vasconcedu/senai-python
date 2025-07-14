import pygame

pygame.init()

pygame.display.set_caption("Pong")

tela_largura = 800
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))

retangulo_largura = 24
retangulo_altura = 120

retangulo_1_centro_x = tela_largura - retangulo_largura/2
retangulo_1_centro_y = tela_altura/2
retangulo_1 = pygame.Rect(retangulo_1_centro_x, retangulo_1_centro_y, retangulo_largura, retangulo_altura)
retangulo_1.center = (retangulo_1_centro_x, retangulo_1_centro_y)

while True:
    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (255, 255, 255), retangulo_1)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
