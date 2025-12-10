import pygame
import sys

pygame.init()

# ---- Configuració bàsica ----
AMPLADA = 800
ALCADA = 600
screen = pygame.display.set_mode((AMPLADA, ALCADA))
pygame.display.set_caption("Arkanoid Simple")

clock = pygame.time.Clock()

# ---- Paddle (barra) ----
paddle = pygame.Rect(350, 550, 100, 15)
vel_paddle = 7

# ---- Bola ----
ball = pygame.Rect(390, 300, 20, 20)
vel_ball = [5, -5]

# ---- Blocs ----
blocs = []
for fila in range(5):
    for col in range(10):
        bloc = pygame.Rect(10 + col*78, 10 + fila*30, 70, 20)
        blocs.append(bloc)

# ---- Joc ----
jugant = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Iniciar joc amb espai
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jugant = True

    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= vel_paddle
    if tecles[pygame.K_RIGHT] and paddle.right < AMPLADA:
        paddle.x += vel_paddle

    if jugant:
        # Moviment bola
        ball.x += vel_ball[0]
        ball.y += vel_ball[1]

        # Rebots laterals
        if ball.left <= 0 or ball.right >= AMPLADA:
            vel_ball[0] *= -1
        
        # Rebot superior
        if ball.top <= 0:
            vel_ball[1] *= -1

        # Comprovar si cau
        if ball.bottom >= ALCADA:
            jugant = False
            ball.x, ball.y = 390, 300

        # Rebot amb la barra
        if ball.colliderect(paddle):
            vel_ball[1] *= -1
        
        # Rebot amb els blocs
        for bloc in blocs[:]:
            if ball.colliderect(bloc):
                blocs.remove(bloc)
                vel_ball[1] *= -1
                break

    # ---- Dibuixar ----
    screen.fill((0, 0, 0))

    # Paddle (blanc)
    pygame.draw.rect(screen, (255, 255, 255), paddle)

    # Bola (vermell)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)

    # Blocs (verd)
    for bloc in blocs:
        pygame.draw.rect(screen, (0, 255, 0), bloc)

    pygame.display.flip()
    clock.tick(60)
