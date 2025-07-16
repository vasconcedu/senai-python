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

linha = pygame.Rect(tela_largura/2, 0, 1, tela_altura)

bola_centro_x = tela_largura/2
bola_centro_y = tela_altura/2
bola_raio = 20
bola_velocidade_x = 4
bola_velocidade_y = 4
bola = pygame.Rect(bola_centro_x, bola_centro_y, bola_raio, bola_raio)

while True:
    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (255, 255, 255), linha)
    pygame.draw.rect(tela, (255, 255, 255), retangulo_1)
    pygame.draw.rect(tela, (255, 255, 255), retangulo_2)
    pygame.draw.rect(tela, (255, 255, 255), bola, border_radius=bola_raio)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if bola.top <= 0 or bola.bottom >= tela_altura:
        bola_velocidade_y = -1*bola_velocidade_y
        som_beep.play()

    if bola.right >= retangulo_1.left:
        if retangulo_1.top <= bola.centery <= retangulo_1.bottom:
            bola_velocidade_x = -1*bola_velocidade_x
            som_beep.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if retangulo_1.top >= 0:
            retangulo_1_centro_y -= retangulo_velocidade
    if keys[pygame.K_DOWN]:
        if retangulo_1.bottom <= tela_altura:
            retangulo_1_centro_y += retangulo_velocidade
    if keys[pygame.K_w]:
        if retangulo_2.top >= 0:
            retangulo_2_centro_y -= retangulo_velocidade
    if keys[pygame.K_s]:
        if retangulo_2.bottom <= tela_altura:
            retangulo_2_centro_y += retangulo_velocidade

    bola_centro_x += bola_velocidade_x
    bola_centro_y += bola_velocidade_y

    retangulo_1.center = (retangulo_1_centro_x, retangulo_1_centro_y)
    retangulo_2.center = (retangulo_2_centro_x, retangulo_2_centro_y)
    bola.center = (bola_centro_x, bola_centro_y)

    pygame.display.flip()
    clock.tick(velocidade_tick)
