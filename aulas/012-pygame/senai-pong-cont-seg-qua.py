import pygame 

pygame.init()

clock = pygame.time.Clock()
velocidade_tick = 64

pygame.display.set_caption("Pong")
pygame.font.init()
fonte = pygame.font.Font('summer-pixel-22.ttf', 36)

pygame.mixer.init()
som_beep = pygame.mixer.Sound("beep.mp3")
som_ponto = pygame.mixer.Sound("ponto.mp3")

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

pontos_1 = 0
pontos_2 = 0

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

    pontos_1_texto = fonte.render("{}".format(pontos_1), True, (255, 255, 255))
    pontos_2_texto = fonte.render("{}".format(pontos_2), True, (255, 255, 255))
    pontos_1_retangulo = pontos_1_texto.get_rect()
    pontos_2_retangulo = pontos_2_texto.get_rect()
    pontos_1_retangulo.center = (tela_largura*0.25, tela_altura*0.1)
    pontos_2_retangulo.center = (tela_largura*0.75, tela_altura*0.1)
    tela.blit(pontos_1_texto, pontos_1_retangulo)
    tela.blit(pontos_2_texto, pontos_2_retangulo)

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

    if bola.left <= retangulo_2.right:
        if retangulo_2.top <= bola.centery <= retangulo_2.bottom:
            bola_velocidade_x = -1*bola_velocidade_x
            som_beep.play()
    
    if bola.centerx >= tela_largura or bola.centerx <= 0:
        bola_centro_x = tela_largura/2
        bola_centro_y = tela_altura/2
        if bola.centerx >= tela_largura:
            pontos_1 += 1
            som_ponto.play()
        else:
            pontos_2 += 1
            som_ponto.play()

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
