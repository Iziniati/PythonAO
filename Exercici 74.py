import pygame
import random

# Inicialització de Pygame
pygame.init()

# Configuració de la finestra
AMPLADA = 800
ALT = 600
finestra = pygame.display.set_mode((AMPLADA, ALT))
pygame.display.set_caption("Arkanoid Simple")

# Colors
NEGRO = (0, 0, 0)
BLANC = (255, 255, 255)

# Carregar imatges (mateix directori)
fons = pygame.image.load("fons.png")
barreta_img = pygame.image.load("barreta.png")
bola_img = pygame.image.load("bola.png")
bloc_img = pygame.image.load("bloc.png")

# Propietats barra
barreta_w = barreta_img.get_width()
barreta_h = barreta_img.get_height()
barreta_x = AMPLADA // 2 - barreta_w // 2
barreta_y = ALT - 50
velocitat_barreta = 7

# Propietats bola
bola_w = bola_img.get_width()
bola_h = bola_img.get_height()
bola_x = AMPLADA // 2 - bola_w // 2
bola_y = barreta_y - bola_h
bola_vel_x = 4
bola_vel_y = -4
bola_en_moviment = False

# Crear blocs
filas = 5
columnes = 8
bloc_w = bloc_img.get_width()
bloc_h = bloc_img.get_height()
blocs = []

for fila in range(filas):
    for col in range(columnes):
        x = col * (bloc_w + 10) + 35
        y = fila * (bloc_h + 10) + 50
        blocs.append(pygame.Rect(x, y, bloc_w, bloc_h))

# Rellotge
clock = pygame.time.Clock()

# Bucle principal
en_joc = True
while en_joc:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_joc = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bola_en_moviment = True

    # Tecles premudes
    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT]:
        barreta_x -= velocitat_barreta
        if barreta_x < 0:
            barreta_x = 0
    if tecles[pygame.K_RIGHT]:
        barreta_x += velocitat_barreta
        if barreta_x > AMPLADA - barreta_w:
            barreta_x = AMPLADA - barreta_w

    # Moviment bola
    if bola_en_moviment:
        bola_x += bola_vel_x
        bola_y += bola_vel_y

        # Col·lisions amb les parets
        if bola_x <= 0 or bola_x >= AMPLADA - bola_w:
            bola_vel_x *= -1
        if bola_y <= 0:
            bola_vel_y *= -1
        if bola_y >= ALT - bola_h:
            bola_en_moviment = False
            bola_x = AMPLADA // 2 - bola_w // 2
            bola_y = barreta_y - bola_h
            bola_vel_x = 4 * random.choice([-1, 1])
            bola_vel_y = -4

        # Col·lisió amb la barra
        barreta_rect = pygame.Rect(barreta_x, barreta_y, barreta_w, barreta_h)
        bola_rect = pygame.Rect(bola_x, bola_y, bola_w, bola_h)
        if bola_rect.colliderect(barreta_rect):
            bola_vel_y *= -1

        # Col·lisions amb blocs
        for bloc in blocs[:]:
            if bola_rect.colliderect(bloc):
                blocs.remove(bloc)
                bola_vel_y *= -1
                break

    # Dibuixar tot
    finestra
